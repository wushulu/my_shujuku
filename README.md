# my_shujuku
数据库的基本操作
## 数据库安装
    1、解压sqlite3的两个压缩包将里面的文件放置在同一个文件夹下<br>
    2、计算机新建添加sqlite3 Path 的环境变量路径(sqlite3的文件路径)
## 数据库的基本操作
    1、创建数据库：sqlite3  shujuku.db
    2、创建表格：
        create table  mytesttable(
            ID INT PRIMARY NOT NULL,
            AGE INT NOT NULL
        );
    3、查看所有表格名称指令 .tables
    4、查看某个表格定义信息.schema mytesttable
    5、sqlite3 的数据类型 常用：
        INT 整型、、、
        INT
        INTEGER
        TINYINT
        SMALLINT
        MEDIUMINT
        BIGINT
        UNSIGNED BIG INT
        INT2
        INT8
    
        、 TEXT 字符串、、、、
        CHARACTER(20)
        VARCHAR(255)
        VARYING CHARACTER(255)
        NCHAR(55)
        NATIVE CHARACTER(70)
        NVARCHAR(100)
        TEXT
        CLOB
        
        、REAL 浮点型、、、
        REAL
        DOUBLE
        DOUBLE PRECISION
        FLOAT
    6、常用术语：表(table)、字段(column，列，属性)、记录(row，record)
    7、关键字：select、insert、update、delete、from、creat、where、desc、order、by、group、table、      alter、  view、index等，数据库中不能使用关键字命名表和字段
    8、特点：不区分大小写，每条语句后加";"结尾
    9、字段约束：
        not null：字段的值不能为空。
        unique：字段的值必需唯一。
        default：指定字段的默认值。
        primary key：主键，用来唯一的标识某条记录，相当于记录的身份证。主键可以是一个或多个字段，应由计算机自动生成和管理。主键字段默认包含了not null和unique两个约束。
        autoincrement：当主键是integer类型时，应该增加autoincrement约束，能实现主键值的自动增长。        
    9、写表格：insert into mytesttable(ID ,AGE)
              values(1,20);
              values(2.24)
        修改表中的数据 ⟹ update：update 表名 set 字段1 ＝ 字段1的值，字段2 ＝ 字段2的值，。。。;
        全部修改：update mytesttable set ID  =1, AGE = 20;
        修改部分：update mytesttable set age = 50 wherw ID ==1;#中间没有逗号
        删除表中的数据 ⟹ delete：delete from 表名；delete from 表名 where 字段 ＝ 字段值
        delete from mytesttable ;删除所有数据
        delete from mytesttable where age = 50;
        排序：select *from mytesttable order by ID ASC;升序 DESC(降序)
    10、显示表格内容：select *from mytesttable;
        计算表格字段行数：select count(*) from mytesttable;

    11、逻辑运算：
        运算符	描述
        AND	AND 运算符允许在一个 SQL 语句的 WHERE 子句中的多个条件的存在。
        BETWEEN	BETWEEN 运算符用于在给定最小值和最大值范围内的一系列值中搜索值。
        EXISTS	EXISTS 运算符用于在满足一定条件的指定表中搜索行的存在。
        IN	IN 运算符用于把某个值与一系列指定列表的值进行比较。
        NOT IN	IN 运算符的对立面，用于把某个值与不在一系列指定列表的值进行比较。
        LIKE	LIKE 运算符用于把某个值与使用通配符运算符的相似值进行比较。
        GLOB	GLOB 运算符用于把某个值与使用通配符运算符的相似值进行比较。GLOB 与 LIKE 不同之处在于，它是大小写敏感的。
        NOT	NOT 运算符是所用的逻辑运算符的对立面。比如 NOT EXISTS、NOT BETWEEN、NOT IN，等等。它是否定运算符。
        OR	OR 运算符用于结合一个 SQL 语句的 WHERE 子句中的多个条件。
        IS NULL	NULL 运算符用于把某个值与 NULL 值进行比较。
        IS	IS 运算符与 = 相似。
        IS NOT	IS NOT 运算符与 != 相似。
        ||	连接两个不同的字符串，得到一个新的字符串。
        UNIQUE	UNIQUE 运算符搜索指定表中的每一行，确保唯一性（无重复）。