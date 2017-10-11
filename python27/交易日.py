# -*- coding: utf-8 -*-
__author__ = 'zjbao123'

from datetime import datetime, date, timedelta

nextday = datetime(2017, 9, 30)
endday = datetime(2018, 12, 31)
while nextday < endday:
    nextday = nextday + timedelta(days=1)
    if (nextday.weekday() != 5 and nextday.weekday() != 6):
        print "insert into `db_sys`.`tb_sys_trade_date` (`date`, `exchange_name`, `exchange_no`, `is_open`) VALUES (", nextday.strftime("%Y%m%d"), u", '中国金融期货交易所', '11', '1');"
    else:
        print "insert into `db_sys`.`tb_sys_trade_date` (`date`, `exchange_name`, `exchange_no`, `is_open`) VALUES (", nextday.strftime("%Y%m%d"), u", '中国金融期货交易所', '11', '2');"
