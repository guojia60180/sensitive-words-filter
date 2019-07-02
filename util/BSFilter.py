#Author guo
import re
from collections import defaultdict
class BSFilter():
    '''
    为了缩短次数
    利用后向排序映射减少时间
    '''
    def __init__(self):
        self.keywords=[]
        self.keywordset=set([])
        self.bsdict=defaultdict(set)
        self.pattern=re.compile(r'^[0-9a-zA-Z]+$')

    def add(self,keyword):
        #keyword=keyword.decode('utf-8')
        keyword=keyword.lower()

        if keyword not in self.keywordset:
            self.keywords.append(keyword)
            self.keywordset.add(keyword)
            index=len(self.keywords)-1
            for word in keyword.split():
                if self.pattern.search(word):
                    self.bsdict[word].add(index)
                else:
                    for char in word:
                        self.bsdict[char].add(index)

    def parse(self,path):
        with open(path,'r',encoding='utf-8')as f:
            for keyword in f:
                self.add(keyword.strip())


    def filter(self,message,repele='*'):
        #message=message.decode('utf-8')

        message=message.lower()

        for word in message.split():
            if self.pattern.search(word):
                for index in self.bsdict[word]:
                    message=message.replace(self.keywords[index],repele)

            else:
                for char in word:
                    for index in self.bsdict[char]:
                        message=message.replace(self.keywords[index],repele)

        return message