class FileServer:

    def execute_command(self, command_in_bytes: bytes) -> str:
        load_file_command: str = command_in_bytes.decode()

        return self.__get_content_from_file(load_file_command)

    def __get_content_from_file(self, load_file_command: str) -> str:
        try:
            command, file_name = load_file_command.split(' ')
            return self.__load_file_from_command(command, file_name)
        except Exception as load_file_error:
            return str(load_file_error)

    @staticmethod
    def __load_file_from_command(command: str, file_name: str) -> str:
        if command == 'obter':
            with open(file_name, 'r') as file:
                return file.read()
        else:
            return 'Not command support'
        pass
