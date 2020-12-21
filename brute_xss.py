#!python3
import requests
import argparse
import threading
import queue

class Cheak_Xss(object):
    def __init__(self):
        self.q=queue.Queue()
        parse=argparse.ArgumentParser()
        parse.add_argument('url', help='待测试xss的url')
        parse.add_argument('-p','--params',help='GET参数')  #格式： 参数,参数,参数
        parse.add_argument('-d','--dict',help='测试xss的字典',default='xss.txt')
        parse.add_argument('-t','--threads',help='线程数',default=3,type=int)
        args=parse.parse_args()
        self.url=args.url
        if args.params:
            self.params=args.params.split(',')
        self.dict=args.dict
        self.threads=args.threads

    def auto_check_xss(self):
        '''
        自动检测xss
        :return:
        '''
        try:

            flag=False
            xss=self.q.get()
            for param in self.params:
                params = {param:xss}
                req=requests.get(self.url,params=params)
                if xss in req.text:
                    print('{} find xss\npayload:{}'.format(self.url,xss))
                    flag=True
                    break

        except Exception as e:
            print(e)

    def main(self):
        with open(self.dict, 'r', encoding='utf-8') as fp:
            xss_list = fp.readlines()
        for xss in xss_list:
            self.q.put(xss.strip())
        for i in range(self.threads):
            sub_thread=threading.Thread(target=self.auto_check_xss)
            sub_thread.start()
            sub_thread.join()


if __name__ == '__main__':
    c=Cheak_Xss()
    c.main()



