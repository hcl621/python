#coding=utf-8
'''
输入一个3位数字，判断是否为水仙花数：
水仙花数参考:https://baike.baidu.com/item/%E6%B0%B4%E4%BB%99%E8%8A%B1%E6%95%B0/2746160?fr=aladdin
'''

a=int(input('输入一个三位数>>'))
#a=153
#百位
bai=a//100

#十位
shi=a%100//10

#个位
ge=a%10

if bai**3+ge**3+shi**3==a:
    print('水仙花')
else:
    print('not 水仙花')
