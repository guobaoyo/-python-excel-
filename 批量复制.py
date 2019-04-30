import os
from PIL import Image
import shutil
path_csv="/lfs1/users/ymwang/Fashion_class1/result.csv"
path="/lfs1/users/ymwang/Fashion_class1/datasets1/"
df = pd.read_csv(path_csv, header=None)
df.columns = ['filename', 'ynn', 'nyn','nny']
list1=sorted(df.nny)
#print(list1)
# for i in (sorted(df.nny)[-100:]):
#     print(i)
df1=df[df.nny>0.93]
print(df1.filename)
newpath="/lfs1/users/ymwang/Fashion_class1/datasets1/nny/"
for i in df1.filename:
    im=Image.open(os.path.join(path+i))
    print("ok")
    #im.show()
    shutil.copy(os.path.join(path+i),newpath)