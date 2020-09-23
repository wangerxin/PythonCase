
#格式化
info="我叫{name},今年{age}岁。".format(name="张三",age=18)
info="我叫{name},今年{age}岁。".format(**{"name" : "张三","age" : 18})

#使用指定分隔符拼接序列中的元素
print("-".join(["a","b","c"])) # a-b-c



