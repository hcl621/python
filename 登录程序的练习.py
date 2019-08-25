#coding=utf-8
请输入注册信息
a.用户输入不能为空
b.用户名和密码都必须由字符和数字组成
c.如果用户名或密码不符合条件就提示重新输入
d.3次退出注册
dic={'simida':'123','kouniqiwa':'456'}

while 1:
    name=input('请输入用户名')
    if name in dic.keys():
        print('用户名正确')
        while 1:
            passwd=input('请输入密码')
            if passwd==dic[name]:
                print('输入密码正确')
                print('您已经登录')
                break
            else:
                print('密码不匹配，请重新弄输入')
        break
    else:
        print('用户名输入错误,请重新输入用户名')
