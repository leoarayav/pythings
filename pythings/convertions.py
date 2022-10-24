'''This module contains all convertions of py@things'''

from matplotlib.pyplot import text


class Convertions:
    '''Class Convertions, this includes simple and advanced convertions.'''

    __binaryText = ""
    __separator = " "

    def __init__(self) -> None:
        pass

    def ascii_to_binary(self, letter: str) -> int:
        '''
        Converts ASCII to binary

        Params:
            letter (str): Each char/letter to convert.
        
        Returns:
            int: Binary convertion.
        '''
        val = ord(letter)
        return "{0:08b}".format(val)

    def text_to_binary(self, text: str) -> int:
        '''
        Converts text to binary.

        Params:
            text (str): Text to convert.
        
        Returns:
            int: Binary convertion.
        '''
        cont = 0
        for let in text:
            self.__binaryText += self.ascii_to_binary(let)
            if cont + 1 < len(text):
                self.__binaryText += self.__separator
            cont += 1
        return print(self.__binaryText)
    
    def int_hex_upper(self, number: int) -> hex:
        '''
        Converts integer value to hexadecimal upper-case format.

        Params:
            number (int): Integer to convert.
        
        Returns:
            hex: Hexadecimal convertion.
        '''
        return print(format(number, 'X'))
    
    def int_hex_lower(self, number: int) -> hex:
        '''
        Converts integer value to hexadecimal lower-case format.

        Params:
            number (int): Integer to convert.
        
        Returns:
            hex: Hexadecimal convertion.
        '''
        return print(format(number, 'x'))

Convertions().text_to_binary("foo")
