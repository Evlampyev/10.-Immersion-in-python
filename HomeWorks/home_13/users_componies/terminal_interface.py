from .interface import Interface


class TerminalInterface(Interface):
    def print_data(self, data):
        print(data)

    def input_data(self, data):
        return input(data)
