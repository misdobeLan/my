# -*- encoding=utf8 -*-
__author__ = "lan"

from airtest.core.api import *

auto_setup(__file__)

'''藏宝图(次数，间隔时间)'''
def treasure_map(count,t):
    touch(Template(r"tpl1644036685390.png", record_pos=(0.47, 0.187), resolution=(2000, 1125)))
    touch(Template(r"tpl1644036700329.png", record_pos=(0.103, 0.084), resolution=(2000, 1125)))
    touch(Template(r"tpl1643605833061.png", record_pos=(0.356, 0.168), resolution=(2000, 1125)))

    while (count > 0):
        wait(Template(r"tpl1643710145907.png", record_pos=(0.355, 0.168), resolution=(2000, 1125)),timeout=t)
        touch(Template(r"tpl1643605833061.png", record_pos=(0.356, 0.168), resolution=(2000, 1125)))
        sleep(2)
        count = count - 1
        print (count)
     

'''抓鬼(次数，间隔时间)'''
def catch_ghost():
    touch(Template(r"tpl1644063202341.png", record_pos=(-0.226, -0.246), resolution=(2000, 1125)))
    touch(Template(r"tpl1644063254885.png", target_pos=9, record_pos=(-0.088, -0.184), resolution=(2000, 1125)))
    touch(Template(r"tpl1644063375533.png", record_pos=(0.349, -0.13), resolution=(2000, 1125)))
    sleep(20)
    '''
    touch(Template(r"tpl1644063510806.png", target_pos=4, record_pos=(0.486, -0.123), resolution=(2000, 1125)),times=2)
    sleep(1320.0)
    touch(Template(r"tpl1644065063826.png", record_pos=(0.083, 0.043), resolution=(2000, 1125)))
    touch(Template(r"tpl1644063375533.png", record_pos=(0.349, -0.13), resolution=(2000, 1125)))
    '''

'''运镖'''
def delivery(times,t):
    touch(Template(r"tpl1644063202341.png", record_pos=(-0.226, -0.246), resolution=(2000, 1125)))
    touch(Template(r"tpl1644414397730.png", target_pos=9, record_pos=(-0.056, -0.098), resolution=(2000, 1125)))
    while(times > 0): 
        sleep(5)
        wait(Template(r"tpl1644246691907.png", record_pos=(0.36, -0.025), resolution=(2000, 1125)),timeout=t)
        touch(Template(r"tpl1644246691907.png", record_pos=(0.36, -0.025), resolution=(2000, 1125)))
        touch(Template(r"tpl1644065063826.png", record_pos=(0.083, 0.043), resolution=(2000, 1125)))
        times = times -1
        print (times) 
    
    
#treasure_map(11,3600.0)
delivery(3,3600.0)
#catch_ghost()
