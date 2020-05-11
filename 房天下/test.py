#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests

headers = {
    'authority': 'sh.newhouse.fang.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'referer': 'https://sh.newhouse.fang.com/house/s/',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': 'global_cookie=j4xwsbg1sxqnunjo5vn24hwsk17k60ig3s6; newhouse_user_guid=404FB4C8-45BD-7D33-B283-B41C0047503A; vh_newhouse=1_1580375360_768%5B%3A%7C%40%7C%3A%5D70b133858d834f3c225364b47dd05681; Integrateactivity=notincludemc; city=sh; global_wapandm_cookie=got7mgfzz4081xlv6jgsygh9q1wk9qlk2k3; __utmc=147393320; new_loginid=69851791; token=db84836b97674723a687a461d091f308; sfut=956111C681CC38670773955B3CE408006061C773CD01127E5C802091AACB61DCD610AD153A5887C6B8B45746F7AB52C2F6866A09246475E3AE6A86F8DE10A41717983B2D88187591BFB8E9C4C301D99053AD72C420A9C2FF70ED047838604412; g_sourcepage=xf_lp%5Elb_pc; __utma=147393320.138136687.1580375081.1588923043.1588928208.5; __utmz=147393320.1588928208.5.4.utmcsr=sh.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; __utmt_t3=1; __utmt_t4=1; new_loginid=69851791; login_username=fnewhous72484383; __utmb=147393320.10.10.1588928208; unique_cookie=U_ye5srgbladbv1iavbbmc36edq1jk9xvr526*17',
}

params = (
    ('ctm', '1.sh.xf_search.page.2'),
)

response = requests.get('https://sh.newhouse.fang.com/house/s/b92/', headers=headers, params=params)
# response.encoding="gbk"
response.encoding=response.apparent_encoding
print(response.text)
