# with优势: io结束后，自动关闭资源
# w覆盖写入，a追加写入，r读取
with open('/home/dev/wex/project/test', 'w') as f:
    f.write("hello word")

with open('/home/dev/wex/project/test', 'r') as f:
    print(f.read())

#序列化与反序列化
import pickle
# 反序列化
object = pickle.load()
