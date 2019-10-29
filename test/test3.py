#coding=utf8
from apscheduler.schedulers.blocking import BlockingScheduler
import time
# 输出时间
from framfriend.test_case.models.sendmail import getReceiverInfo, SendMail

def job():
    readMsg = getReceiverInfo('mail_receiver.txt')
    sendmail = SendMail(readMsg)
    sendmail.sendEmail('report2019-10-22 14_35_55.html')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
if __name__ == '__main__':
    # BlockingScheduler

    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', day_of_week='1-5', hour=6, minute=30)
    scheduler.start()