#Author guo
from collections import defaultdict

import re

class SimpleFilter():
    '''
    simple for replace keywords
    bad rate to complete access
    '''

    def __init__(self):
        self.keywords=set([])


    def parse(self,path):
        for keyword in open(path,encoding='utf-8'):
            self.keywords.add(keyword.strip().lower())

    def filter(self,message,repele='*'):
        message=message.lower()
        for kword in self.keywords:
            message=message.replace(kword,repele)

        return message
