import os
from PIL import Image
import shutil
import pandas as pd
path_csv="./tiaowen.csv"#尽量用英文名字，这样会可靠一些
path=""
df = pd.read_csv(path_csv, header=None)#先将原来的文件读取并且称其为df
df.columns = ['filename', 'tiaowen']#实际上将表格的两个列定义为filename 和 tiaowen
list1=sorted(df.tiaowen)#从小到大排序,而使用sort()方法对list排序会修改list本身，不会返回新的list，而sorted()会返回一个新的list，并不会改变原来的list
#print('**************')
for i in (sorted(df.tiaowen)[-100:]):#看看倒数100个都是多少评分
    print(i)
#print('**************')
df1=df[df.tiaowen>0.999528]#根据刚才的倒数第100个的分数决定数值
#print(df1.filename)
list2=[]#新建个list2这个列表
for i in df1.tiaowen:#
    list2.append(i)#将tiaowen这个  概率  加入到list2这个列表中
print(list2)#
print('**************')

newpath="./上衣/tiaowen1"#新建一个tiaowen的文件夹
for i in df1.filename:
    print(i)
    try:
        shutil.copy(i,newpath)#i为源路径，newpath为目标路径，在这里做一个try和except目的是将报错的文件跳过去（之前不用try的时候会发生文件重名的bug）
    except FileNotFoundError as e:
        continue
j=0#下面的这个for循环的作用是将图片的名字改为概率.jpg
for file_name in os.listdir(newpath):#在这里就将file_name全变为newpath里面的文件名字

    os.rename(os.path.join(newpath,file_name),os.path.join(newpath,str(list2[j])+".jpg"))
    j+=1#上面这句话最好加个try和except的语句这样就可以避免报错