import os
import jieba
from collections import Counter
def extract_chinese_names(text):#提取中文名字
    names=[]
    words=jieba.cut(text,cut_all=False,HMM=True)#使用jieba库进行分词
    for word in words:
        if  '\u4e00'<=word[0]<='\u9fff':#判断是否为中文
            names.append(word)#将中文名字添加到列表中
    return names

def process_file(file_path,target_names):#处理文件
    try:
        with open(file_path,'r',encoding='utf-8')as file:#打开文件
            text=file.read()
            names_in_file=extract_chinese_names(text)#提取中文名字
            name_counts={name:names_in_file.count(name) for name in target_names}#统计名字出现的次数
            return name_counts
    except FileNotFoundError:#处理文件不存在的情况
        print(f"文件{file_path}不存在")
        return {}
    except Exception as e:#处理其他异常
        print(f"文件{file_path}处理时发生错误：{e}")
        return {}
    
def process_directory(directory_path,target_names):#处理目录
    name_counts_total = Counter()
    if os.path.isfile(directory_path) and directory_path.lower().endswith(".txt"):#判断是否为目录
        name_counts = process_file(directory_path, target_names)
        name_counts_total += Counter(name_counts)
    else:
        file_list=os.listdir(directory_path)#获取目录下的文件列表
        if not file_list:
            return "no file"
        for filename in file_list:
            file_path=os.path.join(directory_path,filename)
            if os.path.isfile(file_path) and filename.lower().endswith(".txt"):
                name_counts = process_file(file_path, target_names)
                name_counts_total += Counter(name_counts)
    return name_counts_total

def maincut(input_names,directory_path): # 替换目录路径
    target_names=input_names.split()#将输入的人名转换为列表
    for name in target_names:
        jieba.add_word(name)#添加人名到jieba库中
    name_counts_total=process_directory(directory_path, target_names)#处理目录
    return name_counts_total
