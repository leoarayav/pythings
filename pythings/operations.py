'''This module contains all operations development.'''

class Operations:
    
    @staticmethod
    def addition(*nums: int) -> int:
        '''
        This method allows you sum all numbers that you want.

        Args:
            *nums (*args & int): Numbers to additionate.

        Returns:
            int: Our numbers result. 
        '''
        v = 0
        for n in nums:
            v += n
        return print(v)

    @staticmethod
    def substract(x: int, y: int) -> int:
        '''
        This method allows you substract two numbers

        Args:
            x (int): First number.
            y (int): Second number.
        
        Returns:
            int: Our substraction result.
        '''
        return print(x - y)
    
    @staticmethod
    def multiply(*nums: int) -> int:
        '''
        This method allows you to multiply numbers.

        Args:
            *nums (*args & int): Numbers to multiply.
        
        Returns:
            int: Our multiplication result.
        '''
        v = 0
        for num in nums:
            v *= num
        print(v)
    
    @staticmethod
    def divide(a: int, b: int) -> int:
        '''
        This method allows you to divide two numbers.

        Args:
            a (int): Your first number.
            b (int): Your second number.
        
        Returns:
            int: Our divition result.
        '''
        return a / b
    
    @staticmethod
    def average(numbers: list[int]) -> float:
        '''
        This method allows you average all numbers in a list.

        Args:
            numbers (list[int]): All numbers stored in our list.
        
        Returns:
            float: Our average result.
        '''
        avg = sum(numbers) / len(numbers)
        return print(avg)
    
    @staticmethod
    def power(a: int, b: int) -> int:
        '''
        This method allows you power two numbers.

        Args:
            a (int): Our first number.
            b (int): Our second number.
        
        Returns:
            int: Our power result.
        '''
        return a ** b | pow(a, b)