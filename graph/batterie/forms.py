from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class BattForm(forms.Form):
    type_mod = forms.CharField(label = 'Type de module', initial= "JH4-3P")
    nb_mod = forms.IntegerField(widget = forms.NumberInput, label = 'Nombre de modules par rack', initial= 14)
    nb_rack = forms.IntegerField(widget = forms.NumberInput, label = 'Nombre de racks', initial= 4)
    c_rate = forms.DecimalField(widget = forms.NumberInput, label = 'C-rate du cycle', initial= 0.3)
    nb_jour = forms.IntegerField(widget = forms.NumberInput, label = 'Nombre de jour de simulation', initial= 1)
    
    
    jour_deb = forms.DateTimeField(widget = forms.DateInput(format='%Y-%m-%d', attrs={'type':'date', 'class':'datepicker'}),
                                   input_formats=('%Y-%m-%d', ), label = 'Premier jour de Simulation', initial= "2019-01-05")
    

    
    h = forms.IntegerField(widget = forms.NumberInput, label = 'Coefficient d\'échange des parois du shelter', initial= 50)
    mass = forms.IntegerField(widget = forms.NumberInput, label = 'Masse du shelter à vide', initial= 30)
    set_min_c = forms.IntegerField(widget = forms.NumberInput, label = 'Setpoint début chauffage', initial= 17)
    set_max_c = forms.IntegerField(widget = forms.NumberInput, label = 'Setpoint fin chauffage', initial= 20)
    set_min_f = forms.IntegerField(widget = forms.NumberInput, label = 'Setpoint fin climatisation ', initial= 21)
    set_max_f = forms.IntegerField(widget = forms.NumberInput, label = 'Setpoint début climatisation', initial= 25)
    Pclim = forms.DecimalField(widget = forms.NumberInput, label = 'Puissance de la climatisation', initial= 6.4)
    Pchal = forms.DecimalField(widget = forms.NumberInput, label = 'Puissance du chauffage', initial= 4.4)