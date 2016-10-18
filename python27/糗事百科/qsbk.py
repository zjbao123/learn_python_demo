#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjbao123'
import urllib2
import re
import time

'''
simple spider of QiuShiBaiKe
'''


# 糗事百科爬虫
class QiuShiBaiKe:
    def __init__(self):
        # 初始化方法，定义一些变量
        self.pageIndex = 1

        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        # 存放段子的变量，每一个元素是每一页所包含的段子
        self.stories = []
        # 存放程序是否继续运行的变量
        self.enable = False

    # 连接方法，传入某一页的索引获得页面代码
    def link(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/8hr/page/' + str(pageIndex)
            # 构建request请求
            request = urllib2.Request(url, headers=self.headers)
            # 接收urlopen（）的响应
            response = urllib2.urlopen(request)
            # 获取网页内容并转为UTF-8码
            pageCode = response.read().decode('utf-8')
            return pageCode
        # 捕获错误
        except urllib2.URLError, e:
            if (hasattr(e, 'code')):
                print u"连接糗事百科失败，错误代码:" + e.code
            if (hasattr(e, 'reason')):
                print u"连接糗事百科失败，错误原因:" + e.reason

    # 对获取网页的内容进行处理，返回段子的发布者，内容，点赞数和评论数
    def getPageItem(self, pageIndex):
        # 调用link() 来得到网页内容
        pageCode = self.link(pageIndex)
        if not pageCode:
            print u'阿哦...加载失败...请调试...'
            return None
        # 正则判断所需内容
        pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?"content">' +
                             '.*?span>(.*?)</span>(.*?)number">(.*?)</.*?number">(.*?)</.',
                             re.S)
        # 返回匹配列表
        items = pattern.findall(pageCode)
        # 用来存储每页的段子们
        pageStories = []

        for item in items:
            # 判断是否有图，过滤有图的段子
            haveImg = re.search("img", item[2])
            if not haveImg:
                text = item[1].replace('<br/>', '\n')
                pageStories.append([item[0].strip(), text.strip(), item[3].strip(), item[4].strip()])
        return pageStories

    # 加载并提取网页内容，加入到stories列表中
    def loadPage(self):
        if self.enable == True:
            # 如果页码少于2页，则加载一页内容至stories列表
            if len(self.stories) < 2:
                pageStorise = self.getPageItem(self.pageIndex)
                if pageStorise:
                    self.stories.append(pageStorise)
                    # 获取完之后页码索引加一，表示下次读取的页数
                    self.pageIndex += 1

    # 读取段子们中的一个
    def getOneStory(self, pageStories, page):
        # 遍历一页的段子
        for story in pageStories:
            # 加载页面
            self.loadPage()
            print u"第%d页\t发布人:%s\t赞:%s\t评论:%s\n\n%s\n----------------\n" % (
                page, story[0], story[2], story[3], story[1])
            # 等待用户输入
            intput = raw_input()
            # 如果输入Q则程序结束
            if intput == "Q":
                self.enable = False
                print u'哦不，狠心的人儿啊...'
                time.sleep(2)
                return

    # 开始方法
    def start(self):

        print u'----------------\n这是一个超级酷炫的糗百段子库！\n\n按回车查看新段子，按Q退出\n\n新鲜的段子马上就来！\n----------------\n'
        # 使变量为True，程序可以正常运行
        self.enable = True
        # 先加载一页内容
        self.loadPage()
        # 用来记录当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                # 从全局list中获取一页的段子
                pageStories = self.stories[0]
                # 当前读到的页数加一
                nowPage += 1
                # 删除第一个元素，该页已经取出
                del self.stories[0]
                # 遍历输出该页段子
                self.getOneStory(pageStories, nowPage)


spider = QiuShiBaiKe()
spider.start()
