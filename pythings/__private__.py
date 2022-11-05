'''This module contains all private issues neccesary that @pythings use'''

class Private:
    '''
    Class Private contains all private issues for pythings.
    '''

    '''Methods availables'''
    __methods = {
        'convertions',
        'operations',
        'scrapping'
    }

    def __init__(self) -> None:
        self.__path = ".\pythings"

    def __check_method(self, _method: str) -> bool:
        '''This function check if method is correct or not.'''
        if _method in self.__methods:
            return print('PYTHINGS: This method is working correctly.')
        else:
            return print('PYTHINGS: This method is not working or do not exists.')
    
    def __show_method_doc(self) -> str:
        '''This function show method's documentation'''
        return __doc__