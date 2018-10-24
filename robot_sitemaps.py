# -*- coding: utf-8 -*-
import urllib.robotparser
import requests
from urllib.parse import urlparse
import codecs

headers = {
    'User-Agent': 'Natnaree Asavaseri Agent',
    'From': 'natnaree.as@ku.th'
}

def robot_filter(url):
    robot = find_robot(url)
    if robot == None:
        return True
    try:
        if is_fetchable_robot(robot, url):
            return True
    except:
        return False
    # print('robot error')
    return False

def write_link(url, op):
    robots = []
    try: 
        robots = get_robot_list(op=op)
    except:
        robots = []
    if op == 's':
        file = 'lists_sitemap.txt'
        # print('write sitemap')
    elif op == 'r':
        file = 'lists_robots.txt'
    if url not in robots:
       write_file(url, file)

def write_file(text, file, permission='a'):
    f = codecs.open(file, permission, 'utf-8')
    f.write(text)
    f.write('\n')
    f.close()

def is_robot(url):
    if is_root(url) == False:
        return False
    try:
        r = requests.get(url + '/robots.txt', headers=headers, timeout = 2)
    except:
        return False

    if r.status_code != 200:
        return False
    lines = r.text.split('\n')
    if lines[0] == '<!DOCTYPE html>':
        # print('redirect bot')
        return False
    return True

def is_fetchable_robot(robot, url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robot)
    rp.read()
    return rp.can_fetch("*", url)

def is_same_site(url1, url2):
    o1 = urlparse(url1); o2 = urlparse(url2)
    site1 = o1.netloc; site2 = o2.netloc
    if (site1 == site2) or (site1 == ('www.' + site2)) or (('www.' + site1) == site2) or (site1 == ('www3.' + site2)) or (site1 == ('www3.' + site2)):
        return True
    return False

def is_root(url):
    try:
        o = urlparse(url)
        if url[-1] == '/':
            url = url[:-1]
        if (o.netloc == url[7:]) or (o.netloc == url[8:]):
            return True
    except:
        pass
    return False

def get_robot_list(op):
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

def find_robot(url):
    robots = get_robot_list(op='r')
    for robot in robots:
        if is_same_site(robot, url):
            return robot+'./robots.txt'
    if is_robot(url):
        find_sitemap(url)
        write_link(url, 'r')
        try:
            r = requests.get(url + '/robots.txt', headers=headers, timeout = 2)
            filename = urlparse(url).netloc.replace('.','-').replace('/','-')
            write_file(r.text, f'robots/{filename}', permission='w')
            # print(filename, r.text)
            return url + '/robots.txt'
        except:
            return None
    return None

def find_sitemap(url):
    # print('finding sitemap')
    sitemaps = []
    try: 
        r = requests.get(url + '/robots.txt', headers=headers, timeout = 2)
    # print(r.text)
        if r.status_code == 200:
            lines = r.text.split('\n')
            for i in range(len(lines)-1,-1,-1):
                line = lines[i]
                if line == '':
                    continue
                if line[:8] != 'Sitemap:':
                    break
                sitemaps.append(line[8:].strip())
            # print(line s[i])
    except:
        pass
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