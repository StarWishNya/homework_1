import matplotlib.pyplot as plt
import os
from datetime import datetime

def piepic(piedata):
    plt.rcParams['font.sans-serif']=['SimHei']#设置中文显示
    plt.rcParams['axes.unicode_minus']=False#设置负号显示
    plt.figure(figsize=(5,5))#设置画布大小
    plt.pie(piedata.values(),labels=piedata.keys(),autopct='%1.1f%%',shadow=True)#绘制饼图
    plt.title("人名出现次数统计图")#设置标题
    plt.show()#显示图像
    timestamp=datetime.now().strftime("%Y%m%d%H%M%S")#获取当前时间戳
    filename=f"piepic{timestamp}.png"#设置文件名
    plt.savefig(os.path.join(os.path.dirname(__file__)+"/result",filename))#保存图像