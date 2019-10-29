import time
from apscheduler.schedulers.blocking import BlockingScheduler
from test.test4 import load


def job():
  # readMsg = getReceiverInfo('mail_receiver.txt')
  # sendmail = SendMail(readMsg)
  # sendmail.sendEmail('report2019-10-22 14_35_55.html')
  load()
  print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

if __name__ == '__main__':
  # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
  scheduler = BlockingScheduler()
  # 采用阻塞的方式

  # 采用date的方式，在特定时间只执行一次
  scheduler.add_job(job, 'date', run_date='2019-10-22 17:58:00')
  scheduler.start()