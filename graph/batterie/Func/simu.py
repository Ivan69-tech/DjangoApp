# -*- coding: utf-8 -*-

import pandas as pd
import datetime
from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.models import Band, ColumnDataSource, HoverTool, BoxZoomTool, PanTool, ResetTool
from bokeh.embed import components
from bokeh.models.annotations import Title

def change_title(plot, element, new_name):
        t = Title()
        t.text = new_name
        plot[element].title = t
        plot[element].title.align = "center"

class Simu() :
    
    def __init__(self) :
        
        self.df = pd.DataFrame()
        self.graph = []
        self.plots = {}
        self.script = ""
        self.div = ""
        
        
    def Simulation(self, type_mod, nb_mod, nb_rack, c_rate, nb_jour, jour_deb,
                   path, h, mass, set_min_c, set_max_c, set_min_f, set_max_f,
                   Pclim, Pchal) :
        
        self.profil_puissance(type_mod, nb_mod, nb_rack, c_rate, nb_jour, jour_deb)
        self.calcul_soc(type_mod, nb_mod, nb_rack, 60)
        self.cons_U(nb_mod)
        self.cons_I()
        self.heat_gen(nb_mod, type_mod)
        self.conditions_ext(path)
        self.bilan_thermique(h, mass, nb_mod, nb_rack, set_min_c, set_max_c,
                             set_min_f, set_max_f, Pclim, Pchal)
        self.trace()
        self.set_title()
        self.bokeh_template()
        
        
       
    
    def profil_puissance(self, type_mod, nb_mod, nb_rack, c_rate, nb_jour, jour_deb) :
        
        self.type_module(type_mod)
        cap = self.e_mod * nb_mod * nb_rack
        
        jour_deb = datetime.datetime.strptime(jour_deb, "%Y-%m-%d")
        time = [jour_deb]
        nb_min = nb_jour * 1440
        tps_ch_min = (1/c_rate)*60
        p_ch = -cap * c_rate
        p_dis = cap * c_rate
        
        heure_deb_ch = datetime.datetime.replace(jour_deb, hour = 8)
        heure_fin_ch = heure_deb_ch + datetime.timedelta(minutes = tps_ch_min)
        heure_deb_dis = heure_fin_ch + datetime.timedelta(hours = 3)
        heure_fin_dis = heure_deb_dis + datetime.timedelta(minutes = tps_ch_min)
        
        for k in range(nb_min) :
            time.append(time[-1] + datetime.timedelta(minutes = 1))
        
        PAC = [0 for k in time]
        
        for k in range(len(PAC)):
            if time[k] > heure_deb_ch and time[k] < heure_fin_ch :
                PAC[k] = p_ch
            elif time[k] > heure_deb_dis and time[k] < heure_fin_dis :
                PAC[k] = p_dis    
        
        self.df["date"] = time
        self.df["PAC"] = PAC
        
        return
        
        
        
        
    
    def calcul_soc(self, type_mod, nb_mod, nb_rack, dt):
        
        soc_ini = 0
        self.type_module(type_mod)
        cap = self.e_mod * nb_mod * nb_rack
        
        E_batt = cap * soc_ini
        SOC = [soc_ini]
        
        for k in self.df.PAC :
            
            E_batt = E_batt - (dt * k)/3600
            SOC.append((E_batt / cap)*100)
        
        SOC.pop()    
        self.df['SOC'] = SOC
        
        
        return 
    
    def modele_U(self, nb_mod, x) :
        
        return (-0.0000058415*x**4 + 0.0012711225*x**3 - 0.0879843643*x**2 + 3.2800731870*x + 679.7518292357)*(nb_mod/14)
     
    def cons_U(self, nb_mod) :
        
        U = []
        for k in self.df.SOC :
            U.append(self.modele_U(nb_mod, k))
         
        self.df['U'] = U   
        
        return 
    
    def cons_I(self) :
        I = []
        for k in range(len(self.df.U)) :
            I.append((self.df.PAC[k]*1000)/self.df.U[k])
        self.df["I"] = I
    
    
        
    
    def type_module(self, type_mod):
        
        if type_mod == "JH4-3P" :
            self.r_mod = 0.0157
            self.e_mod = 11.15
        
        if type_mod == "JH4-4P" :
            self.r_mod = 0.0117
            self.e_mod = 14.85
        
        if type_mod == "JH4-2P" :
            self.r_mod = 0.0234
            self.e_mod = 7.425
    
    
        
            
    
    def heat_gen(self, nb_mod, type_mod) :
        self.type_module(type_mod)
        pth = []
        
        for k in self.df.I :
            pth.append(self.r_mod * k ** 2)
        
        self.df["pth"] = pth
        
    
    def conditions_ext(self, path) :
        
        df_cond = pd.read_excel(path) 
        self.df = pd.merge_asof(self.df, df_cond, on = 'date', direction = "nearest")
    
    
    def bilan_thermique(self, h, mass, nb_mod, nb_rack,
                        set_min_c, set_max_c, set_min_f, set_max_f,
                        Pclim, Pchal):
        
        Te = [20, 20]
        Tr = [23, 23]
        Tw = [(self.df.Text[0] + Te[0])/2, (self.df.Text[0] + Te[0])/2 ]
        cpe = 7300 * mass
        cpr = 65000 * nb_mod
        cpw = 840 * (mass * 1000)
        clim = [0]
        chal = [0]
        coef_fan = 9 * nb_mod
        coef_dis = []
        dt = 60
        fan = [0]
        Pclim = - Pclim * 2.4 * 1000
        Pchal = Pchal * 1000
        Pfan = 14 * nb_mod * nb_rack
        cop = 2.7
        conso_aux = [0 for k in range(len(self.df.index))]
        
        for k in range (len(self.df.index)) :
            
                
            if self.df.pth[k] > 15 :
                coef_dis.append(1 * nb_mod)
            else :
                coef_dis.append(0)
                    
            if Tr[-1] > 25 :
                fan.append(1)
            else :
                fan.append(0)
            
            
            if Te[-1] > set_max_f :
                clim.append(1)
            
            elif clim[-1] == 1 and Te[-1] > Te[-2] :
                clim.append(1)

            elif Te[-1] < set_min_f :
                clim.append(0)
            
            elif Te[-1] < Te[-2] and clim[-1] == 1 :
                clim.append(1)
            
            else : clim.append(0)
            
            
            if Te[-1] < set_min_c :
                chal.append(1)
            
            elif Te[-1] > set_max_c :
                chal.append(0)
            
            elif Te[-1] > Te[-2] and chal[-1] == 1 :
                chal.append(1)
            
            else : chal.append(0)
            
            if clim[-1] == 1:
                conso_aux[k] += abs((Pclim/cop) * 0.001)
            
            if chal[-1] == 1:
                conso_aux[k] += Pchal * 0.001
            
            if fan[-1] == 1:
                conso_aux[k] += Pfan * 0.001
        
            Te.append(Te[-1] + (dt/cpe)* (2*h * (Tw[-1] - Te[-1]) +
                                         nb_rack * (coef_dis[-1] + fan[-1] * coef_fan) * (Tr[-1] - Te[-1] ) +
                                         clim[-1] * Pclim +
                                         chal[-1] * Pchal ))
            
            Tr.append(Tr[-1] + (dt/cpr)* (self.df.pth[k] +
                                         (coef_dis[-1] + fan[-1] * coef_fan) * (Te[-1] - Tr[-1] )))
            
            Tw.append(Tw[-1] + (dt/cpw)* (Te[-1] + self.df.Text[k] - 2*Tw[-1]))
            
            
        Te.pop(), Te.pop()
        Tr.pop(), Tr.pop()
        Tw.pop(), Tw.pop()
        clim.pop(),chal.pop(),fan.pop()
        self.df["Te"] = Te
        self.df["Tr"] = Tr
        self.df["Tw"] = Tw
        self.df["conso_aux"] = conso_aux

        return
    
        
    
    def trace(self):
        color = ["red", "blue", "green", "orange", "red",
                  "blue", "green", "orange", "red", "blue",
                  "green", "orange", "red", "blue"]
        graph = []
        tools = []
        col = self.df.columns
        source = ColumnDataSource(self.df)

        for k in range(len(col)):
            if col[k] != "date" :    
                
                p = figure(x_axis_type = "datetime",
                           title = col[k], x_axis_label = "date" , y_axis_label = col[k],
                           tools = tools)
                p.line("date", col[k], line_width = 2, source = source,
                       color = color[k], alpha = 0.6)
                band = Band(base="date", upper=col[k], source=source, level='underlay',
                            fill_alpha=0.2, fill_color='#FF5588')

                p.add_layout(band)
                p.sizing_mode = "stretch_both"
                p.background_fill_alpha = 0.0
                p.border_fill_alpha = 0.0
                p.title.align = "center"
                p.add_tools(HoverTool(), BoxZoomTool(),PanTool(), ResetTool())

                graph.append(p)
            
        for p in range(1,len(graph)):
            graph[p].x_range = graph[p-1].x_range
        
        self.graph = graph

        return

    
    
    def bokeh_template(self):    
        script, div = components(self.plots)
        self.script = script
        self.div = div

        return

    def set_title(self):

        col = self.df.columns
        col = [k for k in col]
        col.remove("date")

        plot = {}
        for k in range(len(self.graph)):
            plot[col[k]] = self.graph[k]
        self.plots = plot

        change_title(self.plots, "PAC", "Puissance AC qui transite dans les racks")
        change_title(self.plots, "SOC", "Etat de charge de la batterie (SoC)")
        change_title(self.plots, "U", "Tension aux bornes du pack batterie")
        change_title(self.plots, "I", "Courant total traversant les racks ")
        change_title(self.plots, "pth", "Puissance thermique générée par un rack")
        change_title(self.plots, "Text", "Température de l'air extérieur")
        change_title(self.plots, "Irr", "Irradiation solaire")
        change_title(self.plots, "Te", "Température de l'air à l'intérieur du shelter")
        change_title(self.plots, "Tr", "Température des modules")
        change_title(self.plots, "Tw", "Température des murs")
        change_title(self.plots, "conso_aux", "Consommations auxiliaires")








        
        
                
            
        
        
        
        
        
        
        
        

