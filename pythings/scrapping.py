'''This module contains all web scrapping using _requests_'''

import requests as rq

class Scrapping:
    '''Class Scrapping, getting URL information, website threads and more.'''
    
    @staticmethod
    def get_web_text(url: str) -> str:
        if url is None:
            pass
        else:
            rq.get(url).text
    
    @staticmethod
    def get_web_headers(url: str) -> str:
        if url is None:
            pass
        else:
            rq.get(url).headers
    
    @staticmethod
    def get_web_cookies(url: str) -> str:
        if url is None:
            pass
        else:
            rq.get(url).cookies

    @staticmethod
    def web_excistence(url: str) -> str:
        if rq.get(url).status_code == 404:
            return print("PYTHINGS: This website doesnt exists.")
        else:
            return print("PYTHINGS: Website available.")
    
    @staticmethod
    def get_web_content(url: str) -> bytes:
        if url is None:
            pass
        else:
            rq.get(url).content