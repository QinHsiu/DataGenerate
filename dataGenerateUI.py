import threading
import tkinter
import tkinter.messagebox
import tkinter.ttk as ttk
import re
import random
from dataGenerate import dataGenerate
from dataGenerate import *
from main import *
from utils import *

def getData(*args):
    pass
    #print("getdata")



"""全局变量"""
entry_data_length=None #数据长度
entry_prob_count=None #四急次数
entry_prob_mile=None #行驶里程
entry_night=None #夜间行驶速度的阈值范围[min,max]
entry_daytime=None #白天日常行驶的速度范围[min,max]
entry_commune=None #通勤行驶速度的阈值范围[min,max]
entryUserInfo=None #用户信息
entrayOthers=None #其他信息
root=None #窗口




def GenerateUI(length,width):
    global root
    #初始化窗体
    root=tkinter.Tk()
    #初始化窗口大小
    root["width"]=width
    root["height"]=length
    #初始化窗口标题
    root.title("datGenerate")

    #设置标签名
    labelName=tkinter.Label(root,text="Data Generate",justify=tkinter.RIGHT,width=100)
    #设置位置
    labelName.place(x=425,y=100,width=100,height=25)

    """设置UI与传递配置信息"""
    GenerateComponent(root)
    """提交按钮"""
    submitButton=tkinter.Button(root,text="submit",command=GenerateConfig)
    submitButton.place(x=425,y=500,width=100,height=25)
    root.mainloop()






# 创建输入框
def GenerateComponent(root):
    """使用全局变量用来获取相关信息"""
    global entryUserInfo
    global entry_commune
    global entry_night
    global entry_daytime
    global entrayOthers
    global entry_data_length
    global entry_prob_count
    global entry_prob_mile

    # 创建文本框初始值
    varName = tkinter.StringVar(value='')
    # 设置文本框
    entry_data_length = tkinter.Entry(root,width=100, textvariable=varName)
    #设置标签名
    labelName=tkinter.Label(root,text="Data Length:",justify=tkinter.RIGHT,width=100)
    #设置位置
    labelName.place(x=125,y=200,width=100,height=25)
    #设置文本框
    #global entryName
    #设置文本框位置
    entry_data_length.place(x=225,y=200,width=100,height=25)

    """数据分布函数"""
    comvalue = tkinter.StringVar(value="Poisson")
    entry_prob_count = ttk.Combobox(root, width=100, textvariable=comvalue)
    entry_prob_label=tkinter.Label(root,text="count prob(四急发生次数的分布函数)",justify=tkinter.RIGHT,width=100)
    entry_prob_label.place(x=0,y=300,width=225,height=25)
    entry_prob_count["value"]=("Poisson:泊松","Binom:伯努利","Norm:正态","Beta:贝塔","Expon:指数")
    entry_prob_count.current(0) #当前默认为0
    entry_prob_count.bind("<<ComboboxSelected>>",getData) #绑定事件
    entry_prob_count.pack()
    entry_prob_count.place(x=225,y=300,width=100,height=25)

    """数据分布函数"""
    comvalue = tkinter.StringVar(value="Norm")
    entry_prob_mile = ttk.Combobox(root, width=100, textvariable=comvalue)
    entry_prob_mile_label=tkinter.Label(root,text="mile prob(里程数的分布函数)",justify=tkinter.RIGHT,width=100)
    entry_prob_mile_label.place(x=0,y=400,width=225,height=25)
    entry_prob_mile["value"]=("Poisson:泊松","Binom:伯努利","Norm:正态","Beta:贝塔","Expon:指数")
    entry_prob_mile.current(2) #当前默认为2
    entry_prob_mile.bind("<<ComboboxSelected>>",getData) #绑定事件
    entry_prob_mile.pack()
    entry_prob_mile.place(x=225,y=400,width=100,height=25)

    """数据阈值，输入最小与最大值"""
    # 创建文本框初始值
    varName = tkinter.StringVar(value='10 40')
    # 设置文本框
    entry_night = tkinter.Entry(root,width=100, textvariable=varName)
    #设置标签名
    labelName=tkinter.Label(root,text="Night speed(夜间速度阈值,(单位km/h)):",justify=tkinter.RIGHT,width=100)
    #设置位置
    labelName.place(x=475,y=200,width=245,height=25)
    #设置文本框位置
    entry_night.place(x=725,y=200,width=100,height=25)

    # 创建文本框初始值
    varName = tkinter.StringVar(value='30 50')
    # 设置文本框
    entry_daytime = tkinter.Entry(root,width=100, textvariable=varName)
    #设置标签名
    labelName=tkinter.Label(root,text="Daytime speed(日间速度阈值,(单位km/h)):",justify=tkinter.RIGHT,width=100)
    #设置位置
    labelName.place(x=475,y=300,width=245,height=25)
    #设置文本框位置
    entry_daytime.place(x=725,y=300,width=100,height=25)

    # 创建文本框初始值
    varName = tkinter.StringVar(value='20 30')
    # 设置文本框
    entry_commune = tkinter.Entry(root,width=100, textvariable=varName)
    #设置标签名
    labelName=tkinter.Label(root,text="Commune speed(通勤速度阈值,(单位km/h)):",justify=tkinter.RIGHT,width=100)
    #设置位置
    labelName.place(x=475,y=400,width=245,height=25)
    #设置文本框位置
    entry_commune.place(x=725,y=400,width=100,height=25)


"""设置定时关闭窗口"""
def timeToClose(root):
    root.quit()
    root.update()



# 设置按钮
def GenerateConfig():
    config={}
    global entryUserInfo
    global entry_commune
    global entry_night
    global entry_daytime
    global entrayOthers
    global entry_data_length
    global entry_prob_count
    global entry_prob_mile
    global root

    config["data_length"]=int(entry_data_length.get())

    """配置信息"""
    driver_habit = {}
    other_thing = {}

    """获取三种速度的阈值:2021/11/26"""
    other_thing["nds_mi"],other_thing["nds_ma"]=map(eval,entry_night.get().split(" "))
    other_thing["cds_mi"],other_thing["cds_ma"]=map(eval,entry_commune.get().split(" "))
    other_thing["dds_mi"],other_thing["dds_ma"]=map(eval,entry_daytime.get().split(" "))
    # print(other_thing)



    if not config:
        raise ValueError("Please chose your config information!")
    else:
        config["use_mile"] = True  # 使用里程来计算四急（每50km发生四急（0~1）次）
        dataGenerate(driver_habit, other_thing, config)
        threading.Timer(5, timeToClose, args=(root,)).start()  # 5秒关闭
        root.mainloop()
        root.destroy()









if __name__=="__main__":
    tkinter_width = 1000
    tkinter_height = 1000
    GenerateUI(tkinter_width, tkinter_height)

    # 运行程序
    # print(random.sample([i for i in range(13)],4))
    # driver_habit = {}
    # other_thing = {}
    # config = {}
    """1 输入需要生成数据的长度"""
    # data_length = int(input("Please input the length of the dataset: "))
    """2 输入夜间出行在一周之中的占比"""
    # driver_habit["night_driving"] = float(input("Please input the proportion of the night driving: "))
    """3 输入短期旅行在一周之中的占比"""
    # driver_habit["short_term_trip"] = float(input("Please input the proportion of the short term trip: "))
    """4 输出周末在家在一周之中的占比"""
    # driver_habit["weekend_home"] = float(input("Please input the proportion of the weeekend home: "))
    """5 输入周末出行的概率"""
    # weeken_out = float(input("Please input the count of the weekend out: "))
    """6 发生随机事件的概率"""
    # random_thing_possibility = float(input("Please input the possibility of the random things: "))
    """7 输入需要使用的数据分布函数以及其相关参数"""
    # function={1:Poisson(),2:Binom(),3:Norm(),4:Beta(),5:Expon()}
    # config["data_length"] = data_length
    # config["use_mile"] = True  # 使用里程来计算四急（每50km发生四急（0~1）次）
    """添加三个输入信息，分别表示夜间行驶速度、通勤行驶速度、白天行驶速度,时间：2021/11/16"""
    """在代码中使用的随机生成，区间分别为[20000,30000),[20000,25000),[10000,20000)"""
    # other_thing["night_driving_distance"]=30000
    # other_thing["commute_driving_distance"] = 25000
    # other_thing["daytime_driving_distance"] = 20000

    # config["month"]=int(input("Please input the number of the month that you want to know!"))
    # dataGenerate(driver_habit, other_thing, config)

