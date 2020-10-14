import subprocess


class RemoteServer:

    def execute(self, command: bytes) -> str:
        if self.have_no_command(command):
            return 'error: must type any command'
        else:
            return self.__run_command_in_sub_process(command)

    @staticmethod
    def have_no_command(client_command: bytes):
        return len(client_command) == 0

    def __run_command_in_sub_process(self, command: bytes) -> str:
        try:
            return self.__execute_command(command)
        except Exception as  command_error:
            return f"Exception: {command_error}!"

    @staticmethod
    def __execute_command(command: bytes) -> str:
        command_and_args = command.decode().split(' ')

        completed_sub_process = subprocess.run(
            command_and_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return f"{completed_sub_process.stdout.decode()} \n {completed_sub_process.stderr.decode()}"
