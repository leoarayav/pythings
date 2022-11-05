'''
Main file of @pythings.

# How to use?
Just execute this file and take a look of each components
handled by pythings, like operations, scrapping etc

# Issues report or bug report
You can report any bug opening an github issue in this repository.

NOTE: Each method can be updated.
'''

from pythings.operations import Operations
from pythings.convertions import Convertions
from pythings.scrapping import Scrapping

'''Definition of objects'''
operation = Operations()
convertion = Convertions()
scrapping = Scrapping()

'''Operation availables methods with examples'''
operation.average([1, 4, 6, 6, 4, 7])
operation.addition(1, 6, 3, 2)
operation.substract(13, 34)
operation.divide(18, 3)
operation.multiply(2, 2, 5)
operation.power(5, 5)

'''Convertion availables methods with examples'''
convertion.int_hex_upper(2435)
convertion.int_hex_lower(1335)
convertion.ascii_to_binary("act")
convertion.text_to_binary("hello everyone")