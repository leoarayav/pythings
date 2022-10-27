'''This module contains all web scrapping using _requests_'''

import requests as rq

class Scrapping:
    '''Class Scrapping, getting URL information, website threads and more.'''
    
    @staticmethod
    def get_web_text(url: str) -> str:
        '''
        This method obtains web text

        Args:
            url (str): Website URL
        
        Returns:
            str: Website text.
        '''
        if url is None:
            pass
        else:
            rq.get(url).text
    
    @staticmethod
    def get_web_headers(url: str) -> str:
        '''
        This method obtains web headers.

        Args:
            url (str): Website URL
        
        Returns:
            str: Website headers.
        '''
        if url is None:
            pass
        else:
            rq.get(url).headers
    
    @staticmethod
    def get_web_cookies(url: str) -> str:
        '''
        This method obtains web text

        Args:
            url (str): Website URL
        
        Returns:
            str: Website cookies.
        '''
        if url is None:
            pass
        else:
            rq.get(url).cookies

    @staticmethod
    def web_excistence(url: str) -> str:
        '''
        This method obtains web excistence.

        Args:
            url (str): Website URL
        
        Returns:
            str: Website excistence message.
        '''
        if rq.get(url).status_code == 404:
            return print("PYTHINGS: This website doesnt exists.")
        else:
            return print("PYTHINGS: Website available.")
    
    @staticmethod
    def get_web_content(url: str) -> bytes:
        '''
        This method obtains web content.

        Args:
            url (str): Website URL
        
        Returns:
            str: Website content.
        '''
        if url is None:
            pass
        else:
            rq.get(url).content