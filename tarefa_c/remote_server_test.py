import unittest

from .remote_server import RemoteServer


class RemoteServerTest(unittest.TestCase):
    __remote_server = RemoteServer()

    def remove_file(self, file_name: str):
        self.__remote_server.execute(f'rm {file_name}'.encode())
        output_message = self.__remote_server.execute('ls'.encode())
        self.assertFalse(file_name in output_message)

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

    def test_create_and_delete_new_file(self):
        file_name = 'new_file.txt'
        message = f'touch {file_name}'.encode()
        self.__remote_server.execute(message)
        output_message = self.__remote_server.execute('ls'.encode())
        self.assertTrue(file_name in output_message)
        self.remove_file(file_name)

    def test_create_new_file_with_content(self):
        file_name = 'new_file.txt'
        message = f'echo "content in new file" > {file_name}'.encode()
        self.__remote_server.execute(message)
        output_message = self.__remote_server.execute(f'cat {file_name}'.encode())
        self.assertTrue('content in new file' in output_message)
        self.remove_file(file_name)


if __name__ == '__main__':
    unittest.TextTestRunner().run(RemoteServerTest())
