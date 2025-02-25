import course_schedule_tools

# 创建课表字典
# 请根据你自己的课表修改以下变量
courses = [
    # 星期一
    {"weekday": "星期一", "time_slot": "1-2", "course": "信息论与编码", "teacher": "汪洋", "weeks": "9-10,12-14,16", "location": "T5304"},
    {"weekday": "星期一", "time_slot": "5-6", "course": "移动通信", "teacher": "张霆廷", "weeks": "3-10,12,13", "location": "G707"},
    # 星期二
    {"weekday": "星期二", "time_slot": "1-2", "course": "移动通信 实验分组/第3组", "teacher": "", "weeks": "13", "location": "K403"},
    {"weekday": "星期二", "time_slot": "3-4", "course": "移动通信 实验分组/第3组", "teacher": "", "weeks": "13", "location": "K403"},
    {"weekday": "星期二", "time_slot": "3-4", "course": "形势与政策", "teacher": "华苗", "weeks": "4-5", "location": "H413"},
    {"weekday": "星期二", "time_slot": "7-8", "course": "通信网络", "teacher": "杨志华", "weeks": "3-15", "location": "G707"},
    {"weekday": "星期二", "time_slot": "9-10", "course": "扩频通信", "teacher": "曹斌", "weeks": "3-11", "location": "T3402"},
    # 星期三
    {"weekday": "星期三", "time_slot": "1-2", "course": "信息论与编码", "teacher": "汪洋", "weeks": "9-16", "location": "T5304"},
    {"weekday": "星期三", "time_slot": "7-8", "course": "移动通信", "teacher": "张霆廷", "weeks": "3-12", "location": "G707"},
    {"weekday": "星期三", "time_slot": "11-12", "course": "电子设计与实践", "teacher": "王立欣", "weeks": "2-7", "location": "H412"},
    # 星期四
    {"weekday": "星期四", "time_slot": "3-4", "course": "通信网络", "teacher": "杨志华", "weeks": "3-9,11-14", "location": "T3402"},
    {"weekday": "星期四", "time_slot": "5-6", "course": "移动通信 实验分组/第3组", "teacher": "", "weeks": "14", "location": "K403"},
    {"weekday": "星期四", "time_slot": "7-8", "course": "移动通信 实验分组/第3组", "teacher": "", "weeks": "14", "location": "K403"},
    {"weekday": "星期四", "time_slot": "9-10", "course": "扩频通信", "teacher": "曹斌", "weeks": "3-9", "location": "T3402"},
    # 星期日
    {"weekday": "星期日", "time_slot": "1-2", "course": "信息论与编码", "teacher": "汪洋", "weeks": "9,11", "location": "T5304"},
]

# 调用函数
cal = course_schedule_tools.create_events(courses)

# 生成ics文件
with open('course_schedule.ics', 'w', encoding='utf-8') as f:
    f.writelines(cal)

print("ICS文件已生成：course_schedule.ics")
