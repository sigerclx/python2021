# Flask wtforms简介
## 字段介绍
- wtforms中的Field类主要用于数据验证和字段渲染(生成html)，以下是比较常见的字段：

- StringField    字符串字段，生成input要求字符串
- PasswordField　　密码字段，自动将输入转化为小黑点
- DateField　　日期字段，格式要求为datetime.date一样
- IntergerField　　整型字段，格式要求是整数
- FloatField　　文本字段，值是浮点数
- BooleanField　　复选框，值为True或者False
- RadioField　　一组单选框
- SelectField　　下拉列表，需要注意一下的是choices参数确定了下拉选项，但是和HTML中的<select> 标签一样。
- MultipleSelectField　　多选字段，可选多个值的下拉列表
...

## 字段参数:

- label：字段别名，在页面中可以通过字段.label展示；
- validators：验证规则列表；
- filters：过氯器列表，用于对提交数据进行过滤；
- description：描述信息，通常用于生成帮助信息；
- id：表示在form类定义时候字段的位置，通常你不需要定义它，默认会按照定义的先后顺序排序。
- default：默认值
- widget：html插件，通过该插件可以覆盖默认的插件，更多通过用户自定义；
- render_kw：自定义html属性；
- choices：复选类型的选项 ;