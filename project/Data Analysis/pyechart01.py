from pyecharts import options as opts
from pyecharts.charts import Bar
x = [*range(11)]
y1 = [*range(10,21)]
y2 = [*range(20,31)]


def theme_default() -> Bar:
    c = (
        Bar()
        # 等价于 Bar(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
        .add_xaxis(x)
        .add_yaxis("商家A", y1)
        .add_yaxis("商家B", y2)
        .add_yaxis("商家C", y1)
        .add_yaxis("商家D", y2)
        .set_global_opts(title_opts=opts.TitleOpts("Theme-default"))
    )
    return c

c =theme_default()
c.render()