import unittest

from .remote_server import RemoteServer


class RemoteServerTest(unittest.TestCase):
    __remote_server = RemoteServer()

    def test_request_have_no_command(self):
        message = ''.encode()
        output_message = self.__remote_server.execute(message)
        self.assertTrue('error: must type any command' in output_message)

    def test_request_have_command_but_wrong_args(self):
        message = 'ls dsadawds'.encode()
        output_message = self.__remote_server.execute(message)
        self.assertTrue('No such file or directory' in output_message)

    def test_request_have_command_and_correct_args(self):
        message = 'ls .'.encode()
        output_message = self.__remote_server.execute(message)
        self.assertFalse('error: must type any command' in output_message)

    def test_request_have_command_without_args(self):
        message = 'ls'.encode()
        output_message = self.__remote_server.execute(message)
        self.assertFalse('No such file or directory' in output_message)


if __name__ == '__main__':
    unittest.TextTestRunner().run(RemoteServerTest())
