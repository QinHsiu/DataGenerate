主要代码架构：
1.dataGenerate.py:负责生成数据的主要函数，包括架构
2.dataGenerateUI.py:会显示一个框架，负责将参数输入过程可视化
3.main.py:主要的运行函数
4.utils.py:包含所有套件函数，各种分布函数以及其他函数


数据部分：
"""输入数据介绍"""
"""用户驾驶行为习惯"""
driver_habit = {
    "night_driving": 0  # 表明是否倾向与夜间出行,数据区间[0,1]表示夜间出行的频率
    , "short_term_trip": 0  # 表明是否倾向于短途旅行，数据区间[0,1]表示短期出行的偏好程度
    ,'long_term_trip':0 #表明是否倾向于长途旅行
    , "weekend_home": 0  # 表明周末是否很少出门，数据区间[0,1]表示周末在家的程度
}

"""其他事情，例如加班、意外事件等"""
other_thing = {
    "overtime_count": 0   # 周末加班的概率[0,1]
    ,"random_thing_possibility":0 #随机距离
    ,'week_commute_count':20 # 一周通勤次数
    ,'commute_driving_speed:20~30' #通勤行驶速度，一个阈值范围
    ,'daytime_driving_speed:30~50' #日间正常行驶速度，一个阈值范围
    ,'night_driving_speed:10~40' #夜间行驶速度,一个阈值范围
}

"""配置信息"""
config={
    'data_length':10 #生成数据长度
    'use_mile':使用行程数计算四急
}



"""通勤行驶时长、日间行驶时长、夜间行驶时长""":均由次数与单次通行时长相乘获得

"""长途旅游时长、短途旅游时长"""：由行程里程数除以日间正常行驶速度获得


"""一周里程正常取值区间为[200000,400000]"""
"""每周行程数目为20次，注意节假日"""
"""一般车速为30~50KM"""

# 驾驶习惯
normal_driving_distance = [10000, 40000]  # 单位为M
reference = 20000  # 正常行驶参考值
normal_communte_distance = [20000, 30000]  # 单位为M
referance = 25000  # 通勤正常参考值
random_thing_possibility = 0.5  # 发生随机事件的概率
weekend_out = 0.6  # 周末出行的概率
data_length = 1  # 生成的数据长度
