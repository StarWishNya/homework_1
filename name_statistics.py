import tkinter as tk
import tkinter.font
import tkinter.filedialog
import os
from tooltip import ToolTip
import cut

def singlenamestatistics(name,file_path):
    names=name.split(" ")
    full_name=""
    for name in names:
        full_name+=name
    count=int(0)
    for singlename in names:
        count+=cut.maincut(singlename,file_path)[singlename]
    return count
def Namestatistics(namelist,file_path="data"):
    name_counts_total={}
    for name in namelist:
        name_counts_total[name]=singlenamestatistics(name,file_path)
    name_counts_total=sorted(name_counts_total.items(),key=lambda x:x[1],reverse=True)#按照出现次数排序
    return name_counts_total

Namelist=("安艺 伦也","泽村 英梨梨","加藤 惠","霞之丘 诗羽")
print(Namestatistics(Namelist))