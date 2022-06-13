# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import threading
# import ZMQServer
from ZMQSubscriber_trackdeal import MessageSubscriber
import time


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    msg = MessageSubscriber(ip="100.65.23.241", port="8030")
    # msg = MessageSubscriber()
    t = threading.Thread(target=msg.ReceiveThread, args=())
    t.setDaemon(True)
    t.start()
    while True:
        time.sleep(0.5)
        # data = ZMQServer.Dequeue()
        # if data is None:
        #     print('no data')
        # else:
        #     print(data[0:7])
        # print(ZMQServer.q.qsize())

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
