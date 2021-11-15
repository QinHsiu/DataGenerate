from dataGenerateUI import *
from dataGenerate import *
from utils import *
import pandas as pd
import numpy as np




if __name__ == '__main__':
   #root.mainloop()
   driver_habit = {}
   other_thing={}
   config={}

   """1 输入需要生成数据的长度"""
   data_length = int(input("Please input the length of the dataset: "))
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
   config["data_length"]=data_length
   config["use_mile"]=True #使用里程来计算四急（每50km发生四急（0~1）次）

   #config["month"]=int(input("Please input the number of the month that you want to know!"))
   dataGenerate(driver_habit,other_thing,config)


