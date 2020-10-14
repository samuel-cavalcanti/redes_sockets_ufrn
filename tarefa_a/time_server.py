import time


class TimeServer:
    __command = 'data'

    def response(self, message: bytes) -> bytes:
        command = message.decode()
        if command == self.__command:
            return time.ctime().encode()
        else:
            return f'only command supported is {self.__command}'.encode()
