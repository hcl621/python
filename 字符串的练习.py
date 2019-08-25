#coding=utf-8
'''
1.提示用户输入内容，如果为空则提示！
2.判断用户输入的字符串首字母是否为元音(A、E、I、O、U)
3.如果为元音，则在字符串后加上'ay'
  eg.如果用户输入apple'-'appleay'
4.如果首字母为辅音字母，则将该字符串首字母移动结尾，并加上'ay'
  eg.如果用户输入'hello'-'ellohay'
  '''
a=input('请输入字符串>>')
'''
if a=='':
    print('为空！')
'''

'''
if len(a)==0:
    print('为空')
elif a[0]=='A' or  a[0]=='E':
    print('yes')
else:
    pass
'''

if len(a)==0:
    print('null')
elif a[0] in 'aeiouAEIOU':
    print(a+'ay')
else:
    print(a[1:]+a[0]+'ay')
