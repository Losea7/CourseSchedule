from ics import Calendar, Event
from datetime import datetime, timedelta

# 学期基础信息配置：
# 定义开学日期
semester_start = datetime(2025, 2, 24)

# 定义每节课的开始和结束时间
time_slots = {
    "1-2": ("08:30:00", "10:15:00"),
    "3-4": ("10:30:00", "12:15:00"),
    "5-6": ("14:00:00", "15:45:00"),
    "7-8": ("16:00:00", "17:45:00"),
    "9-10": ("18:45:00", "20:30:00"),
    "11-12": ("20:45:00", "22:30:00")
}


def parse_weeks(week_str):
    '''对周次字符串进行处理，得到升序排序后的week列表'''
    print('正在对周次字符串进行处理：')
    ranges = week_str.split(",") # 将week_str字符串以','为分隔符分割为多个字符串储存到ranges列表中
    weeks = [] # 定义名为weeks的空列表
    for r in ranges:
        if '-' in r: # 如果是范围周
            start, end = map(int, r.split('-')) # 解析开始和结束周
            weeks.extend(range(start, end+1)) # 将范围内的周次添加到列表
        else: # 如果是单个周
            weeks.append(int(r))
    print(sorted(weeks))
    return sorted(weeks) # 返回排序后的weeks列表（升序）



def calculate_date(base_date, weekday, week_num):
    '''计算日期'''
    print('正在计算日期：')
    days_offset = (weekday - 1) + (week_num - 1) * 7 # 计算日期偏移量
    print(base_date + timedelta(days=days_offset))
    return base_date + timedelta(days=days_offset) #返回最终日期


def create_events(course_data):
    '''利用event模块创建日历日程'''
    cal = Calendar()
    for row in course_data:
        print('-' * 200)
        print('导入课程：',row)
        day_col = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"].index(row["weekday"]) + 1
        time_slot = row["time_slot"]
        start_time, end_time = time_slots[time_slot] # 获取上课时间和下课时间
        print('正在遍历weeks列表：')
        for week in parse_weeks(row["weeks"]): # 在排序后的weeks列表中遍历
            course_date = calculate_date(semester_start, day_col, week)
            dt_start = datetime.combine(course_date, datetime.strptime(start_time, "%H:%M:%S").time()) - timedelta(hours=8)
            dt_end = datetime.combine(course_date, datetime.strptime(end_time, "%H:%M:%S").time()) - timedelta(hours=8)
            
            print()

            print('正在创建日程：')
            event = Event()
            event.name = f"{row['course']} [{row['teacher']}]" + (" [实验]" if "实验" in row['course'] else "")
            print('日程名称为：',event.name)
            event.begin = dt_start.strftime("%Y-%m-%d %H:%M:%S")
            event.end = dt_end.strftime("%Y-%m-%d %H:%M:%S")
            print('日程开始和结束时间为：',event.begin,event.end)
            event.location = row["location"]
            event.description = f"周次: {row['weeks']}\n时间段: 第{time_slot}节"
            cal.events.add(event)
            print('已经添加该日程！')
            print()
    return cal
