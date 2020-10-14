import unittest

from .time_server import TimeServer


class TimeServerTest(unittest.TestCase):

    def test_receive_correct_message_from_client(self):
        server = TimeServer()
        message = 'data'.encode()
        output_message = server.response(message)
        self.assertFalse('only command supported is data' in output_message.decode())

        return

    def test_receive_wrong_message_from_client(self):
        server = TimeServer()
        message = 'please fail'.encode()
        output_message = server.response(message)
        self.assertTrue('only command supported is data' in output_message.decode())


if __name__ == '__main__':
    unittest.TextTestRunner().run(TimeServerTest())
