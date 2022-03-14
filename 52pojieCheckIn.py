# -*- coding: utf8 -*-
import requests 
from bs4 import BeautifulSoup

cookie = ''  # 配置你的cookie
sckey = '' # 配置你的server酱SCKEY

def pushinfo(info,specific):
    headers={   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'ContentType': 'text/html'
    }
    requests.session().get("https://sc.ftqq.com/"+sckey+".send?text=" + info + "&desp=" + specific,headers=headers)

def main(*args):
    headers={
        'Cookie': htVC_2132_saltkey=wrPb8dk2; htVC_2132_lastvisit=1645752264; htVC_2132_auth=e176Hz%2FIDlsVIC9tMFBmbjt9sLF5Oi%2FAZn3BV1X1cSe6mDA%2BvuwsS6UrhdAHu6pZ7W8PqLaHWU5EC2xU8CrecFKgW804; KF4=U59f7W; htVC_2132_sid=0; htVC_2132_nofavfid=1; htVC_2132_ttask=1850980%7C20220314; htVC_2132_client_created=1647226406; htVC_2132_client_token=8228A4A18D28566405D25A1FE3F02D53; htVC_2132_connect_js_name=user_bind; htVC_2132_connect_js_params=YToxOntzOjQ6InR5cGUiO3M6OToibG9naW5iaW5kIjt9; htVC_2132_connect_login=1; htVC_2132_connect_is_bind=1; htVC_2132_connect_uin=8228A4A18D28566405D25A1FE3F02D53; htVC_2132_stats_qc_reg=3; wzws_sid=5bfaf7ced1e8e29afe6941c78c2496787aefd74439e271c6a9badf42f9735bc9f71d92a27bbe34ccd89dfdd2c1f4ce1f81d865c5f3e3b1e427b779fa30e59c196b188de074b983fafde738a86cb739c7; htVC_2132_visitedfid=13D5; htVC_2132_smile=1D1; htVC_2132_ignore_rate=1; Hm_lvt_46d556462595ed05e05f009cdafff31a=1645758048,1646638460,1647226049,1647226919; htVC_2132_seccodecS0=980763.8ccd3665719f796b4b; htVC_2132_secqaaqS0=980762.7f08694c40db114ed1; htVC_2132_checkpm=1; htVC_2132_lastcheckfeed=1850980%7C1647227271; htVC_2132_checkfollow=1; htVC_2132_ulastactivity=1647227280%7C0; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1647227285; htVC_2132_lastact=1647227282%09plugin.php%09,
        'ContentType':'text/html;charset=gbk'
    }
    requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=apply&id=2',headers=headers)
    a=requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=draw&id=2',headers=headers)
    b=BeautifulSoup(a.text,'html.parser')          
    c=b.find('div',id='messagetext').find('p').text

    if "您需要先登录才能继续本操作"  in c: 
        pushinfo("Cookie失效", c)
    elif "恭喜"  in c:
        pushinfo("吾爱破解签到成功",c)
    else:
        pushinfo("吾爱破解签到失败",c)
    print(c)


if __name__ == '__main__':
    main()
