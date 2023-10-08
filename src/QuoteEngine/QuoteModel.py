from abc import ABC, abstractmethod


class QuoteModel(ABC):
    def __init__(self, body = '', author = ''):
        if body:
            self.body = body
        if author:
            self.author = author

    def __str__(self):
        print(f'{self.body} - {self.author}')
