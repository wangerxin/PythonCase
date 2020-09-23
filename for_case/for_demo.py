
# 生成器: 边遍历，边计算
result1 = [i * 10 for i in range(1,10) if i >= 5] # [50, 60, 70, 80, 90]
result2 = {score: True for score in range(1,5)}   # {1: True, 2: True, 3: True, 4: True}

def test(arg):
    print(type(arg))

