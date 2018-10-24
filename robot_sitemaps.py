# -*- coding: utf-8 -*-
import urllib.robotparser
import requests
from urllib.parse import urlparse
import codecs

class robot_sitemaps ():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Natnaree Asavaseri Agent',
            'From': 'natnaree.as@ku.th'
        }
        self.robot_request = None
        # self.sitemaps = []
        self.robots = self.get_robot_list('r')

    def robot_filter(self,url):
        robot = self.find_robot(url)
        if robot == None:
            return True
        try:
            if self.is_fetchable_robot(robot, url):
                return True
        except:
            return False
        # print('robot error')
        return False

    def write_link(self,url, op):
        if op == 's':
            file = 'lists_sitemap.txt'
            # print('write sitemap')
        elif op == 'r':
            file = 'lists_robots.txt'
        if url not in self.robots:
            self.robots.append(url)
            self.write_file(url, file)

    def write_file(self,text, file, permission='a'):
        f = codecs.open(file, permission, 'utf-8')
        f.write(text)
        f.write('\n')
        f.close()

    def is_robot(self,url):
        if self.is_root(url) == False:
            return False
        try:
            self.robot_request = requests.get(url + '/robots.txt', headers=self.headers, timeout = 2)
        except:
            self.robot_request = None
            return False
        if self.robot_request.status_code != 200:
            return False
        lines = self.robot_request.text.split('\n')
        if lines[0] == '<!DOCTYPE html>':
            # print('redirect bot')
            return False
        return True

    def is_fetchable_robot(self,robot, url):
        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(robot)
        rp.read()
        return rp.can_fetch("*", url)

    def is_same_site(self,url1, url2):
        o1 = urlparse(url1); o2 = urlparse(url2)
        site1 = o1.netloc; site2 = o2.netloc
        if (site1 == site2) or (site1 == ('www.' + site2)) or (('www.' + site1) == site2) or (site1 == ('www3.' + site2)) or (site1 == ('www3.' + site2)):
            return True
        return False

    def is_root(self,url):
        try:
            o = urlparse(url)
            if url[-1] == '/':
                url = url[:-1]
            if (o.netloc == url[7:]) or (o.netloc == url[8:]):
                return True
        except:
            pass
        return False

    def get_robot_list(self,op):
        robot = []
        if op == 'r':
            file = 'lists_robots.txt'
        if op == 's':
            file = 'lists_sitemap.txt'
        f = None
        try:
            f = open(file, "r")
            for line in f:
                robot.append(line[:-1])
        except:
            pass
        return robot

    def find_robot(self,url):
        # robots = self.get_robot_list(op='r')
        for robot in self.robots:
            if self.is_same_site(robot, url):
                return robot+'./robots.txt'
        if self.is_robot(url):
            # self.find_sitemap(url)
            self.robots.append(url)
            self.write_link(url, 'r')
            return url + '/robots.txt'
        return None

    def find_sitemap(self,url):
        # print('finding sitemap')
        sitemaps = []
        # try: 
        #     r = requests.get(url + '/robots.txt', headers=headers, timeout = 2)
        # # print(r.text)
        #     if r.status_code == 200:
        r = self.robot_request
        lines = r.text.split('\n')
        for i in range(len(lines)-1,-1,-1):
            line = lines[i]
            if line == '':
                continue
            if line[:8] != 'Sitemap:':
                break
            sitemaps.append(line[8:].strip())
                # print(line s[i])
        # sitemap_url = url + '/sitemap.xml'
        # # print(sitemap_url)
        # r = None
        # try: 
        #     r = requests.get(sitemap_url, headers=headers, timeout = 2)
        # except:
        #     return False
        # if len(sitemaps) > 0 or r.status_code == 200:
        #     # print(f'sitemap {url}')
        #     write_link(url, op='s')
        #     return True
        return False