# CourseSchedule
import HITsz students' course schedule into IOS calendar

***欢迎使用CourseSchedule***

***本项目可以实现哈工大（深圳）本研教学平台课表导入ios系统日程本***

方法一、自动导入：
    ---此方法目前仅测试本科生课表，若程序报错可以使用手动导入---
1.从本研教学平台下载xlsx格式的课表，移动进本文件夹中
2.确保环境内安装了openpyxl ics datetime这三个库。若没有安装，请在终端输入以下命令：
    pip instal openpyxl ics datetime
3.打开Auto_course_schedule_main.py文件并运行
4.运行程序后会生成一个calendar文件，后缀为.ics，将这个文件发送到ios系统的手机
5.先在日历中添加一个日历，以免污染系统自带的日历环境
6.手机接收文件后选择储存到文件，将文件拖拽进日历中。
具体操作方式：在文档中长按该文件并拖动，此时不要松手，用另一只手指退出文件界面，点开日历，此时松开拖动文件的手指。选择我们刚刚添加的日历，确认导入即可。

方法二、手动导入：
1.确保环境内安装了openpyxl ics datetime这三个库。若没有安装，请在终端输入以下命令：
    pip instal openpyxl ics datetime
2.打开course_schedule_main.py文件，将第6-25行代码按照你的课表进行修改然后运行
3.运行程序后会生成一个calendar文件，后缀为.ics，将这个文件发送到ios系统的手机
4.先在日历中添加一个日历，以免污染系统自带的日历环境
5.手机接收文件后选择储存到文件，将文件拖拽进日历中。
具体操作方式：在文档中长按该文件并拖动，此时不要松手，用另一只手指退出文件界面，点开日历，此时松开拖动文件的手指。选择我们刚刚添加的日历，确认导入即可。
