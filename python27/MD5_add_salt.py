#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

'''MD5_add_salt'''
def md5(str):
    md = hashlib.md5()
    md.update(str)
    md_5 = md.hexdigest()
    return md_5


def register(username, password):
    dict_client[username] = md5(password + username + 'the-Salt')


def login(username, password):
    if dict_client[username] == md5(password + username + 'the-Salt'):
        print "welcome %s" % username
    else:
        print "your keywords are wrong ! "


dict_client = {}
while 1:
    ty = raw_input("欢迎使用用户登录系统...存储用户数据请按1，登录请按2，退出请按3\n")
    if ty == '1':
        name_str = raw_input("请输出用户名字：\n")
        keywords_str = raw_input("请输入密码：\n")
        register(name_str, keywords_str)
        print 'MD5密码加密已完成...'
        print dict_client
    if ty == "2":
        name_str = raw_input("请输出用户名字：\n")
        keywords_str = raw_input("请输入密码：\n")
        login(name_str,keywords_str)
    if ty == "3":
        print 'BYE...'
        break
