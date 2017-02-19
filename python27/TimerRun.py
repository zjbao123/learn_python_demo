# -*- coding: utf-8 -*-
import os
import platform

import datetime

__author__ = 'zjbao123'
def run_task():
    os_platfrom = platform.platform()
    if os_platfrom.startswith('Darwin'):

        print'this is mac os system'


    elif os_platfrom.startswith('Window'):

        print'this is win system'

def TimerRun(sched_Timer):
    flag = 0
    while(True):
        now = datetime.datetime.now()
        if now == sched_Timer:
            run_task()
            flag = 1
        else:
            if flag ==1 :
                sched_Timer = sched_Timer + datetime.timedelta(seconds=1) #用以设置延迟时间
                flag = 0

if __name__ =='__main__':
    sched_Timer = datetime.datetime(2017,2,17,13,52,00)
    print '该程序将于{0}运行...'.format(sched_Timer)
    TimerRun(sched_Timer)