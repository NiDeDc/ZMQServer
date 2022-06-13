import zmq
import struct
import numpy as np


class MessageSubscriber:
    def __init__(self, ip='127.0.0.1', port='8010'):
        self.context = zmq.Context()
        self.subscriber = self.context.socket(zmq.SUB)
        self.address = "tcp://{}:{}".format(ip, port)
        self.subscriber.connect(self.address)
        self.subscriber.setsockopt(zmq.SUBSCRIBE, "".encode('utf-8'))

    def ReceiveThread(self):
        while True:
            message = self.subscriber.recv()
            # print("response: %s" % message)
            # print(message)
            prefix_len = 2
            prefix = message[0:prefix_len].decode()
            print(prefix)
            if prefix == "WH":
                head_length = struct.calcsize('Q4h')
                shell = message[prefix_len:prefix_len+head_length]
                datatime, datatype, dev, ch, colum = struct.unpack_from('Q4h', shell, 0)
                data = np.frombuffer(message[prefix_len+head_length:], dtype=np.float32)
                sample = len(data) // colum
                data = data.reshape(sample, colum)
                # timeStamp = datetime.datetime.fromtimestamp(datatime / 1000)
                # time_string = timeStamp.strftime("%Y-%m-%d %H:%M:%S.%f")
                t_data = [dev, ch, datatime, data]
                cnt_array = np.where(data,(0, 0))
                print("当前包0元素个数", np.sum(cnt_array))
            #     pass
