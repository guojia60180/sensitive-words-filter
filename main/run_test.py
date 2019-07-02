#Author guo

from collections import defaultdict
import os
import sys
import time
import re

from util.BSFilter import BSFilter
from util.SimpleFilter import SimpleFilter
from util.DFAFilter import DFAFilter


def test_first_char():
    f=DFAFilter()
    f.add('年')
    print(f.filter('1989年asd','*'))

if __name__=='__main__':
    log_path='../data/keywords.txt'
    #f=BSFilter()
    f=DFAFilter()
    f.parse(log_path)

    t=time.time()
    for i in range(100):
        print(f.filter('习近平', "*"))

    print(time.time()-t,'时间')




'''
'活' (113890688) = {dict} {'动': {'管': {'理': {'员': {'\x00': 0}}}}}
 __len__ = {int} 1
 '动' (113891088) = {dict} {'管': {'理': {'员': {'\x00': 0}}}}
  __len__ = {int} 1
  '管' (113890288) = {dict} {'理': {'员': {'\x00': 0}}}
   __len__ = {int} 1
   '理' (113891008) = {dict} {'员': {'\x00': 0}}
    __len__ = {int} 1
    '员' (113891168) = {dict} {'\x00': 0}
     __len__ = {int} 1
     '\x00' (20939640) = {int} 0
'''






