# brute_xss
xss暴力破解脚本

## 参数
usage: brute_xss.py [-h] [-p PARAMS] [-d DICT] [-t THREADS] url  
  
### positional arguments:  
  - url                   待测试xss的url  
  
### optional arguments:   
  - -h, --help            show this help message and exit  
  - -p PARAMS, --params PARAMS   GET参数  
  - -d DICT, --dict DICT  测试xss的字典(默认xss.txt)  
  - -t THREADS, --threads THREADS   线程数(默认3)

## 使用方法
安装python依赖库
```python
pip install -r requirements.txt
```
调用脚本
```python
python brute_xss.py -p GET参数 -d xss字典 -t 线程数 待测试xss的url
```
