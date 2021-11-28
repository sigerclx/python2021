# 导入绘图工具
from pyecharts import options as opts
from pyecharts.charts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子" , "高跟鞋" , "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = (
        Bar()
        .add_xaxis(attr)
        .add_yaxis("商家A", v1)
        .add_yaxis("商家B", v2)
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
# 在notebook中输出
bar.render_notebook()
