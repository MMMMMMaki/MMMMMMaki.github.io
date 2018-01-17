# -*- coding: utf-8 -*-

from splinter.browser import Browser
from time import sleep

class builder(object):

    order = 33
    def __init__(self):
        self.builder_url = "http://192.168.1.110:8000/"
        self.a_href = "/jobmng/dojob/"+str(self.order)

    def start(self):
        self.driver = Browser()
        self.driver.visit(self.builder_url)

        while self.driver.url == self.builder_url:
            self.driver.reload()
            try:
                sleep(1)
                self.driver.find_by_css("a[href='"+self.a_href+"']").click()
                print("正在构建。。")
            except Exception as a :
                print("其他项目在构建")
                sleep(10)
                continue


if __name__ == '__main__':
	build = builder()
	build.start()

