#coding=utf-8
'''
文件的默认字符集是utf-8
字符集就是翻译官,解析不同的语言用于显示,作用是声明python代码的文本格式是utf-8，python按照utf-8的方式来读取程序。
如果不加这个声明，无论代码中还是注释中有中文都会报错。
为了维护代码的统一性，一般统一设置成utf-8
常见字符集GBK2312
注意一点:coding与=之间不能有空格,否则也会报错

1.直接输出
'''
#直接输出是通过print()函数进行打印
#输出翻滚吧牛宝宝！！！

print("翻滚吧牛宝宝")


'''
2.变量输出
'''
#变量可以理解为容器，容器的值是不固定的，设置什么保存什么
name='python'
print(name)

#变量之间也可以进行操作
a=20
b=30
print(a+b)
a='heygor is '
b='handsome!!! '
print(a+b)

'''
3.函数输出
'''
#输出通过函数处理过的值
#abs()    绝对值
#len()    字符串的长度
print(abs(-20))
name='heygorgaga'
print(len(name))

'''
4.格式化输出
'''
#  %s  输出字符串
#  %d  输出整型
#如果说语句中只传入一个变量，不用加括号，如果是多个变量需要加括号
name='python'
no=1
print('%s is no.%d'%(name,no))

name='heygor'
print('%s is sososo handsome!!!'% name )

#print('%d is good'% name)

