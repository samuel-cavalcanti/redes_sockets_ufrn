import unittest

from file_server import FileServer


class FileServerTest(unittest.TestCase):

    def test_no_file_request_from_client(self):
        file_server = FileServer()
        possible_command_in_bytes = 'obter arquivo.txt'.encode()

        content = file_server.execute_command(possible_command_in_bytes)

        self.assertTrue('No such file or directory' in content)

    pass

    def test_server_has_file(self):
        file_server = FileServer()

        possible_command_in_bytes = 'obter file.txt'.encode()

        content = file_server.execute_command(possible_command_in_bytes)

        self.assertTrue('content' in content)

    def test_wrong_command_request(self):
        file_server = FileServer()

        possible_command_in_bytes = 'atualizar file.txt'.encode()

        content = file_server.execute_command(possible_command_in_bytes)

        self.assertTrue('Not command support' in content)


if __name__ == '__main__':
    unittest.TextTestRunner().run(FileServerTest())
