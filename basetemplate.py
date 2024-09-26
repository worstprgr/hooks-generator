from typing import Callable


class BaseTemplate:
    def __init__(self) -> None:
        self.__levels: list[str] = ['INFO', 'WARNING', 'ERROR']

    def error_message(self, msg: str, log_level: int = 2) -> None:
        """
        Log Levels:  
            0 -> INFO  
            1 -> WARNING  
            2 -> ERROR  
        :param msg: Error/Warning message
        :param log_level: integer, see description
        """
        return f'[{self.__levels[log_level]}]: {msg}'

    def build(self) -> list[str]:
        pass

    @staticmethod
    def add_line_sep(method: Callable) -> list[str]:
        buffer = []
        for line in method:
            buffer.append(line + '\n')
        return buffer

