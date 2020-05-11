#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests
import time
import random

session = requests.Session()

def parse():
    url = "https://secure.louisvuitton.cn/ajaxsecure/getStockLevel.jsp?storeLang=zhs-cn&pageType=storelocator_section&skuIdList=1A87EU,1A87EV,1A87EW,1A87EX,1A87EY,1A87EZ,1A87F0,1A87F1,1A87F2,1A87F3,1A87F4,1A87F5,1A87F6,1A87F8,1A87F9,1A87EE,1A87EF,1A87EG,1A87EH,1A87EI,1A87EJ,1A87EK,1A87EL,1A87EM,1A87EN,1A87EO,1A87EP,1A87EQ,1A87ES&null&_=1589083810744"
    headers = {
        'authority': 'secure.louisvuitton.cn',
        'method':'GET',
        'path':'/ajaxsecure/getStockLevel.jsp?storeLang=zhs-cn&pageType=storelocator_section&skuIdList=1A87EU,1A87EV,1A87EW,1A87EX,1A87EY,1A87EZ,1A87F0,1A87F1,1A87F2,1A87F3,1A87F4,1A87F5,1A87F6,1A87F8,1A87F9,1A87EE,1A87EF,1A87EG,1A87EH,1A87EI,1A87EJ,1A87EK,1A87EL,1A87EM,1A87EN,1A87EO,1A87EP,1A87EQ,1A87ES&null&_=1589083810744',
        'scheme':'https',
        'accept':'*/*',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9',
        # 'cookie':'lvbmwe1=979DDBDE111D501A2831853477A241D2; lvbmwe2=67F605C6350C4428C460EE23C8DC507B; _qubitTracker=8hb4wbm70w0-0k7vk8hjg-krtx0tc; qb_generic=:XDnVurK:.louisvuitton.cn; _cs_c=1; _gcl_au=1.1.1436033953.1584429743; kameleoonVisitorCode=_js_jyjf9agt7226v0dv; bm_sz=4616F1FCEFE9B29056CFECB11FA08E57~YAAQHB7eOrnyqdJxAQAAa6ax/AcV2qax0F+IJkx10Jzxv3u8bxT6BjvvF9QCpg5YThgr4V2POG6E1XPqCJVDwJBJcFQpVe73Vd84Ja+MFlFV5ZkefxBBaFUjrB7f0qDxf4Vv08247Zoqu94c6LJVotsEPJJp1u6wxEGpNZMKsUejh6E/uJBvsLAonvzXwP8NXVeyhi0=; bm_mi=DD9D79B8A32427EB7E2403294EABD349~AmFobxujnplKKHQj2VtBXI8zPjEe/n66KEV8si2eIEq4Gh+qPVl06vcSThWQlx9WIbbonT/3rBMwuf2KBOt3AjIe3B6vvLTw3GKHYoK4F+ozrJLt0sACEpWWGrhzolO/wKDGSApsPuI6VnjlAEUPJ3Hbrru8zzeaY7gjTdw5+np01YbvcWOhrxjmVV/e2GQvu5q4Vnf7ifenT1jfmCBu3m/tukL1hzqgxJY2UCRkXEA8nAt3Jh1tqDZZG1nByFAmiv0KXmmfKdcCuKLlYJ1X+DP/dEBXX9yEDugUOPqJ630=; ak_bmsc=A339CCED041EBB38703445D0BDE2D9E73ADE1E1CBC5B00004179B75E0CBF8A40~plKDaewHqAaGpEkVYpQwM1ayg6Z+MzkID7VSb2hVXaszT5qptRlua3vTVPp30B1UJWMO4jXSOaCpigT8D4RD7YMFllRusxdWeUAKK3fKhhqww3+/OHGcysyjJZOOn1yRdFd7GHKdWXTKuKd2WoDjcvr43FqB6MlJsMmTM2vuYZEeex3/BwIeYBWu+/MDY6UN+rWJS38W/lx6s82YLJ20L1R2UkUab7q8WVy/QlPug+AIXnOZpGJ0mSMIXq5i9wKyAi; _ga=GA1.2.88020053.1589082562; _gid=GA1.2.126329821.1589082562; order_CN="H4sIAAAAAAAAAKtWyi9KSS1SslLKK8s3N7UwMDY2s1SqBQDu5iFXFwAAAA=="; anonymous_session=false; orderSize_CN=2; s_cc=true; JSESSIONID=fOUcbzcfKiGZP9u67X94n6yl.front11-prc; ATG_SESSION_ID=fOUcbzcfKiGZP9u67X94n6yl.front11-prc; lvbmwe2=D8BF50A4E93BFC48E02CF7ACA363FA1B; _dynSessConf=8538836923219439227; JSESSIONID=QdOh9PRY0if4CXzLpLDgplBz.front41-prc; SGID=sb.springboot41-prc; Qs_lvt_187854=1584429202%2C1589082562%2C1589083802; Hm_lvt_70ef235947285936a07191ef669a6813=1589082563,1589083545,1589083803; AMCVS_A69F5C6655799DC57F000101%40AdobeOrg=1; AMCV_A69F5C6655799DC57F000101%40AdobeOrg=-2017484664%7CMCIDTS%7C18393%7CMCMID%7C83817385992757700752496287171482804876%7CMCAAMLH-1589688605%7C11%7CMCAAMB-1589688605%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1589083744.846%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.3.0; s_sq=%5B%5BB%5D%5D; OPTOUTMULTI=0:0%7Cc1:0%7Cc2:0%7Cc4:0%7Cc3:0; Hm_lpvt_70ef235947285936a07191ef669a6813=1589083807; Qs_pv_187854=423684455387728500%2C343645826456109060%2C3300365248676331000%2C3743325596736426500%2C2820487524273044500; _cs_id=cf414b58-acfc-a7e5-85ee-872a345553a5.1584429212.2.1589083807.1589082563.1.1618593212887.Lax.0; _cs_s=12.1; lvbmwe1=979DDBDE111D501A2831853477A241D2; _abck=0BA073FC7AA7C0CB78E3DB4E66FD9376~-1~YAAQNx7eOkbYRZlxAQAAg6nG/ANG1yrlwyzQPTdxYLif5f/eYhHfRqunk+/RDFWHOWmSuHyVBQTeMQNO2Twv6lmJ9yu+kZEIUnMjWe2EcN0ClDsTLA2n/7pcdJ8FcP+H6CVLm4bFmfRty2gdnJ189S/yBuYpns1vstyjCWv5i8h/XOg0mb9Des8oKLh4GreK/RMRlkq5Ljv0q5Gi8riFfYbajiisJJe809I6A1yMizIemnivyIN9dtraxYQIII7GeLY08T+T2Sr+VSbdtAhFUk4REcX5et8r92NOqJBJxbUl6dlJ3EuBDK4oIV9Wtbaa92IBo1Qy+T0OkhwT~0~-1~-1; bm_sv=2A33D98B206EDD2C0B9CDEBF25C857E9~qXifEUbnBMcv8wB54VoP+7FS5DqIRJ+Kj4ayfIFhOuf+JD8qll1/4SLcwkTTh4DwBYmX0gXszjqQW85BJL9444W+7dL9ddFBxFsbhVqcLjLzVYR8rgE4fn6Dhoi6e1rq0ZkXNE71vuqUayMQNQyhyY4YauQiMDnnzdQsmZWGG7E=; utag_main=v_id:0170e756eb0f000b68ff5c964b190306e00fc06600978$_sn:2$_se:46$_ss:0$_st:1589085610938$vapi_domain:louisvuitton.cn$dc_visit:2$ses_id:1589082561169%3Bexp-session$_pn:12%3Bexp-session$dc_event:45%3Bexp-session$dc_region:eu-central-1%3Bexp-session; qb_permanent=8hb4wbm70w0-0k7vk8hjg-krtx0tc:18:4:2:4:0::0:1:0:BecHiP:Bet36j:A::::117.83.123.195:suzhou:39132:china:CN:31.31:120.61:suzhou:156078:jiangsu%20sheng:35603:migrated|1589082561406:EYai==G=CCFu=Ek&Em5V==G=CF7t=Hm::XH8xqyM:XH8xo2q:0:0:0::0:0:.louisvuitton.cn:0; qb_session=12:1:50:EYai=F&Em5V=G:0:XH8s5to:0:0:0:0:.louisvuitton.cn',
        'cookie':'lvbmwe1=D689D074677818C6B922D5E1A289166D; lvbmwe2=67F605C6350C4428C460EE23C8DC507B; _qubitTracker=8hb4wbm70w0-0k7vk8hjg-krtx0tc; qb_generic=:XDnVurK:.louisvuitton.cn; _cs_c=1; _gcl_au=1.1.1436033953.1584429743; kameleoonVisitorCode=_js_jyjf9agt7226v0dv; bm_sz=4616F1FCEFE9B29056CFECB11FA08E57~YAAQHB7eOrnyqdJxAQAAa6ax/AcV2qax0F+IJkx10Jzxv3u8bxT6BjvvF9QCpg5YThgr4V2POG6E1XPqCJVDwJBJcFQpVe73Vd84Ja+MFlFV5ZkefxBBaFUjrB7f0qDxf4Vv08247Zoqu94c6LJVotsEPJJp1u6wxEGpNZMKsUejh6E/uJBvsLAonvzXwP8NXVeyhi0=; bm_mi=DD9D79B8A32427EB7E2403294EABD349~AmFobxujnplKKHQj2VtBXI8zPjEe/n66KEV8si2eIEq4Gh+qPVl06vcSThWQlx9WIbbonT/3rBMwuf2KBOt3AjIe3B6vvLTw3GKHYoK4F+ozrJLt0sACEpWWGrhzolO/wKDGSApsPuI6VnjlAEUPJ3Hbrru8zzeaY7gjTdw5+np01YbvcWOhrxjmVV/e2GQvu5q4Vnf7ifenT1jfmCBu3m/tukL1hzqgxJY2UCRkXEA8nAt3Jh1tqDZZG1nByFAmiv0KXmmfKdcCuKLlYJ1X+DP/dEBXX9yEDugUOPqJ630=; ak_bmsc=A339CCED041EBB38703445D0BDE2D9E73ADE1E1CBC5B00004179B75E0CBF8A40~plKDaewHqAaGpEkVYpQwM1ayg6Z+MzkID7VSb2hVXaszT5qptRlua3vTVPp30B1UJWMO4jXSOaCpigT8D4RD7YMFllRusxdWeUAKK3fKhhqww3+/OHGcysyjJZOOn1yRdFd7GHKdWXTKuKd2WoDjcvr43FqB6MlJsMmTM2vuYZEeex3/BwIeYBWu+/MDY6UN+rWJS38W/lx6s82YLJ20L1R2UkUab7q8WVy/QlPug+AIXnOZpGJ0mSMIXq5i9wKyAi; _ga=GA1.2.88020053.1589082562; _gid=GA1.2.126329821.1589082562; order_CN="H4sIAAAAAAAAAKtWyi9KSS1SslLKK8s3N7UwMDY2s1SqBQDu5iFXFwAAAA=="; orderSize_CN=2; s_cc=true; _dynSessConf=8538836923219439227; JSESSIONID=QdOh9PRY0if4CXzLpLDgplBz.front41-prc; SGID=sb.springboot41-prc; Qs_lvt_187854=1584429202%2C1589082562%2C1589083802; Hm_lvt_70ef235947285936a07191ef669a6813=1589082563,1589083545,1589083803; AMCVS_A69F5C6655799DC57F000101%40AdobeOrg=1; AMCV_A69F5C6655799DC57F000101%40AdobeOrg=-2017484664%7CMCIDTS%7C18393%7CMCMID%7C83817385992757700752496287171482804876%7CMCAAMLH-1589688605%7C11%7CMCAAMB-1589688605%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1589083744.846%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.3.0; s_sq=%5B%5BB%5D%5D; JSESSIONID=wsYdhsZJ2W0zXRqm64VRqHIG.front11-prc; ATG_SESSION_ID=wsYdhsZJ2W0zXRqm64VRqHIG.front11-prc; lvbmwe1=D689D074677818C6B922D5E1A289166D; lvbmwe2=D8BF50A4E93BFC48E02CF7ACA363FA1B; OPTOUTMULTI=0:0%7Cc1:0%7Cc2:0%7Cc4:0%7Cc3:0; Qs_pv_187854=3300365248676331000%2C3743325596736426500%2C2820487524273044500%2C545700125408399700%2C3348515229361200600; Hm_lpvt_70ef235947285936a07191ef669a6813=1589084662; _cs_id=cf414b58-acfc-a7e5-85ee-872a345553a5.1584429212.2.1589084663.1589082563.1.1618593212887.Lax.0; _cs_s=14.1; qb_session=13:1:61:EYai=H&Em5V=H:0:XH8s5to:0:0:0:0:.louisvuitton.cn; _abck=0BA073FC7AA7C0CB78E3DB4E66FD9376~0~YAAQHB7eOggTqtJxAQAAuX7U/APy5rebnCOSlH1TSMIskSxTgsrMXo8Ufg7b3VbTfYgzJzu5r2CtWYbb1nOZC1nUV122Srl6u7OLFmMkQV1CwYwrqxRyVdXyoXV4SGSR49wnSc6DRUr9T4Ik8Hxz2lLQw3KiyA9iu+wh3FF7N5knu8EyWY2tGUovbNBdv3mcflfnMKbNKwbSByAm4psxCtFrVbOqa/ymRkXyfUB1teNd9SxgXClZ6skgWmESL5/5kUV+JbyrkbGPBuzwHB02GEQGu/3ySn3ELu7BlVskzkEWdFVP76Ekgt6yJDGKRIC18gzoIGfRwPQ2Jece~-1~1-PAoOELhqQQ-10000-100-3000-1||1-DNsXhWnOHW-2250-100-3000-2||~-1; bm_sv=2A33D98B206EDD2C0B9CDEBF25C857E9~qXifEUbnBMcv8wB54VoP+7FS5DqIRJ+Kj4ayfIFhOuf+JD8qll1/4SLcwkTTh4DwBYmX0gXszjqQW85BJL9444W+7dL9ddFBxFsbhVqcLjIla71ymPq402FSdkdbvvgUDpUFIlFNP9Gk2FcvRiGp/B0IbwMUue0PoFXF5UogOtg=; qb_permanent=8hb4wbm70w0-0k7vk8hjg-krtx0tc:19:5:2:4:0::0:1:0:BecHiP:Bet4H3:A::::117.83.123.195:suzhou:39132:china:CN:31.31:120.61:suzhou:156078:jiangsu%20sheng:35603:migrated|1589082561406:EYai==I=CCFu=Ek&Em5V==H=CF7t=Hm::XH81Ifv:XH8xo2q:0:0:0::0:0:.louisvuitton.cn:0; utag_main=v_id:0170e756eb0f000b68ff5c964b190306e00fc06600978$_sn:2$_se:54$_ss:0$_st:1589086519188$vapi_domain:louisvuitton.cn$dc_visit:2$ses_id:1589082561169%3Bexp-session$_pn:14%3Bexp-session$dc_event:53%3Bexp-session$dc_region:eu-central-1%3Bexp-session',
        'origin':'https://www.louisvuitton.cn',
        'referer':'https://www.louisvuitton.cn/zhs-cn/products/stellar-sneaker-nvprod2240005v',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-site',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
    }
    response = session.get(url,headers=headers)
    print(response.json())
# parse()

while True:
    parse()
    time.sleep(random.randint(1,2))
