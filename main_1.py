import threading
import ZMQServer
# from ZMQSubscriber import MessageSubscriber
import time


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    t = threading.Thread(target=ZMQServer.ReceiveData, args=())
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
