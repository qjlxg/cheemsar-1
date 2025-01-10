# w1770946466 北慕白  https://github.com/w1770946466/Auto_proxy
# v2ray_collecto
# coding=utf-8
import base64
import requests
import re
import time
import os
import threading
from tqdm import tqdm
import random, string
import datetime
from time import sleep
import chardet

#试用机场链接
home_urls =(



'https://m33.spwvpn.com',
'https://m4y2z.no-mad-world.club',
'https://magicae.pics',
'https://maho.chipsfuck.fish',
'https://marketepicpanel.marketepic.ir:2087',
'https://mc.jiedianxielou.workers.dev',
'https://mercedes1208.xn--3iq226gfdb94q.com',
'https://miaomiao.xn--7rs48z0nlr6hc8cqz4a.com',
'https://mlshu.xyz',
'https://mm.hnekoo.top',
'https://mo.mojieurl.com',
'https://mochizuki.top',
'https://mojie.app',
'https://mojie.co',
'https://mojie.link',
'https://mojie0201.xn--8stx8olrwkucjq3b.com',
'https://mro5n.no-mad-world.club',
'https://multikeys.outlinekeys.net',
'https://music.easygourl.xyz',
'https://my.335570.xyz',
'https://my.cat66.lol',
'https://my.mingri.icu',
'https://mydy.xlm.plus',
'https://myko.buzz',
'https://mymy.lanyanyun.co',
'https://mysub.cc',
'https://mytoken.huyun.nl',
'https://mytoken-1.huyun.nl',
'https://myu.best',
'https://n3.leensasub.net',
'https://nachoneko.cn',
'https://nanbei.cloud',
'https://nano.nachoneko.cn',
'https://needay.net',
'https://needay.xyz',
'https://neko.hnekocloud.top',
'https://neko2.hnekocloud.top',
'https://neo.facal.one',
'https://neolink.nkkc.one',
'https://net.17181922.xyz',
'https://new.xn--pbt38zg4v.com',
'https://ng.69hub.cc',
'https://ng.s2fjeyeeyafe.bond',
'https://nginx-proxy-123.69hub.cc',
'https://niaodi.top',
'https://ninjasub.com',
'https://nmsubs.com',
'https://nn0310.xn--8stx8olrwkucjq3b.com',
'https://node.666666222.xyz',
'https://node.yifang02.men',
'https://node.zasublinkv1.com',
'https://nogin.djjc.cfd',
'https://notls.11111111.eu.org',
'https://nsm5o.no-mad-world.club',
'https://nuonuonet.uk',
'https://nxiyy.com',
'https://o7pl1.no-mad-world.club',
'https://oiiccdn.yydsii.com',
'https://okztwo.com',
'https://on1vejas4m6z.w7yxefcx0i11.click',
'https://oss.pithecia.com',
'https://oss-alibabaclod.fsddsadsavgroup.top',
'https://outlinekeysrobotgb.outlinekeys.net',
'https://owo.o00o.ooo',
'https://p0.mahilobia.org',
'https://panel.kernel-mirrors.org:2053',
'https://parsroute.net',
'https://pavo.eu.org',
'https://pdda.me',
'https://pincht.sbs',
'https://platform.djjc.cfd',
'https://post.jianjiaoyun.link',
'https://pp.fra-shop.ir:8443',
'https://pp.hnekoo.top',
'https://pqjc.site',
'https://pro.76898102.xyz',
'https://prob.xn--l9qyaz082a.cn',
'https://proc.xn--l9qyaz082a.cn',
'https://protal.xfxun.com',
'https://psce.pw',
'https://qianggewangluo.cc',
'https://qifei.today.elementfx.com',
'https://qingchayun.icu',
'https://qkt83qnp2yuj.subconnect.org',
'https://qqqqqqqqqqqqqqqqqqqq.n3el78lqhbc5yhb2.xyz',
'https://QTjDQsor6e7D.configbit.com',
'https://qwe.097482.xyz',
'https://qwerzfdsfgrtds.mejd.cn',
'https://qyoo.aibvs.cn',
'https://red.colacloud.free.hr',
'https://repzt3P1yq.qinyues4.cc',
'https://rgergergergerg6555.saojc.xyz',
'https://rockvpn.4bmg9.online',
'https://rss.biteb-sub.com',
'https://rss.paoluz.xyz',
'https://rss2024.jkl-sub.com',
'https://rss202407.mugua-sub.com',
'https://rsslinghun1.xyz',
'https://rss-node.com',
'https://rxxqa.no-mad-world.club',
'https://s.33y.run',
'https://s.feisucloud.xyz',
'https://s.hajimi.icu',
'https://s.jiasu01.vip',
'https://s.jockerchief.online',
'https://s.kalaa.me',
'https://s.kingarthor.online',
'https://s.princeseed.online',
'https://s.qzsub.live',
'https://s.suying666.info',
'https://s.youyun666.site',
'https://s1.bnpublicsub.com',
'https://s1.bnsubservdom.com',
'https://s1.byte16.com',
'https://s1.byte33.com',
'https://s1.daxun-link.com:8888',
'https://s1.iajsy.lol',
'https://s2.sub.gfw.gg',
'https://s6.ssysub1.xyz',
'https://s7.sub.gfw.gg',
'https://sakuracat1203.xn--3iq226gfdb94q.com',
'https://sanguayun.jiumaojiu.net',
'https://sb.swiftnet.cloud',
'https://sbs.fastfly.life:21600',
'https://sbsqwzfgh.santoku.cn',
'https://sdgvps.com',
'https://server.fylink.link',
'https://sinhvien4g.com',
'https://sinsocloud.top',
'https://spr.278986.xyz',
'https://ss.81dlg.com',
'https://ss.cft.my',
'https://ss.hxcq.cc',
'https://ss.suyunti.cc',
'https://ssvpn.org',
'https://starlinkcloud.club',
'https://starlinkcloud.xyz',
'https://st-sub.fly.dev',
'https://study.jaycloud11111.top',
'https://study1.v1999.sbs',
'https://subtest.mojc.xyz',
'https://subthree.996yyds.xyz',
'https://sulian.cc',
'https://sulian.life',
'https://sux.lol',
'https://svip.365cloud.me',
'https://syyn.ianong.cn',
'https://syyn.xyz',
'https://syynweb.shop',
'https://syynweb.xyz',
'https://taoyuanjiasu.com',
'https://texon.io',
'https://tg.z-cloud.dynv6.net',
'https://tghjjcp.bestcloud.lol',
'https://thepoint1.free886.site',
'https://tjjd.yzyx1.v6.army',
'https://tokenapi.fbcloud.lol',
'https://too.st',
'https://toysforyou.top',
'https://trojanfree-76s.pages.dev',
'https://ttc01.xyz',
'https://tudou.igken.com',
'https://tugeda.xyz',
'https://turbooserver.xyz',
'https://tuzi226.top',
'https://tv.modemhub.work',
'https://tz.vfkum.website',
'https://u4dqz2t0x576.syynweb.shop',
'https://update.dotusub.xyz',
'https://update.glados-config.com',
'https://url.409648.xyz',
'https://url.funhub.cc',
'https://url.mtdwoodwork.com',
'https://us.freecat.cloud',
'https://user.1vpn.sbs',
'https://user.wolf-iran.ir',
'https://user192.dukadi.one',
'https://user413.dukadi.one',
'https://user9125.eyudy.one',
'https://v.spwvpn.com',
'https://v1.mk',
'https://v2.545155.xyz',
'https://v2.bgp.dedyn.io',
'https://v2.ixlmo.com',
'https://v2.udid8.com',
'https://vase.bengalj.com',
'https://vip.365cloud.me',
'https://vip.kernel-mirrors.org',
'https://vip.sgjc.top',
'https://vips.lol',
'https://vodfavor.top',
'https://vot.278986.xyz',
'https://vot.981176.xyz',
'https://vpn.linuxdo.pro',
'https://vpn6688.com',
'https://vt.louwangzhiyu.xyz',
'https://vtwoc1.top',
'https://vtwoc3.top',
'https://vyyy.vyunyunnode.top',
 'https://dash2.moonriver.one',
'https://mdss.cloud',
 'http://66ds.dishujichang.xyz',
'http://6b.zhunchuanpb.com',
'http://6bsub.zhunchuanpb.com',
'http://8.134.181.161:12580',
'http://81.90.147.182:2096',
'http://91.107.179.40:443',
'http://95.182.98.33:2096',
'http://dydz.xn--mesv8bx6xtx3b.com:2006',
'http://e8a580bd3a51b6050aabd8919a17d106.52pokemon.top',
'http://n15uvht4r659107p.eastasia.cloudapp.azure.com',
'http://on1vejas4m6z.w7yxefcx0i11.click',
'http://panda.xn--i8sx78aisa52z.com',
'http://panda.xn--lbrx91akmhm30c.com',
'http://sub.sub.sub.subsub123456789.com',
'http://sub.xn--54qu5qypuo1o.xn--fiqs8s',
'http://sub2086.fnyune.shop:2086',
'https://0415.chun-auto-one.xyz',
'https://069059b7ef-1ytapi01.1ytsub.com',
'https://0d2th.no-mad-world.club',
'https://0mv.top',
'https://1.bethebest.eu.org',
'https://1.mjjclub.top',
'https://1.xn--xc3ao8r.top',
'https://10th.sub-airport.com',
'https://123x6y9z.d01olikp.thesyeec7l60ouav1lz0tesk.top',
'https://15212712-20f5-40a5-b9aa-8363e0130171.ee137666-1e0a-46db-bbd6-cc18f9841234.accesscam.org',
'https://16th.sub-airport.com',
'https://20240802.canadapost-vip.com',
'https://20240913.sux.lol',
'https://2381bfde-8c93-4701-8f14-24f071067a1a.nginx24bit.xyz',
'https://3.cundu.eu.org',
'https://30178aeb-8299-045d-fb67-ae12ce73dd2c.buou.lol',
'https://30388d70-6f5c-4d7c-8daa-9d3df7c5c526.9150e878-8296-4798-a172-c3fe66b8dee5.ddnsgeek.com',
'https://3093492f6b2332f8server.lycoris.one',
'https://353g78qgfq.surfcat.store',
'https://38.181.25.67',
'https://3dxre.no-mad-world.club',
'https://3ra4214.tjsd.site',
'https://41be350f-5079-4195-8329-f6fa25f9906a.com',
'https://cm-sub.pz.pe',
'https://subscribe.fastsocks.xyz',
'https://damp-mode-4de5.6006101.workers.dev',
'https://c3.notesync.org',
'https://088ea81a-3547-85e0-4af6-dfcb3c6674aa.372372.xyz',
'https://dy.pmy666.xyz',
'https://xn--mesz9ptugxg.com',
'https://sub123.71345.xyz',
'https://bujidao.cc',
'https://ymzx.jiedianxielou.workers.dev',
'https://linke.phantasy.life',
'https://kcsub.vip',
'http://xby2.op-house.top:2096',
'https://zero.76898102.xyz',
'https://subscribe.seyyedmt.blog',
'https://52daishu.uk',
'https://1321078938-11mmjf3qkb-hk.scf.tencentcs.com',
'https://sub.cokecloud.world',
'https://get.biu001.xyz',
'https://getinfo.bigwatermelon.org',
'https://dbjc.xyz',
'https://b3b0549e-160e-495a-a528-cccf5148bc48.372372.xyz',
'https://088EA81A-3547-85E0-4AF6-DFCB3C6674AA.372372.xyz',
'https://sub.htg8866.us.kg',
'https://sub.miaolianyun.vip',
'https://www.066664.xyz',
'https://d7b12d59-21aa-9561-087f-89c834ac7fe8.372372.xyz',
'https://doata.net',
'https://sub.cjcloud.cc',
'https://a.aikllc.tech',
'https://aini.200566.xyz',
'https://yuxi.fanqiev2.work',
'https://b.bbydy.org',
'https://cat.ikkt.cn',
'https://www.laoniu49.top',
'https://zjsub.gitpub.top',










 )
#文件路径
update_path = "./sub/"
#所有的clash订阅链接
end_list_clash = []
#所有的v2ray订阅链接
end_list_v2ray = []
#所有的节点明文信息
end_bas64 = []
#获得格式化后的链接
new_list = []
#永久订阅
e_sub = ['']
#频道
urls =[]
#线程池
threads = []
#机场链接
plane_sub = ['']
#机场试用链接
try_sub = []
#获取频道订阅的个数
sub_n = -25
#试用节点明文
end_try = []

#获取群组聊天中的HTTP链接
def get_channel_http(url):
    headers = {
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://t.me/s/oneclickvpnkeys',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.post(
        url, headers=headers)
    #print(response.text)
    pattren = re.compile(r'"https+:[^\s]*"')
    url_lst = pattren.findall(response.text)
    #print('获取到',len(url_lst),'个网址')
    #print(url_lst)
    return url_lst


#对bs64解密
def jiemi_base64(data):  # 解密base64
    # 对 Base64 编码后的字符串进行解码，得到字节字符串
    decoded_bytes = base64.b64decode(data)
    # 使用 chardet 库自动检测字节字符串的编码格式
    encoding = chardet.detect(decoded_bytes)['encoding']
    # 将字节字符串转换为字符串
    decoded_str = decoded_bytes.decode(encoding)
    return decoded_str

#判读是否为订阅链接
def get_content(url):
    #print('【获取频道',url,'】')
    url_lst = get_channel_http(url)
    #print(url_lst)
    #对链接进行格式化
    for i in url_lst:
        result = i.replace("\\", "").replace('"', "")
        if result not in new_list:
            if "t" not in result[8]:
                if "p" not in result[-2]:
                    new_list.append(result)
    #print(new_list)
    #print("共获得", len(new_list), "条链接")
    #获取单个订阅链接进行判断
    i = 1
    try:
        new_list_down = new_list[sub_n::]
    except:
        new_list_down = new_list[len(new_list) * 2 // 3::]
    #print("共获得", len(new_list_down), "条链接")
    #print('【判断链接是否为订阅链接】')
    for o in new_list_down:
        try:
            res = requests.get(o)
            #判断是否为clash
            try:
                skuid = re.findall('proxies:', res.text)[0]
                if skuid == "proxies:":
                    #print(i, ".这是个clash订阅", o)
                    end_list_clash.append(o)
            except:
                #判断是否为v2
                try:
                    #解密base64
                    peoxy = jiemi_base64(res.text)
                    #print(i, ".这是个v2ray订阅", o)
                    end_list_v2ray.append(o)
                    end_bas64.extend(peoxy.splitlines())
                    
                #均不是则非订阅链接
                except:
                    #print(i, ".非订阅链接")
                    pass
        except:
            #print("第", i, "个链接获取失败跳过！")
            pass
        i += 1
    return end_bas64

#写入文件
def write_document():
    if e_sub == [] or try_sub == []:
        print("订阅为空请检查！")
    else:
        #永久订阅
        random.shuffle(e_sub)
        for e in e_sub:
            try:
                res = requests.get(e)
                proxys=jiemi_base64(res.text)
                end_bas64.extend(proxys.splitlines())
            except:
                print(e,"永久订阅出现错误❌跳过")
        print('永久订阅更新完毕')
        #试用订阅
        random.shuffle(try_sub)
        for t in try_sub:
            try:
                res = requests.get(t)
                proxys=jiemi_base64(res.text)
                end_try.extend(proxys.splitlines())
            except Exception as er:
                print(t,"试用订阅出现错误❌跳过",er)
        print('试用订阅更新完毕',try_sub)
        #永久订阅去重
        end_bas64_A = list(set(end_bas64))
        print("去重完毕！！去除",len(end_bas64) - len(end_bas64_A),"个重复节点")
        #永久订阅去除多余换行符
        bas64 = '\n'.join(end_bas64_A).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
        #试用去除多余换行符
        bas64_try = '\n'.join(end_try).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
        #获取时间，给文档命名用
        t = time.localtime()
        date = time.strftime('%y%m', t)
        date_day = time.strftime('%y%m%d', t)
        #创建文件路径
        try:
            os.mkdir(f'{update_path}{date}')
        except FileExistsError:
            pass
        txt_dir = update_path + date + '/' + date_day + '.txt'
        #写入时间订阅
        file = open(txt_dir, 'w', encoding='utf-8')
        file.write(bas64)
        file.close()       
        
        #减少获取的个数
        r = 1
        length = len(end_bas64_A)  # 总长
        m = 8  # 切分成多少份
        step = int(length / m) + 1  # 每份的长度
        for i in range(0, length, step):
            print("起",i,"始",i+step)
            zhengli = '\n'.join(end_bas64_A[i: i + step]).replace('\n\n', "\n").replace('\n\n', "\n").replace('\n\n', "\n")
            #将获得的节点变成base64加密，为了长期订阅
            obj = base64.b64encode(zhengli.encode())
            plaintext_result = obj.decode()
            #写入长期订阅
            file_L = open("Long_term_subscription"+str(r), 'w', encoding='utf-8')
            file_L.write(plaintext_result)
            r += 1
        #写入总长期订阅
        obj = base64.b64encode(bas64.encode())
        plaintext_result = obj.decode()
        file_L = open("Long_term_subscription_num", 'w', encoding='utf-8')
        file_L.write(plaintext_result)
        #写入试用订阅
        obj_try = base64.b64encode(bas64_try.encode())
        plaintext_result_try = obj_try.decode()
        file_L_try = open("Long_term_subscription_try", 'w', encoding='utf-8')
        file_L_try.write(plaintext_result_try)
        #写入README
        with open("README.md", 'r', encoding='utf-8') as f:
            lines = f.readlines()
            f.close()
        now_time = datetime.datetime.now()
        TimeDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for index in range(len(lines)):
            try:
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription_num`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription1`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription2`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription3`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription4`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription5`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription6`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription7`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription8`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length-step*7}`\n')
                if lines[index] == '`https://raw.githubusercontent.com/w1770946466/Auto_proxy/main/Long_term_subscription3.yaml`\n': # 目标行内容
                    lines.pop(index+4)
                    lines.pop(index+4)
                    lines.insert(index+4, f'Updata：`{TimeDate}`\n')
                    lines.insert(index+4, f'### Try the number of high-speed subscriptions: `{len(try_sub)}`\n')
                if lines[index] == '>Trial subscription：\n': # 目标行内容
                    lines.pop(index)
                    lines.pop(index)
                """
                if lines[index] == '## ✨Star count\n': # 目标行内容
                    n = 5
                    for TrySub in try_sub:
                        lines.insert(index-n, f'\n>Trial subscription：\n`{TrySub}`\n')
                        n += 3
                """
            except:
                #print("写入READ出错")
                pass
        #写入试用订阅
        for index in range(len(lines)):
            try:
                if lines[index] == '## ✨Star count\n': # 目标行内容
                    n = 5
                    for TrySub in try_sub:
                        #lines.insert(index+n-1, f'\n>')
                        lines.insert(index-n, f'\n>Trial subscription：\n`{TrySub}`\n')
                        n += 3
            except:
                print("写入试用出错")
        
        with open("README.md", 'w', encoding='utf-8') as f:
            data = ''.join(lines)
            f.write(data)
        print("合并完成✅")
        try:
            numbers =sum(1 for _ in open(txt_dir))
            print("共获取到",numbers,"节点")
        except:
            print("出现错误！")
        
    return

#获取clash订阅
def get_yaml():
    print("开始获取clsah订阅")
    urls = []
    n = 1
    for i in urls:
        response = requests.get(i)
        #print(response.text)
        file_L = open("Long_term_subscription" + str(n) +".yaml", 'w', encoding='utf-8')
        file_L.write(response.text)
        file_L.close()
        n += 1
    print("clash订阅获取完成！")

#获取机场试用订阅
def get_sub_url():
    V2B_REG_REL_URL = '/api/v1/passport/auth/register'
    times = 1
    for current_url in home_urls:
        i = 0
        while i < times:
            header = {
                'Referer': current_url,
                'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            form_data = {
                'email': ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(12))+'@gmail.com',
                'password': 'autosub_v2b',
                'invite_code': '',
                'email_code': ''
            }
            if current_url == 'https://xn--4gqu8thxjfje.com' or current_url == 'https://seeworld.pro'  or current_url == 'https://www.jwckk.top'or current_url == 'https://vvtestatiantian.top':
                try:
                    fan_res = requests.post(
                        f'{current_url}/api/v1/passport/auth/register', data=form_data, headers=header)
                    auth_data = fan_res.json()["data"]["auth_data"]
                    #print(auth_data)
                    fan_header = {
                        'Origin': current_url,
                        'Authorization': ''.join(auth_data),
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Connection': 'keep-alive',
                        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
                        'Referer': current_url,
                    }
                    fan_data = {
                        'period': 'onetime_price',
                        'plan_id': '1',
                    }
                    fan_res_n = requests.post(
                        f'{current_url}/api/v1/user/order/save', headers=fan_header, data=fan_data)
                    #print(fan_res_n.json()["data"])
                    fan_data_n = {
                        'trade_no':fan_res_n.json()["data"],
                        #'method': '1',
                    }
                    fan_res_pay = requests.post(
                        f'{current_url}/api/v1/user/order/checkout', data=fan_data_n, headers=fan_header)
                    subscription_url = f'{current_url}/api/v1/client/subscribe?token={fan_res.json()["data"]["token"]}'
                    try_sub.append(subscription_url)
                    e_sub.append(subscription_url)
                    print("add:"+subscription_url)
                except Exception as result:
                    print(result)
                    break
            else:
                try:
                    response = requests.post(
                        current_url+V2B_REG_REL_URL, data=form_data, headers=header)
                    subscription_url = f'{current_url}/api/v1/client/subscribe?token={response.json()["data"]["token"]}'
                    try_sub.append(subscription_url)
                    e_sub.append(subscription_url)
                    print("add:"+subscription_url)
                except Exception as e:
                    print("获取订阅失败",e)
            i += 1

            
  
def get_kkzui():
    # ========== 抓取 kkzui.com 的节点 ==========
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
        res = requests.get("https://kkzui.com/jd?orderby=modified",headers=headers)
        article_url = re.search(r'<h2 class="item-heading"><a href="(https://kkzui.com/(.*?)\.html)"',res.text).groups()[0]
        #print(article_url)
        res = requests.get(article_url,headers=headers)
        sub_url = re.search(r'<p><strong>这是v2订阅地址</strong>：(.*?)</p>',res.text).groups()[0]
        print(sub_url)
        e_sub.append(sub_url)
        print("获取kkzui.com完成！")
    except:
        print("获取kkzui.com失败！")
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
        res = requests.get("https://www.cfmem.com/search/label/free",headers=headers)
        article_url = re.search(r"https?://www\.cfmem\.com/\d{4}/\d{2}/\S+v2rayclash-vpn.html",res.text).group()
        #print(article_url)
        res = requests.get(article_url,headers=headers)
        sub_url = re.search(r'>v2ray订阅链接&#65306;(.*?)</span>',res.text).groups()[0]
        print(sub_url)
        try_sub.append(sub_url)
        e_sub.append(sub_url)
    except Exception as e:
        print(e)
        
    
if __name__ == '__main__':
    print("========== 开始获取机场订阅链接 ==========")
    get_sub_url()
    print("========== 开始获取kkzui.com订阅链接 ==========")
    get_kkzui()
    print("========== 开始获取频道订阅链接 ==========")
    for url in urls:
        #print(url, "开始获取......")
        thread = threading.Thread(target=get_content,args = (url,))
        thread.start()
        threads.append(thread)
        #resp = get_content(get_channel_http(url))
        #print(url, "获取完毕！！")
    #等待线程结束
    for t in tqdm(threads):
        t.join()
    print("========== 准备写入订阅 ==========")
    res = write_document()
    clash_sub = get_yaml()
    print("========== 写入完成任务结束 ==========")
