import random
from utils import *


"""计算一周的里程数"""
def calculate(driver_habit
              , holiday_num=None
              ,other_thing=None
              ,config=None
              ,seeds=None #随机数种子
              ):
    week_data = {}
    for head in ["week_"]:
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
            week_data[head + rear] = 0 #所有值初始化为0
    week_data["trip_radius"] = 0  # 行程半径


    """夜间、通勤、日常的正常行驶速度，单位m/h"""
    night_driving_speed = other_thing["night_driving_speed"]
    commute_driving_speed=other_thing["commute_driving_speed"]
    daytime_driving_speed = other_thing["daytime_driving_speed"]

    """夜间出行次数、夜间里程数与一周夜间行驶的时长"""
    week_data["week_nighttime_count"] += int(5 * driver_habit["night_driving"])+int(2 * (1-driver_habit["weekend_home"]))
    week_data["week_nighttime_mile"] = night_driving_speed * week_data["week_nighttime_count"]*other_thing["night_driving_time"]
    night_driving_time=week_data["week_nighttime_count"]*other_thing["night_driving_time"]

    """初始化旅游距离和次数(以及旅游的时长)"""
    trip_distance=0
    trip_count=0

    if holiday_num == None:
        """一周通勤次数、里程数与通勤时长"""
        week_data["week_commute_count"]=other_thing["week_commute_count"] #一周通勤次数
        week_data["week_commute_mile"]=other_thing["week_commute_count"]*commute_driving_speed*other_thing["commute_driving_time"]
        commute_driving_time=other_thing["week_commute_count"] * other_thing["commute_driving_time"]

        """表明用户会出去旅游"""
        if driver_habit["weekend_home"]<1:
            """长途、短途旅行"""
            short_term_trip = int(2 * driver_habit["short_term_trip"])
            long_term_trip = int(2 * (1-driver_habit["short_term_trip"]))
            trip_count=short_term_trip+long_term_trip
            trip_distance=short_term_trip*random.sample(range(30000,100000),1)[0]+long_term_trip*random.sample(range(100000,400000),1)[0]
    else:
        """如果为长假，通勤距离为0；否则剪掉假期所放掉的次数"""
        if holiday_num==7:
            week_data["week_commute_count"]=0
            week_data["week_commute_mile"]=0
            commute_driving_time =0
        else:
            week_data["week_commute_count"]=other_thing["week_commute_count"]-2*holiday_num
            week_data["week_commute_mile"]=other_thing["week_commute_count"]*commute_driving_speed*other_thing["commute_driving_time"]
            commute_driving_time = other_thing["week_commute_count"] * other_thing["commute_driving_time"]

        """旅行距离"""
        if driver_habit["weekend_home"]<1:
            short_term_trip = int(holiday_num * driver_habit["short_term_trip"])
            long_term_trip = int(holiday_num * (1 - driver_habit["short_term_trip"]))
            trip_count=short_term_trip+long_term_trip
            trip_distance=short_term_trip*random.sample(range(30000,100000),1)[0]+long_term_trip*random.sample(range(100000,400000),1)[0]



    distance_total=week_data["week_nighttime_mile"]+week_data["week_commute_mile"]+trip_distance
    week_data["week_mileage"] += distance_total
    week_data["week_driving_time"]=night_driving_time+commute_driving_time+trip_distance//daytime_driving_speed*3600  # 平均时速为30km/h,计算时间再乘以3600
    week_data["week_count"]=week_data["week_nighttime_count"]+week_data["week_commute_count"]+trip_count

    """使用一周行程里程数或者一周行程次数来估计四急次数"""
    if config["use_mile"]==True:
        tp = random.sample([0, 1], 1)[0]
        week_data["week_harsh_line"]=week_data["week_mileage"]//50000*tp//4

        tp = random.sample([0, 1], 1)[0]
        week_data["week_harsh_acc"]=week_data["week_mileage"]//50000*tp//4

        tp = random.sample([0, 1], 1)[0]
        week_data["week_harsh_brk"]=week_data["week_mileage"]//50000*tp//4

        tp = random.sample([0, 1], 1)[0]
        week_data["week_harsh_turn"]=week_data["week_mileage"]//50000*tp//4
    else:

        tp = random.sample([0, 1], 1)[0]
        week_data["week_harsh_line"] = week_data["week_count"] // 2 * tp


        tp = random.sample([0, 1], 1)[0]
        week_data["week_harsh_acc"] = week_data["week_count"] // 2 * tp


        tp = random.sample([0, 1], 1)[0]
        week_data["week_harsh_brk"] = week_data["week_count"] // 2 * tp


        tp = random.sample([0, 1], 1)[0]
        week_data["week_harsh_turn"] = week_data["week_count"] // 2 * tp

    """修改了四急生成次数的方法：2021/11/13"""
    four_thing_count=week_data["week_harsh_brk"]+week_data["week_harsh_line"]+week_data["week_harsh_turn"]+week_data["week_harsh_acc"]
    while four_thing_count>week_data["week_count"]*0.5:
        if week_data["week_harsh_line"]>0:
            four_thing_count-=1
            week_data["week_harsh_line"]-=1
            continue
        else:
            if week_data["week_harsh_turn"]>0:
                four_thing_count-=1
                week_data["week_harsh_turn"]-=1
            elif week_data["week_harsh_brk"]>0:
                four_thing_count-=1
                week_data["week_harsh_brk"]-=1
            elif week_data["week_harsh_acc"]>0:
                four_thing_count-=1
                week_data["week_harsh_acc"]-=1
            continue


    #当一周行驶距离大于400000km发生一次疲劳驾驶
    if distance_total>400000:
        week_data["week_tired_trip_mile"]=distance_total%400000
        week_data["week_tired_trip"]=distance_total//400000
    return week_data




def dataGenerate(driver_habit,other_thing,config):
    """获取数据列名"""
    getName()
    """获取数据长度"""
    if config=={}:
        config["data_length"]=int(input("Please input the length of the dataset"))
        data_length=config["data_length"]
    else:
        data_length=config["data_length"]

    """deviceName 装置名称使用累加"""
    data = pd.read_csv("dataGenerate.csv")
    data["deviceName"] = range(data_length)
    data["trip_radius"]=0

    year_data={}
    for head in ["year_"]:
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
            year_data[head + rear] = 0


    month_data={}
    for head in ["month_"]:
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
            month_data[head + rear] = 0

    """month"""
    #data_year = int(input("Please input the year: "))
    data_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    """根据输入年份更新输入的月份"""

    """2月：春节 7天"""
    """3月：清明节 3天"""
    """5月：五一 3天"""
    """6月：端午节 3天"""
    """9月：中秋节 3天"""
    """10月：国庆节 7天"""
    long_term = [2, 10]
    short_term = [3, 5, 6, 9]



    p=np.arange(0,1,0.0005).tolist()
    wcc=list(range(14,22)) #一周通勤次数


    for i in range(data_length):

        # 对于每一个条数据，每一次更新数据需要将年的数据清空
        for y_k in year_data:
            year_data[y_k]=0

        # 设置随机数种子,使用不同的随机数种子
        random.shuffle(p) #打乱顺序
        random.seed(i)
        #if driver_habit=={}:
        """驾驶习惯"""
        driver_habit["night_driving"] = random.sample(p,1)[0]
        driver_habit["short_term_trip"] = random.sample(p,1)[0]
        driver_habit["weekend_home"]=random.sample(p,1)[0]

        #if other_thing=={}:
        """其他事情，例如加班、随机事件、一周通勤次数"""
        other_thing["overtime_count"]=random.sample(p,1)[0]
        other_thing["random_thing_possibility"]=random.sample(p,1)[0]
        other_thing["week_commute_count"]=random.sample(wcc,1)[0]

        """设置三种速度的阈值,分别为夜间、通勤与日间正常行驶速度:2021/11/26"""
        nds_ma=other_thing["nds_ma"]*1000
        nds_mi=other_thing["nds_mi"]*1000

        cds_ma=other_thing["cds_ma"]*1000
        cds_mi=other_thing["cds_mi"]*1000

        dds_ma=other_thing["dds_ma"]*1000
        dds_mi=other_thing["dds_mi"]*1000

        nds_mi=int(nds_mi)
        nds_ma=int(nds_ma)
        cds_mi=int(cds_mi)
        cds_ma=int(cds_ma)
        dds_mi=int(dds_mi)
        dds_ma=int(dds_ma)

        """设置通勤速度、日间行驶速度、夜间行驶速度：2021/11/16"""
        other_thing["night_driving_speed"] = random.sample(range(nds_mi,nds_ma,1),1)[0]
        other_thing["commute_driving_speed"] = random.sample(range(cds_mi,cds_ma,1),1)[0]
        other_thing["daytime_driving_speed"] = random.sample(range(dds_mi,dds_ma,1),1)[0]

        """设置单次通勤时长、单次夜间行驶时长,2021/11/25"""
        other_thing["commute_driving_time"]=random.sample(np.arange(0.2,1,0.005).tolist(),1)[0]
        other_thing["night_driving_time"]=random.sample(np.arange(0.2,1,0.005).tolist(),1)[0]



        for m in data_month:
            if m in long_term:
                h=7
            elif m in short_term:
                h=3
            else:
                h=None
            # 为了防止两次随机破环数据的连续性,计算一周的情况，2021/11/13
            week_data=calculate(driver_habit=driver_habit,holiday_num=h,other_thing=other_thing,config=config,seeds=i)
            for t_w in week_data:
                data.loc[i,t_w]=int(week_data[t_w]) #所有数据均为整型数据

            # 计算一个月的驾驶情况:2021/11/13
            if h:
                week_data_0 = calculate(driver_habit=driver_habit,other_thing=other_thing, config=config, seeds=i)
                for t_w in week_data_0: #将所有数据变为整型
                    week_data_0[t_w]=int(week_data_0[t_w])
            else:
                week_data_0=week_data

            for m_l in range(len(list(month_data.keys()))):
                month_data[list(month_data.keys())[m_l]]=week_data[list(week_data.keys())[m_l]]+3*week_data_0[list(week_data_0.keys())[m_l]]

            """修改日期：2021/11/13，添加了设定生成指定月份的配置"""
            if "month" not in list(config.keys()):
                """默认使用12月份的数据"""
                for t_m in month_data:
                    data.loc[i,t_m]=int(month_data[t_m]) #整型
            else:
                """使用指定月份的数据"""
                if config["month"]==m:
                    for t_m in month_data:
                        data.loc[i, t_m] = int(month_data[t_m]) #整型

            """求一年的数据"""
            for m_y in range(len(list(year_data.keys()))):
                year_data[list(year_data.keys())[m_y]]+=month_data[list(month_data.keys())[m_y]]

        """汇总一年的数据"""
        for t_y in year_data:
            data.loc[i,t_y]=int(year_data[t_y]) #整型


    data.to_csv("dataGenerate.csv",index=False)
    #print(data)

if __name__ == '__main__':
    driver_habit={}
    """1 输入需要生成数据的长度"""
    data_length = int(input("Please input the length of the dataset: "))
    """2 输入夜间出行在一周之中的占比"""
    #driver_habit["night_driving"] = float(input("Please input the proportion of the night driving: "))
    """3 输入短期旅行在一周之中的占比"""
    #driver_habit["short_term_trip"] = float(input("Please input the proportion of the short term trip: "))
    """4 输出周末在家在一周之中的占比"""
    #driver_habit["weekend_home"] = float(input("Please input the proportion of the weeekend home: "))
    """5 输入周末出行的概率"""
    # weeken_out = float(input("Please input the count of the weekend out: "))
    """6 发生随机事件的概率"""
    # random_thing_possibility = float(input("Please input the possibility of the random things: "))
    """7 输入需要使用的数据分布函数以及其相关参数"""
    # function={1:Poisson(),2:Binom(),3:Norm(),4:Beta(),5:Expon()}
    #dataGenerate(driver_habit, data_length)
    #l=[1,2,3,4,5,6,7]
    #random.shuffle(l)
    #print(l)





