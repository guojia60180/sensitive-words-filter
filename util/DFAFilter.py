#Author guo
class DFAFilter():
    '''有穷状态机完成'''

    def __init__(self):
        self.keywords_chains={}
        self.delimit='\x00'

    def add(self,keyword):
        #keyword=keyword.decode('utf-8')
        keyword=keyword.lower()
        chars=keyword.strip()
        if not chars:
            return

        level=self.keywords_chains
        for i in range(len(chars)):
            if chars[i] in level:
                level=level[chars[i]]

            else:
                if not isinstance(level,dict):
                    break

                for j in range(i,len(chars)):
                    level[chars[j]]={}
                    last_level,last_char=level,chars[j]
                    level=level[chars[j]]

                last_level[last_char]={self.delimit:0}
                break

        if i==len(chars)-1:
            level[self.delimit]=0

    def parse(self,path):
        with open(path,encoding='utf-8') as f:
            for keyword in f:
                self.add(keyword.strip())


    def filter(self,message,repele='*'):
        #message.decode('utf-8')

        message=message.lower()
        ret=[]

        start=0
        while start<len(message):
            level=self.keywords_chains
            step_ins=0
            for char in message[start:]:
                if char in level:
                    step_ins+=1
                    if self.delimit not in level[char]:
                        level=level[char]

                    else:
                        ret.append(repele*step_ins)
                        start+=step_ins-1
                        break

                else:
                    ret.append(message[start])
                start+=1


            return ''.join(ret)