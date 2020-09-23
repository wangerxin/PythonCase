import sys
import os

# 即ls
file_list = os.listdir("/tmp")

# 脚本路径
# 打印文件的完整父路径: /home/dev/wex/project/PythonCase/sys_case
print(sys.path[0])

# 脚本参数：python sys_demo.py 2020-01-01
# 打印文件名:sys_demo.py
print(sys.argv[0])
# 打印程序的第一个参数:2020-01-01
print(sys.argv[1])

# 执行命令,获取标准输出
cmd="cd /home/dev/wex/project/PythonCase/sys_case;ls"
with os.popen(cmd) as stdout:
    warnings = stdout.readlines()
    print(''.join(warnings))
    fail = [warning for warning in warnings if warning.startswith('FAILED:')]
    if fail:
        print(fail)
        sys.exit(1)



