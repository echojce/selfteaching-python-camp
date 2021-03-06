text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#1：将text中含有“ea”的单词剔除
import re
list1 = re.split(r"(\W+)",text)   
for i in list1:  
    if 'ea' in i:   
        list1.remove(i) 

#2：将list1中全部的‘better’转换为‘worse’
s0 = ''
s1 = ''
s2 = ''
s1 = s0.join(list1)  
s2 = s1.replace('better','worse')  

#3：将s2中所有单词的大写字母转成小写，小写字母转成大写
s3 = ''
s3 = s2.swapcase()   

#4：将s3中所有的单词按首字母从a到z排列，并输出结果
list2 = re.split(r"\W+",s3)   
list2.sort()    
while '' in list2:   
    list2.remove('')

print("最终结果为:")    
print(list2)    #输出结果