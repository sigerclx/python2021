# SQLAlchemy
### SQLAlchemy常⽤数据类型：
1. Integer：整形，映射到数据库中是int类型。
2. Float：浮点类型，映射到数据库中是float类型。他占据的32位。
3. Double：双精度浮点类型，映射到数据库中是double类型，占据64位。
4. String：可变字符类型，映射到数据库中是varchar类型.
5. Boolean：布尔类型，映射到数据库中的是tinyint类型。
6. DECIMAL：定点类型。是专门为了解决浮点类型精度丢失的问题的。在存储钱相关的字段的时候建议⼤家都使⽤这个数据类型。并且这
个类型使⽤的时候需要传递两个参数，第⼀个参数是⽤来标记这个字段总能能存储多少个数字，第⼆个参数表⽰⼩数点后有多少位。
7. Enum：枚举类型。指定某个字段只能是枚举中指定的⼏个值，不能为其他值。在ORM模型中，使⽤Enum来作为枚举
8. Date：存储时间，只能存储年⽉⽇。映射到数据库中是date类型。在Python代码中，可以使⽤`datetime.date`来指定
9. DateTime：存储时间，可以存储年⽉⽇时分秒毫秒等。映射到数据库中也是datetime类型。在Python代码中，可以使⽤
`datetime.datetime`来指定。⽰例代码如下：
10. Time：存储时间，可以存储时分秒。映射到数据库中也是time类型。在Python代码中，可以使⽤`datetime.time`来⾄此那个。
11. Text：存储长字符串。⼀般可以存储6W多个字符。如果超出了这
--------------------------------------------------------
作者：12万花盼曼资料集
链接：https://wenku.baidu.com/view/44ed7e99bad528ea81c758f5f61fb7360b4c2b95.html
来源：百度文库
