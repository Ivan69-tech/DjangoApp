from random import randint
from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.models import Band, ColumnDataSource, HoverTool, BoxZoomTool, PanTool, ResetTool
from bokeh.embed import components
from bokeh.models.annotations import Title


def random_data(nbr_data):
    Y = [randint(1,100) for k in range(nbr_data)]
    X = [k for k in range(nbr_data)]

    source = ColumnDataSource(dict(X=X, Y=Y))

    tools = [HoverTool(), BoxZoomTool(),PanTool(), ResetTool()]
    p = figure(title = "Random graph", x_axis_label = "X" , y_axis_label = "Y",
               tools = tools)


    p.line("X", "Y", line_width = 2, source = source, color = "#770550")
    band = Band(base="X", upper="Y", source=source, level='underlay',
                fill_alpha=0.2, fill_color='#FF5588')

    p.add_layout(band)
    p.sizing_mode = "stretch_both"
    p.background_fill_alpha = 0.0
    p.border_fill_alpha = 0.0
    p.title.align = "center"

    script, div = components(p)

    return {"script" : script,
            "div": div,
            "X" : X,
            "Y": Y}

    
    
