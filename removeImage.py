
import os

#指定路径 需要删除的路径地址
path = '/Users/godox/Desktop/xxxx/'


for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith("@2x.png"):             #  填写规则
            os.remove(os.path.join(root, name))
            print("Delete File: " + os.path.join(root, name))
        if name.endswith("@3x.png"):             #  填写规则
            os.remove(os.path.join(root, name))
            print("Delete File: " + os.path.join(root, name))
