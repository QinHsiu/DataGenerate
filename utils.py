"""选择生成数据的分布函数，所有函数输入参数均为生成数的一个区间，和生成数据的长度"""
"""泊松分布"""
from numpy.random import poisson
import numpy as np
import pandas as pd



"""生成数据集标签"""
def getName():
    data = []
    data.append("deviceName")
    for head in ["year_", "month_", "week_"]:
        for rear in ["mileage"  # 里程数
            , "driving_time"  # 行驶时间
            , "count"  # 行程次数
            , "harsh_acc"  # 急加次数
            , "harsh_brk"  # 急减次数
            , "harsh_turn"  # 急转次数
            , "harsh_line"  # 急变道次数
            , "commute_mile"  # 通勤里程
            , "commute_count"  # 通勤次数
            , "nighttime_mile"  # 夜间行驶里程数
            , "nighttime_count"  # 夜间行驶次数
            , "tired_trip_mile"  # 疲劳驾驶里程数
            , "tired_trip"]:  # 疲劳驾驶次数
            tempStr = head + rear
            data.append(tempStr)
    data.append("trip_radius")
    with open("dataGenerate.csv", "w+") as f:
        f.write(",".join(data))





"""泊松分布"""
def Poisson():
    lam = input("Please input the value of lam: ")
    size = int(input("Please input the value of size: "))
    return poisson(lam=lam, size=size)


"""伯努利分布"""
"""输入三个参数分别表示特征系数、次数（需要生成数据的大小）、概率"""
from scipy.stats import binom
def Binom():
    k = input("Please input the value of k: ")
    n = input("Please input the value of n: ")
    p = input("Please input the value of p: ")
    return binom(k=k, n=n, p=p)


"""正态分布"""
from scipy.stats import norm
def Norm():
    k = input("Please input the value of lam: ")
    u = input("Please input the value of lam: ")
    thgma = input("Please input the value of lam: ")
    return norm.pdf(k, u, thgma)


"""贝塔分布"""
from scipy.stats import beta
def Beta():
    k = input("Please input the value of k: ")
    a = input("Please input the value of a: ")
    b = input("Please input the value of b: ")
    return beta.pdf(k, a, b)


"""指数分布"""
from scipy.stats import expon
def Expon():
    scale = input("Please input the value of scale: ")
    size = input("Please input the value of size: ")
    return expon.rvs(scale=scale, size=size)


"""调用选择的分布函数"""
def chooseP():
    function_id=int(input("1:Poisson(),2:Binom(),3:Norm(),4:Beta(),5:Expon(): "))
    if function_id==1:
        return Poisson()
    elif function_id==2:
        return Binom()
    elif function_id==3:
        return Norm()
    elif function_id==4:
        return Beta()
    else:
        return Expon()
