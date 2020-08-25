# -*- coding: UTF-8 -*-
import requests


class Constrains(object):
    URL = 'https://api.live.bilibili.com/msg/send'
    MESSAGES = [ "校招已经开始，未注册简历的同学抓紧时间~"
        , "今晚有多轮抽奖活动，同学们要积极参加哦。"
        , "同学们有什么不懂的可以直接发弹幕提问"
        , "加入中兴奥利给！"
        , "中兴通讯，活好钱多！"
        , "这次一定！"
        , "在下玄功已成，投递简历，走向巅峰！"
        , "如果爱情有颜色的话，那一定是中兴蓝！"
        , "万水千山总是情，给我offer行不行！"
        , "立即推，加入中兴！"
        , "通讯技术哪家强，中国中兴第一香！"
        , "秋招千万步，选择中兴第一步。"
        , "生而为人，我很牛批。"
        , "秋招注意事项:猥琐发育，别浪。"
        , "祝大家都能获得心仪的offer。"
        , "妈妈，我要投简历去中兴！投！投最好的！"
        , "这个是不是财富密码"
        , "内推码ZTE374VZ0送给你们"]

    HEADER = {
        'Cookie': "粘贴内容",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36'}
