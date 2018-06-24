#N的多次方
#描述
#编写一个程序，计算输入数字N的0次方到5次方结果，并依次输出这6个结果，输出结果间用空格分隔。其中：N是一个整数或浮点数。
#print()函数可以同时输出多个信息，采用如下方法可以使用空格对多个输出结果进行分割：
#print(3.14, 1024, 2048)
#本平台可以通过input()函数获得测试用例输入，请注意，不要在input()中增加提示信息参数，使用如下方式获得测试用例输入并将其输出：
#a = input()
#print(a)
# -*- coding: utf-8 -*-
def chengfang(a):
     b=a**0
     c=a**1
     d=a**2
     e=a**3
     f=a**4
     g=a**5
     print(b,c,d,e,f,g)
a=input()
if a.isdecimal():
    a=int(a)
    chengfang(a)
    #print(b,c,d,e,f,g)
else:
    a=float(a)
    chengfang(a)
    #print(b,c,d,e,f,g)
