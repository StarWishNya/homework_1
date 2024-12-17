import tkinter as tk
import webbrowser
from datetime import datetime
from pathlib import Path
from tkinter import filedialog, font

import hanlp

import name_identify
import name_statistics
from charaicon import CharaIconButton
from download_utils import download_click
from piepic import piepic
from tooltip import ToolTip

hanlp.pretrained.pos.ALL
HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH)
get_pos = hanlp.load(hanlp.pretrained.pos.CTB9_POS_ELECTRA_SMALL)

global file_path, namelistshow_flag
namelistshow_flag = False
file_path = "data"
window = tk.Tk()
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="微软雅黑", size=12)
window.title("《路人女主的养成方法》轻小说人名统计")
window.resizable(False, False)
length, width = 512, 640
left = (window.winfo_screenwidth() - length) / 2
top = (window.winfo_screenheight() - width) / 2
window.geometry(f"{length}x{width}+{int(left)}+{int(top)}")
window.iconbitmap(Path(__file__).parent / "resource" / "icon.ico")

input_names = tk.StringVar()
input_names.set("泽村 英梨梨")
prompt = tk.Label(window, text="请输入要查找的人名 用逗号分隔：")
prompt.place(x=50, y=0)
entry = tk.Entry(window, textvariable=input_names, font=("楷体", 12, "bold"), width=30)
entry.place(x=53, y=30)

result_dir = Path(__file__).parent / "result"
result_dir.mkdir(exist_ok=True)

def on_select(event):
    select_index = labelist.curselection()
    if select_index:
        input_names.set(namelist[select_index[0]])

def name_list_show():
    global namelistshow_flag
    if not namelistshow_flag:
        namelistshow_flag = True
        global namelist
        namelist = ("泽村 英梨梨", "安艺 伦也", "加藤 惠", "霞之丘 诗羽", "波岛 出海", "冰堂 美智留", "波岛 伊织", "泽村 小百合", "姬川 时乃", "森丘 蓝子")
        global labelist
        labelist = tk.Listbox(window, listvariable=tk.StringVar(value=namelist))
        labelist.place(x=170, y=70)
        labelist.bind("<<ListboxSelect>>", on_select)
    else:
        labelist.place_forget()
        namelistshow_flag = False

def name_list_hide():
    global namelistshow_flag
    if namelistshow_flag:
        labelist.place_forget()
    namelistshow_flag = False

button_list = tk.Button(window, text="主要人物", command=name_list_show)
button_list.place(x=58, y=70)
ToolTip(button_list, "点击查看主要人物列表")

def import_file():
    global file_path
    file_path = filedialog.askopenfilename(title="选择文件", filetypes=[("文本文档", "*.txt")])

def import_path():
    global file_path
    file_path = filedialog.askdirectory(title="选择文件夹")

def import_defaultfile():
    global file_path
    file_path = "data"

button_importfile = tk.Button(window, text="导入其他文件", command=import_file)
button_importfile.place(x=390, y=50)
ToolTip(button_importfile, "请导入txt文件")
button_importdefaultfile = tk.Button(window, text="导入默认文件", command=import_defaultfile)
button_importdefaultfile.place(x=390, y=10)
ToolTip(button_importdefaultfile, "导入默认文件")
button_importpath = tk.Button(window, text="导入文件夹", command=import_path)
button_importpath.place(x=400, y=90)
ToolTip(button_importpath, "请导入文件夹")
output_labels = []

button_allchara = tk.Button(window, text="全部人物", command=lambda: input_names.set("泽村 英梨梨,安艺 伦也,加藤 惠,霞之丘 诗羽,波岛 出海,冰堂 美智留,波岛 伊织,泽村 小百合,姬川 时乃,森丘 蓝子"))
button_allchara.place(x=58, y=180)
ToolTip(button_allchara, "点击查看全部人物列表")

aki_button = CharaIconButton(window, chara_name="安艺 伦也", input_var=input_names, image_path=Path(__file__).parent / "resource" / "Aki_Tomoya.png", width=140, height=140)
aki_button.place(x=20, y=300)
ToolTip(aki_button, "安艺 伦也")

Eriri_button = CharaIconButton(window, chara_name="泽村 英梨梨", input_var=input_names, image_path=Path(__file__).parent / "resource" / "Sawamura_Spencer_Eriri.png", width=140, height=140)
Eriri_button.place(x=190, y=300)
ToolTip(Eriri_button, "泽村 英梨梨")

Megumi_button = CharaIconButton(window, chara_name="加藤 惠", input_var=input_names, image_path=Path(__file__).parent / "resource" / "Kato_Megumi.png", width=140, height=140)
Megumi_button.place(x=360, y=300)
ToolTip(Megumi_button, "加藤 惠")

Utaha_button = CharaIconButton(window, chara_name="霞之丘 诗羽", input_var=input_names, image_path=Path(__file__).parent / "resource" / "Kasumigaoka_Utaha.png", width=140, height=140)
Utaha_button.place(x=20, y=450)
ToolTip(Utaha_button, "霞之丘 诗羽")

Izumi_button = CharaIconButton(window, chara_name="波岛 出海", input_var=input_names, image_path=Path(__file__).parent / "resource" / "Hashima_Izumi.png", width=140, height=140)
Izumi_button.place(x=190, y=450)
ToolTip(Izumi_button, "波岛 出海")

Michiru_button = CharaIconButton(window, chara_name="冰堂 美智留", input_var=input_names, image_path=Path(__file__).parent / "resource" / "Hyodo_Michiru.png", width=140, height=140)
Michiru_button.place(x=360, y=450)
ToolTip(Michiru_button, "冰堂 美智留")
output_window = None

logtime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + "_log.txt"

def click(function = 'default'):
    name_list_hide()
    global file_path, output_window
    print(file_path)
    if output_window is not None:
        output_window.destroy()
        output_window = None
    if function == 'default':
        input_names.set(input_names.get().replace("，", ","))
        new_names = input_names.get().split(",")
        name_counts_total = name_statistics.Namestatistics(new_names, file_path)
    else:
        name_counts_total = name_identify.static_name_from_data(file_path)
        name_counts_total = name_statistics.name_format(name_counts_total)
    for label in output_labels:
        label.destroy()
    output_labels.clear()
    output_window = tk.Toplevel(window)
    output_window.title("统计结果")
    output_window.resizable(False, True)
    length, width = 512, 320
    left = (window.winfo_screenwidth() - length) / 2
    top = (window.winfo_screenheight() - width) / 2
    output_window.geometry(f"{length}x{width}+{int(left)}+{int(top)}")
    output_window.iconbitmap(Path(__file__).parent / "resource" / "icon.ico")
    close_button = tk.Button(output_window, text="关闭", command=output_window.destroy)
    close_button.pack(fill=tk.X, side=tk.BOTTOM)
    try:
        with open(result_dir / logtime, "a", encoding="utf-8") as f:
            if name_counts_total == {}:
                output = tk.Label(output_window, text="没有找到对应的人名", fg="red")
                output.place(x=160, y=70)
                output_labels.append(output)
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n{file_path}\n没有找到对应的人名\n")
            elif name_counts_total == "no file":
                output = tk.Label(output_window, text="没有找到对应的文件", fg="red")
                output.place(x=160, y=70)
                output_labels.append(output)
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n{file_path}\n没有找到对应的文件\n")
            else:
                canvas = tk.Canvas(output_window, width=512, height=320)
                scrollbar = tk.Scrollbar(output_window, orient=tk.VERTICAL, command=canvas.yview)
                output_frame = tk.Frame(canvas)
                canvas.configure(yscrollcommand=scrollbar.set)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                canvas.create_window((0, 0), window=output_frame, anchor=tk.NW)
                output_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
                piedata = {}
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n{file_path}\n")
                for name in name_counts_total:
                    output = tk.Label(output_frame, text=f"{name[0]}:", fg="blue", justify='center')
                    output.pack(fill=tk.X, expand=True)
                    output_labels.append(output)
                    fullname = name_statistics.fullname(name[0])
                    piedata[fullname] = name[1][fullname]
                    f.write(f"{name[0]}:\n")
                    for key in name[1]:
                        output = tk.Label(output_frame, text=f"{key}:{name[1][key]}", justify='center')
                        output.pack(fill=tk.X, expand=True)
                        output_labels.append(output)
                        f.write(f"{key}:{name[1][key]}\n")
                piepic(piedata)
    except Exception as e:
        print(e)
        output = tk.Label(output_window, text="出现错误", fg="red")
        output.place(x=160, y=70)
        output_labels.append(output)
        with open(result_dir / logtime, "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n{file_path}\n出现错误\n")

button_start = tk.Button(window, text="开始统计", command=click, font=("微软雅黑", 14, "bold"), fg="blue")
button_start.place(x=50, y=120)
button_exit = tk.Button(window, text="退出", command=window.quit)
button_exit.pack(fill=tk.X, side=tk.BOTTOM)

def download_and_set_path():
    webbrowser.open("www.wenku8.net")
    global file_path, current_path_label
    file_path = 'download'
    current_path_label = tk.Label(window, text=f"当前路径：{file_path}", font=("微软雅黑", 12, "bold"))
    download_click()

button_download = tk.Button(window, text="下载指定id的小说", command=download_and_set_path, font=("微软雅黑", 14, "bold"), fg="blue")
button_download.place(x=320, y=140)

current_path_label = tk.Label(window, text=f"当前路径：{file_path}", font=("微软雅黑", 12, "bold"))
current_path_label.place(x=50, y=230)

button_ai_identify = tk.Button(window, text="AI人名识别", command=lambda: click('ai'), font=("微软雅黑", 14, "bold"), fg="blue")
button_ai_identify.place(x=375, y=190)

window.mainloop()

if __name__ == "__main__":
    window.mainloop()