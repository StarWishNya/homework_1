import cut
import tkinter as tk
import tkinter.font
import tkinter.filedialog
import os
from tooltip import ToolTip
from charaicon import CharaIconButton
import name_statistics

global file_path,namelistshow_flag
namelistshow_flag=False
file_path="data"
window=tk.Tk()#创建窗口
default_font = tkinter.font.nametofont("TkDefaultFont")#设置默认字体
default_font.configure(family="微软雅黑",size=12)
window.title("《路人女主的养成方法》轻小说人名统计")
window.resizable(False,False)#设置窗口大小不可变
length=512
width=640
left=(window.winfo_screenwidth()-length)/2#获取窗口左上角的横坐标
top=(window.winfo_screenheight()-width)/2#获取窗口左上角的纵坐标
window.geometry("%dx%d+%d+%d"%(length,width,left,top))#设置窗口的初始位置和大小
window.iconbitmap(os.path.join(os.path.dirname(__file__)+"/resource","icon.ico"))#设置窗口图标

input_names=tk.StringVar()#创建输入框的变量
input_names.set("泽村 英梨梨")
prompt=tk.Label(window,text="请输入要查找的人名 用逗号分隔：")#创建标签
prompt.place(x=50,y=0)#显示标签
entry=tk.Entry(window,textvariable=input_names,font=("楷体",12,"bold"))#创建输入框
entry.place(x=53,y=30)#显示输入框

def on_select(event):#事件处理函数
    select_index=labelist.curselection()#获取选中的索引
    if select_index:
        input_names.set(namelist[select_index[0]])#将选中的人名添加到输入框中

def namelistshow():
    global namelistshow_flag
    if namelistshow_flag==False:
        namelistshow_flag=True
        global namelist
        namelist=("泽村 英梨梨","安艺 伦也","加藤 惠","霞之丘 诗羽","波岛 出海","冰堂 美智留","波岛 伊织","泽村 小百合","姬川 时乃","森丘 蓝子")
        global labelist
        labelist=tk.Listbox(window,listvariable=tk.StringVar(value=namelist))#创建列表框
        labelist.place(x=170,y=70)#显示列表框
        labelist.bind("<<ListboxSelect>>",on_select)#绑定事件处理函数
    else:
        labelist.place_forget()#隐藏列表框
        namelistshow_flag=False

def namelisthide():
    global namelistshow_flag
    if namelistshow_flag:
        labelist.place_forget()#隐藏列表框
    namelistshow_flag=False

button_list=tk.Button(window,text="主要人物",command=namelistshow)#创建按钮
button_list.place(x=58,y=70)#显示按钮
ToolTip(button_list,"点击查看主要人物列表")

def import_file():
    global file_path
    file_path=tk.filedialog.askopenfilename(title="选择文件", filetypes=[("文本文档", "*.txt")])#获取文件路径

def import_path():
    global file_path
    file_path=tk.filedialog.askdirectory(title="选择文件夹")#获取文件夹路径

def import_defaultfile():
    global file_path
    file_path="data"

button_importfile=tk.Button(window,text="导入其他文件",command=import_file)
button_importfile.place(x=390,y=50)
ToolTip(button_importfile,"请导入txt文件")
button_importdefaultfile=tk.Button(window,text="导入默认文件",command=import_defaultfile)
button_importdefaultfile.place(x=390,y=10)
ToolTip(button_importdefaultfile,"导入默认文件")
button_importpath=tk.Button(window,text="导入文件夹",command=import_path)
button_importpath.place(x=390,y=90)
ToolTip(button_importpath,"请导入文件夹")
output_labels=[]
print(file_path)

aki_button=CharaIconButton(window,chara_name="安艺 伦也",input_var=input_names,image_path=os.path.join(os.path.dirname(__file__)+"/resource","Aki_Tomoya.png"),width=140,height=140)
aki_button.place(x=20,y=300)
ToolTip(aki_button,"安艺 伦也")

Eriri_button=CharaIconButton(window,chara_name="泽村 英梨梨",input_var=input_names,image_path=os.path.join(os.path.dirname(__file__)+"/resource","Sawamura_Spencer_Eriri.png"),width=140,height=140)
Eriri_button.place(x=190,y=300)
ToolTip(Eriri_button,"泽村 英梨梨")

Megumi_button=CharaIconButton(window,chara_name="加藤 惠",input_var=input_names,image_path=os.path.join(os.path.dirname(__file__)+"/resource","Kato_Megumi.png"),width=140,height=140)
Megumi_button.place(x=360,y=300)
ToolTip(Megumi_button,"加藤 惠")

Utaha_button=CharaIconButton(window,chara_name="霞之丘 诗羽",input_var=input_names,image_path=os.path.join(os.path.dirname(__file__)+"/resource","Kasumigaoka_Utaha.png"),width=140,height=140)
Utaha_button.place(x=20,y=450)
ToolTip(Utaha_button,"霞之丘 诗羽")

Izumi_button=CharaIconButton(window,chara_name="波岛 出海",input_var=input_names,image_path=os.path.join(os.path.dirname(__file__)+"/resource","Hashima_Izumi.png"),width=140,height=140)
Izumi_button.place(x=190,y=450)
ToolTip(Izumi_button,"波岛 出海")

Michiru_button=CharaIconButton(window,chara_name="冰堂 美智留",input_var=input_names,image_path=os.path.join(os.path.dirname(__file__)+"/resource","Hyodo_Michiru.png"),width=140,height=140)
Michiru_button.place(x=360,y=450)
ToolTip(Michiru_button,"冰堂 美智留")

def click():
    namelisthide()
    global file_path
    input_names.set(input_names.get().replace("，",","))#将中文逗号替换为英文逗号
    new_names=input_names.get().split(",")#将输入的人名转换为列表
    name_counts_total=name_statistics.Namestatistics(new_names,file_path)#统计人名出现的次数
    for label in output_labels:
        label.destroy()
    output_labels.clear()
    if name_counts_total=={}:#没有找到对应的人名
        output=tk.Label(window,text="没有找到对应的人名",fg="red")
        output.place(x=170,y=70)
        output_labels.append(output)
    elif name_counts_total=="no file":#文件不存在
        output=tk.Label(window,text="没有找到对应的文件",fg="red")
        output.place(x=170,y=70)
        output_labels.append(output)
    else:
        y_coordinates=70
        for name,count in name_counts_total:
            output=tk.Label(window,text=f"{name}: {count} 次")
            output.place(x=170,y=y_coordinates)
            output_labels.append(output)
            y_coordinates+=30

button_start=tk.Button(window,text="开始统计",command=click,font=("微软雅黑",14,"bold"),fg="blue")#创建按钮
button_start.place(x=50,y=120)#显示按钮
button_exit=tk.Button(window,text="退出",command=window.quit)#创建按钮
button_exit.pack(fill=tkinter.X,side=tk.BOTTOM)#显示按钮

window.mainloop()#显示窗口