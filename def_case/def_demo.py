
"""
结论: 函数的参数没有类型，但需要知道它的可操作性，例如参数可以被迭代，可以被切片。
"""
def test_arg_stype(arg):
    print(type(arg))
    print(arg[0])

test_arg_stype(10)   # int,arg[0]报错
test_arg_stype("10") # str,1