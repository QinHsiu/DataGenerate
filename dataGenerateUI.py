import tkinter
import tkinter.messagebox
import tkinter.ttk
import re
import random
from dataGenerate import dataGenerate
from dataGenerate import *
from main import *

#初始化窗体
root=tkinter.Tk()

#初始化窗口大小
root["width"]=1000
root["height"]=1000

#初始化窗口标题
root.title("datGenerate")



entryName=0


# 生成数据
def getData():
    pass

# 创建输入框
def Generate():
    """数据长度"""
    #创建文本框初始值/两种初始化方式
    varName=tkinter.StringVar(value='')
    #设置用户名标签
    labelName=tkinter.Label(root,text="Data Length:",justify=tkinter.RIGHT,width=100)
    #设置位置
    labelName.place(x=125,y=200,width=100,height=25)
    global entryName
    #设置文本框
    entryName=tkinter.Entry(root,width=100,textvariable=varName)
    #设置文本框位置
    entryName.place(x=225,y=200,width=100,height=25)


Generate()

# 设置按钮
def setButton():
    """提交按钮"""
    driver_habit = {}
    other_thing = {}
    config = {}
    #data_length = int(input("Please input the length of the dataset: "))
    global data_length
    data_length=int(entryName.get())
    config["data_length"] = data_length
    config["use_mile"] = True  # 使用里程来计算四急（每50km发生四急（0~1）次）
    dataGenerate(driver_habit, other_thing, config)

submitButton=tkinter.Button(root,text="submit",command=setButton)
submitButton.place(x=225,y=300,width=100,height=25)





if __name__=="__main__":
    # 运行程序
    # print(random.sample([i for i in range(13)],4))
    root.mainloop()
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

