import tkinter
import tkinter.messagebox
import tkinter.ttk
import re
import random

#初始化窗体
root=tkinter.Tk()

#初始化窗口大小
root["width"]=1000
root["height"]=1000

#初始化窗口标题
root.title("datGenerate")


# 生成数据
def getData():
    pass

# 创建输入框
def Generate():
    #创建文本框初始值/两种初始化方式
    varName=tkinter.StringVar(value='')
    #设置用户名标签
    labelName=tkinter.Label(root,text="first value:",justify=tkinter.RIGHT,width=100)
    #设置位置
    labelName.place(x=125,y=200,width=100,height=50)
    #设置文本框
    entryName=tkinter.Entry(root,width=100,textvariable=varName)
    #设置文本框位置
    entryName.place(x=250,y=200,width=100,height=25)

Generate()

# 设置按钮
def setButton():
    pass



if __name__=="__main__":
    #运行程序
    #print(random.sample([i for i in range(13)],4))
    root.mainloop()
