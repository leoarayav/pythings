'''This file contains texts constants'''

from time import sleep
from colorama import Fore, Style, init

class Text:
    '''Class Text of pythings.constants, contains all texts design :-)'''

    @staticmethod
    def message(color: str, message: str) -> str:
        '''
        This method returns console message
        
        Args:
            color (str): Message color.
            message (str): Message text.
        
        Returns:
            str: Our printed message.
        '''
        return print(color + message)
    
    @staticmethod
    def alert(color: str, message: str, alertType: str = "?") -> str:
        '''
        This method returns console alert.
        
        Args:
            color (str): Alert message color.
            message (str): Alert message text.
            alertType (str): Alert type.
        
        Returns:
            str: Our printed alert.
        '''
        return print(color + f"{alertType} | {message}")
    
    @staticmethod
    def loading(message: str, secs: float | int) -> str:
        '''
        This method returns console loading animation.
        
        Args:
            message (str): Loading message text.
            secs (float or int): Time to wait.

        Returns:
            str: Our printed loading animation.
        '''
        try:
            print(f"LOADING | {message}")
            sleep(secs)
        except Exception as err:
            print(err)

class Special:
    '''
    Special class constains specials outputs and messaging.
    
    Script idea by: @manucabral -> https://www.github.com/manucabral

    Deployed by: @leoarayav -> https://www.github.com/leoarayav
    '''
    PYTHINGS_COLORS = {
        '<red>': Fore.RED,
        '<blue>': Fore.BLUE,
        '<green>': Fore.GREEN,
        '<black>': Fore.BLACK,
        '<cyan>': Fore.CYAN,
        '<yellow>': Fore.YELLOW
    }

    def __init__(self, output: str, parse: str = True) -> None:
        '''Initialize special texts instances'''
        if parse: output = self.__parse(output)
        self.messagec(output)
    
    @staticmethod
    def init() -> None:
        '''Initialize colorama'''
        return init()
    
    def __parse(self, text: str) -> str:
        '''Parse a string and replace the color-codes with colorama codes'''
        for k, v in self.PYTHINGS_COLORS.items():
            text = text.replace(k, v)
        return text
    
    def messagec(self, text: str) -> None:
        '''Print a string using special attributes'''
        print(Style.RESET_ALL + text)