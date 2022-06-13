import zmq
import struct
import time


class CarData:
    def __init__(self):
        self.id = 0
        self.lane = 0
        self.speed = 0
        self.position = 0
        self.range = []
        self.type = 0
        self.plate = '鄂A1V21A       '
        self.edge = 0
        self.direction = 0


class FrameData:
    def __init__(self):
        self.sn = 0
        self.ip = [192, 168, 1, 100]
        self.timestamp = 0
        self.num = 0
        self.CarData = []


class MessageSubscriber:
    def __init__(self, ip='127.0.0.1', port='8030'):
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
            sn = struct.unpack_from("I", message[0:4])[0]
            timestamp, num = struct.unpack_from('QI', message[8:20])
            file_handle = open('dcLog.txt', mode='a')
            data_time = time.localtime(timestamp / 1000)
            str_time = time.strftime("%Y-%m-%d %H:%M:%S", data_time)
            all_log = f"{str_time} 车子数量:{num} \n"
            for i in range(num):
                offset = i * 44 + 20
                car_id = struct.unpack_from('Q', message[offset:offset + 8])[0]
                car_speed = struct.unpack_from('f', message[offset + 33: offset + 37])[0]
                car_way = struct.unpack_from('b', message[offset + 37: offset+38])[0]
                car_mil = struct.unpack_from('i', message[offset + 38:offset + 42])[0]
                str_log = f"{str_time} ID{car_id} 速度{car_speed}, 车道 {car_way}, 里程{car_mil}"
                # print(str_time, "ID", car_id, "速度", car_speed, "车道", car_way, "里程", car_mil)
                all_log += str_log + "\n"
            print(all_log)
            file_handle.write(all_log)
            file_handle.close()

