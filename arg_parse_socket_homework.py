import argparse


class ArgParseSocketHomework:

    def __init__(self, start_server_callback, start_client_callback, description='Dever de casa socket'):
        self.__start_server_callback = start_server_callback
        self.__start_client_callback = start_client_callback
        self.__parser = self.__create_parser(description)

    @staticmethod
    def __create_parser(description: str) -> argparse.ArgumentParser:

        parser = argparse.ArgumentParser(description=description)
        parser.add_argument('-server', dest='server', action='store_const',
                            const=True, default=False,
                            help='caso queria iniciar o server utilize -server')

        parser.add_argument('-client', dest='client', action='store_const',
                            const=True, default=False,
                            help='caso queria iniciar o cliente utilzie -client')

        return parser

    def parse(self):
        args = self.__parser.parse_args()
        self.__select_option(args.server, args.client)

    def __select_option(self, server_option: bool, client_option: bool):

        if server_option and client_option:
            raise Exception('Só pode iniciar o server ou o client')
        elif server_option is True:
            self.__start_server_callback()
        elif client_option is True:
            self.__start_client_callback()
        else:
            self.__parser.print_help()
