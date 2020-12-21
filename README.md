# brute_xss
xss暴力破解脚本


usage: brute_xss.py [-h] [-p PARAMS] [-d DICT] [-t THREADS] url

positional arguments:
  url                   待测试xss的url

optional arguments:
  -h, --help            show this help message and exit
  -p PARAMS, --params PARAMS
                        GET参数
  -d DICT, --dict DICT  测试xss的字典(默认xss.txt)
  -t THREADS, --threads THREADS
                        线程数(默认3)
