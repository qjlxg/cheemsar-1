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
'http://agakoti3.com',
'http://www.akanyoni.com',
'https://akanyoni.com',
'http://ag.nezalab.com',
'https://5.104.85.115',
'https://5.181.79.10',
'https://www.duguletian.com',
'https://45.76.195.195',
'https://c.ms66.vip',
'http://c.ms66.vip',
'https://8.209.219.56',
'https://oneairport.club',
'https://140.99.243.104',
'https://93.179.98.143',
'http://www.8ks.link',
'https://tmdgogo.com',
'http://tmdgogo.com',
'http://new.tmdgogo.com',
'https://www.tmdgogo.com',
'http://c.tmdgogo.com',
'https://api.tmdgogo.com',
'http://www.tmdgogo.com',
'https://c.tmdgogo.com',
'http://plu.socoo-best.xyz',
'https://new.tmdgogo.com',
'http://api.tmdgogo.com',
'https://www.8ks.link',
'http://8ks.link',
'https://8ks.link',
'https://45.77.121.157',
'https://plu.socoo-best.xyz',
'http://206.189.46.32',
'http://3.37.83.181',
'http://www.swyun.cc',
'http://43.202.2.92',
'http://74.48.17.20',
'https://3.37.55.212',
'http://185.217.109.250',
'https://192.210.141.201',
'https://45.77.179.58',
'https://43.202.2.92',
'https://www.swyun.cc',
'https://client.vpn-tn.com',
'https://www.899800.xyz',
'https://899800.xyz',
'http://www.899800.xyz',
'http://899800.xyz',
'https://154.9.249.172:8443',
'http://103.137.246.5',
'http://139.162.110.25',
'https://172.93.221.93',
'http://157.230.255.121',
'http://totorolink.top',
'https://129.80.143.155',
'https://totorolink.top',
'http://totorol-a.top',
'https://totorol-a.top',
'https://104.243.28.247',
'https://45.77.73.40',
'https://74.48.45.254',
'http://asocupa2023.opc.uy',
'https://139.162.110.25',
'https://167.71.123.80',
'http://544.qmvuvpn1.top',
'https://asocupa2023.opc.uy',
'https://www.asocupa2023.opc.uy',
'http://www.asocupa2023.opc.uy',
'http://222.211.73.133:8081',
'http://www.asocupa2024.opc.uy',
'http://asocupa2024.opc.uy',
'http://cardiologia2025.opc.uy',
'http://tamako.iflute.cn',
'https://neurologia2024.opc.uy',
'https://www.neurologia2024.opc.uy',
'http://psiquiatriapediatrica2024.opc.uy',
'https://ajakteman.telkomsel.com',
'http://iclover.one',
'http://152.53.109.177',
'https://777.fsgyaa7.xyz',
'http://777.fsgyaa7.xyz',
'https://asocupa2024.opc.uy',
'http://www.cardiologia2025.opc.uy',
'http://fastpeak.net',
'https://www.fastpeak.cc',
'https://544.qmvuvpn1.top',
'https://subscribe.flydog.xyz',
'http://3.fsgyaa3.xyz',
'https://flydog.xyz',
'https://www.asocupa2024.opc.uy',
'http://www.fastpeak.top',
'https://fastpeak.top',
'http://my1708.myiplc.net',
'https://tamako.iflute.cn',
'http://www.fastpeak.xyz',
'https://www.cardiologia2025.opc.uy',
'http://neurologia2024.opc.uy',
'http://98.159.108.153',
'https://congresoshu2023.opc.uy',
'http://congresoshu2023.opc.uy',
'http://141.105.68.150',
'https://fastpeak.net',
'https://4.fsgyaa3.xyz',
'http://4.fsgyaa3.xyz',
'http://subscribe.flydog.xyz',
'http://www.fastpeak.net',
'http://fastpeak.top',
'https://xn--elt536k.com',
'https://my1708.myiplc.net',
'https://154.31.112.245',
'https://visite360.immo',
'https://154.12.56.232',
'https://www.visite360.immo',
'http://visite360.immo',
'http://www2.visite360.immo',
'https://www2.visite360.immo',
'http://www.visite360.immo',
'http://umgrade.com',
'http://www.umgrade.com',
'https://umgrade.com',
'https://www.umgrade.com',
'https://halug-app.fortcode.com.br',
'http://halug.fortcode.com.br',
'http://halug-app.fortcode.com.br',
'https://13.212.68.108',
'https://spadeecho.top',
'https://as9929.cc',
'http://sater1.xyz',
'https://www.sater.asia',
'https://sater.asia',
'http://sater.asia',
'https://sater1.xyz',
'http://www.ssweb.me',
'https://ssweb.me',
'https://www.ssweb.me',
'http://ssweb.me',
'https://zxwlpanl.xyz',
'http://zxwlpanl.xyz',
'https://cdpc.fun',
'https://103.93.73.144',
'https://108.61.247.148',
'https://149.129.52.64',
'http://test.hg-hy.com',
'https://5.181.79.10:8443',
'http://103.61.37.139',
'http://43.154.22.85',
'http://jiasugou.me',
'https://216.73.156.140',
'https://172.104.105.156',
'https://45.63.13.111',
'https://108.61.246.141',
'https://biu.zhangdada.news',
'http://biu.zhangdada.news',
'https://159.65.8.120',
'https://91.218.20.197',
'https://178.128.83.131',
'https://baibai.dodaci.xyz',
'http://baibai.dodaci.xyz',
'https://209.126.13.61',
'https://185.217.109.250',
'http://107.182.26.220',
'https://mail.snapminiblog.com',
'https://www.myladder.xyz',
'https://myladder.xyz',
'https://209.141.32.40',
'https://141.105.68.150',
'https://ntcloud.iceborder.com',
'http://ntcloud.iceborder.com',
'https://97.64.32.201',
'https://148.135.55.132',
'https://www.xn--elt536k.com',
'http://x.kidsclothe.shop',
'https://my.feimaapp.com',
'https://34.215.13.186',
'http://520vip.buzz',
'https://520vip.buzz',
'http://www.520vip.buzz',
'https://www.520vip.buzz',
'http://m1.fastpeak.xyz',
'http://m5.ai54321.com',
'https://m5.ai54321.com',
'https://m1.fastpeak.xyz',
'http://ek13.tw',
'https://ek13.tw',
'http://pannel.yimultd.com',
'https://pannel.yimultd.com',
'http://subs.maooooozaizi.xyz',
'https://subs.maooooozaizi.xyz',
'http://198.13.39.228',
'https://66.94.120.243',
'http://zz.sttkk.com',
'https://www.cepest.eu',
'https://zz.sttkk.com',
'https://autodiscover.cepest.eu',
'https://205.198.65.7',
'https://167.179.113.154',
'https://43.207.90.177',
'https://172.104.91.241',
'https://103.61.37.139',
'https://43.154.61.41',
'https://20.205.16.216',
'https://209.141.39.133',
'https://74.48.78.144',
'https://3.37.83.181',
'http://siminternet.org',
'https://siminternet.org',
'https://5.78.94.134',
'https://45.76.123.150',
'https://vanisher.top',
'https://www.vanisher.top',
'http://vanisher.top',
'https://152.67.214.174',
'https://152.53.109.177',
'https://198.13.39.228',
'https://217.197.160.178',
'https://198.13.37.132',
'https://52.78.46.53',
'https://45.66.134.90',
'https://45.154.13.10',
'http://www.justdidit.page',
'http://mail.snapminiblog.com',
'https://m.cepest.eu',
'https://129.159.241.89',
'https://smtp.cepest.eu',
'http://16.162.193.228',
'http://tiaowu.moe',
'http://www.catjun.mom',
'http://www.cepest.eu',
'https://cpcalendars.cepest.eu',
'http://hx148.rcmnk.cn',
'https://cpanel.cepest.eu',
'https://xinsrr.vip',
'https://justdidit.page',
'https://xxjc.work',
'http://91.218.20.197',
'https://cpcontacts.cepest.eu',
'http://dd.wudixingxing.com',
'http://xxjc.one',
'https://109.123.231.224',
'http://240608.duolaxin99.buzz',
'https://240608.duolaxin99.buzz',
'http://240607.duolaxin99.buzz',
'https://240607.duolaxin99.buzz',
'https://240607.duolaxin99.buzz:3443',
'https://240608.duolaxin99.buzz:3443',
'http://dyy.wudixingxing.com',
'http://xxjc.work',
'https://mail.justdidit.page',
'https://mail.cepest.eu',
'http://y.wudixingxing.com',
'https://dd.wudixingxing.com',
'https://ddyy.wudixingxing.com',
'https://www.justdidit.page',
'http://justdidit.page',
'https://xxjc.one',
'http://89.116.247.152:82',
'https://webmail.cepest.eu',
'http://ddyy.wudixingxing.com',
'https://hx148.rcmnk.cn',
'https://y.wudixingxing.com',
'https://www.shejimao.club',
'https://dyy.wudixingxing.com',
'https://www.catjun.mom',
'http://34.215.13.186',
'http://www.meimeiyun.top',
'http://www.shejimao.club',
'https://shejimao.club',
'http://xn--elt536k.com',
'https://aplusautism.com',
'https://www.pocketsponsor.com',
'https://mail.pocketsponsor.com',
'http://www.pocketsponsor.com',
'http://mail.pocketsponsor.com',
'http://pocketsponsor.com',
'https://pocketsponsor.com',
'http://5.104.84.149',
'https://fastpeak.cc',
'https://www.fastpeak.top',
'https://fastpeak.xyz',
'https://www.fastpeak.net',
'https://www.fastpeak.xyz',
'http://fastpeak.cc',
'http://www.fastpeak.cc',
'http://fastpeak.xyz',
'https://www.xinsrr.vip',
'http://www.xinsrr.vip',
'https://149.28.65.142',
'https://35.83.197.66:8443',
'https://www.enigmalogistics.org',
'http://www.enigmalogistics.org',
'https://enigmalogistics.org',
'http://enigmalogistics.org',
'https://www.778233.best',
'http://www.778233.best',
'https://www.vpnm.org',
'https://157.90.241.75',
'http://yibai.agakoti3.com',
'https://yibai.agakoti3.com',
'https://5.104.84.149',
'https://74.48.28.206',
'https://totorol-us4.top',
'http://totorol-us4.top',
'https://193.123.242.32',
'https://www.familee.page',
'http://www.familee.page',
'https://familee.page',
'http://familee.page',
'https://172.105.198.97',
'https://20240928.uk',
'http://20240928.uk',
'http://5.104.85.115',
'https://206.252.232.185:8443',
'https://www.akanyoni.com',
'https://agakoti3.com',
'https://ag.nezalab.com',
'http://akanyoni.com',
'http://www.agakoti3.com',
'https://www.agakoti3.com',
'https://www.snapminiblog.com',
'https://www.rocklandpage.com',
'http://www.rocklandpage.com',
'http://snapminiblog.com',
'http://simvpn.org',
'https://simvpn.org',
'http://www.ouer.one',
'https://www.ouer.one',
'http://ouer.one',
'https://ouer.one',
'https://www.emergencia2024.opc.uy',
'https://www.swsd2024.opc.uy',
'http://www.ovum2024.opc.uy',
'http://www.test.ovum2024.opc.uy',
'http://www.cardiologia2024.opc.uy',
'http://www.larim2023.opc.uy',
'https://www.psiquiatriapediatrica2024.opc.uy',
'http://test.ovum2024.opc.uy',
'http://www.neurologia2024.opc.uy',
'https://www.lag-cll2024.opc.uy',
'https://test.ovum2024.opc.uy',
'https://psiquiatriapediatrica2024.opc.uy',
'http://cardiologia2024.opc.uy',
'https://www.test.ovum2024.opc.uy',
'https://ovum2024.opc.uy',
'http://www.emergencia2024.opc.uy',
'http://www.psiquiatriapediatrica2024.opc.uy',
'https://emergencia2024.opc.uy',
'https://larim2023.opc.uy',
'http://larim2023.opc.uy',
'https://cardiologia2024.opc.uy',
'https://access.842698.xyz',
'http://yournetspeeder.xyz',
'https://www.yournetspeeder.xyz',
'http://www.yournetspeeder.xyz',
'https://yournetspeeder.xyz',
'http://subscribe.909808.xyz',
'https://bg.sspace.eu.org',
'http://45.77.73.40',
'http://bg.sspace.eu.org',
'https://www.mystic.skin',
'http://mystic.skin',
'http://www.mystic.skin',
'https://mystic.skin',
'https://45.77.26.81',
'https://142.171.118.59',
'https://43.135.132.241',
'http://rocklandvolleyball.net',
'https://rocklandvolleyball.net',
'https://test1.hdpt.pw',
'http://test.hdpt.pw',
'https://test.hdpt.pw',
'http://test1.hdpt.pw',
'https://18.179.230.107',
'https://node.hoopox.com',
'http://xykt.hehouzhu.cn',
'https://140.82.18.20',
'https://sh.cclchina.cn',
'https://154.26.208.61',
'http://3.36.134.53',
'https://okxyz.top',
'http://okxyz.top',
'http://ssr.hoste.top',
'http://stv22.228228.xyz:89',
'https://wiki.duguletian.com',
'https://li1852-97.members.linode.com',
'https://bw3.frankjun.com',
'https://140.238.36.123',
'http://cp1.asiagame.cloud',
'https://cp1.asiagame.cloud',
'https://dj.zuoy.co.uk',
'http://dj.zuoy.co.uk',
'http://panel.mkld.cc',
'https://panel.mkld.cc',
'http://f2k2y716e2ko9sdy.kenrich.xyz',
'https://rubisoft.co',
'http://rubisoft.co',
'http://172.93.221.93',
'https://foraintoo.dodaci.xyz',
'https://172.105.230.160',
'https://103.147.199.6',
'https://f2k2y716e2ko9sdy.kenrich.xyz',
'http://104.243.26.153',
'http://m3.fastpeak.cc',
'http://portal.solaronoff.com',
'https://m2.fastpeak.xyz',
'http://m2.fastpeak.xyz',
'https://m3.fastpeak.cc',
'http://mmxz2.meimei1314.xyz',
'http://haohao.dodaci.xyz',
'http://partoff.com',
'https://partoff.com',
'https://ss-test.1280720.xyz',
'http://ss-test.1280720.xyz',
'https://206.189.46.32',
'https://108.160.131.186',
'https://162.245.223.68',
'https://ssr.hoste.top',
'http://v1.jiasugou.life',
'http://v.jiasugou.club',
'http://v.jiasugou.life',
'https://v.jiasugou.life',
'https://v1.jiasugou.life',
'https://v.jiasugou.club',
'http://xxjc.casa',
'https://132.226.170.164',
'https://v6.goeed.com',
'https://104.225.154.178',
'https://xxjc.in',
'https://xxjc.casa',
'http://xxjc.in',
'https://vip.jiasugou.club',
'http://43.135.132.241',
'http://172.105.205.253',
'https://www.aplusautism.com',
'http://www.aplusautism.com',
'https://www.jiasugou.top',
'https://www.jiasugou.club',
'https://jiasugou.me',
'https://www.jiasugou.life',
'https://206.252.232.185',
'https://80.66.196.107',
'http://217.197.160.178',
'https://89.116.247.152',
'http://205.198.65.7',
'https://aka.nezalab.com',
'http://aka.nezalab.com',
'http://cdn.akanyoni.com',
'https://www.shejimao.trade',
'https://shejimao.xyz',
'http://shejimao.xyz',
'https://www.yitaiwa.com',
'http://www.yitaiwa.com',
'https://3.36.134.53',
'https://cp3.asiagame.cloud',
'http://cp3.asiagame.cloud',
'https://www.digidocparts.com',
'https://digidocparts.com',
'http://digidocparts.com',
'http://www.digidocparts.com',
'http://hal1.pqs.cloud',
'https://hal1.pqs.cloud',
'https://103.137.246.5',
'http://world.summercloud.one',
'https://world.summercloud.one',
'https://520.520vip.buzz',
'http://qwe.520vip.buzz',
'http://qwe.520vip.sbs',
'https://520.520vip.sbs',
'https://qwe.520vip.buzz',
'https://qwe.520vip.sbs',
'http://520.520vip.sbs',
'http://520.520vip.buzz',
'https://swsd2024.opc.uy',
'http://www.congresoshu2023.opc.uy',
'https://www.congresoshu2023.opc.uy',
'http://www.swsd2024.opc.uy',
'http://swsd2024.opc.uy',
'https://cardiologia2025.opc.uy',
'http://ttjs458.tcekx.cn',
'https://ttjs458.tcekx.cn',
'http://xxjc.vip',
'https://xxjc.vip',
'http://cdpc.fun',
'http://66.42.32.194:89',
'https://cdpc.club',
'http://cdpc.club',
'http://kenrich.io',
'https://kenrich.io',
'https://summercloud.one',
'http://summercloud.one',
'http://ctrl.onedak.com',
'https://ctrl.onedak.com',
'https://103.112.211.170',
'https://www.ovum2024.opc.uy',
'http://ovum2024.opc.uy',
'http://vvv.xn--laji2-ce2hy87ccl2a4n8h.com',
'https://vvv.xn--laji2-ce2hy87ccl2a4n8h.com',
'http://43.134.44.165:89',
'http://lag-cll2024.opc.uy',
'https://lag-cll2024.opc.uy',
'https://www.cardiologia2024.opc.uy',
'http://www.lag-cll2024.opc.uy',
'http://myladder.xyz',
'http://ml.lovepass.xyz',
'http://www.myladder.xyz',
'https://ml.lovepass.xyz',
'https://987100.xyz',
'https://halug.fortcode.com.br',
'https://www.larim2023.opc.uy',
'http://foraintoo.dodaci.xyz',
'http://emergencia2024.opc.uy',
'https://web.app.gfwjump.xyz',
'http://web.app.gfwjump.xyz',
'https://ssbb520.sbs',
'https://64.225.37.184',
'http://smtp.visite360.immo',
'https://smtp.visite360.immo',
'http://s.vpnm.su',
'http://v.jiasugou.live',
'https://v.jiasugou.live',
'https://vp1.jiasugou.life',
'http://xinsrr.vip',
'http://cdn.xiyoujishop.xyz',
'https://cdn.xiyoujishop.xyz',
'http://global.asiagame.cloud',
'https://global.asiagame.cloud',
'https://myreminders.page',
'http://myreminders.page',
'https://5.161.63.218',
'http://www.520vip.sbs',
'https://sub11.biubiusub001.top',
'https://s.vpnm.su',
'http://vp1.jiasugou.life',
'https://www.shejimao.xyz',
'http://simvpn3.org',
'https://dongqilai123.com',
'http://ssbb520.sbs',
'http://rayx.club',
'https://rayx.club',
'http://107.173.80.135:8000',
'http://dongqilai123.com',
'https://v.fook.us',
'http://www.shejimao.xyz',
'https://ouer.cyou',
'https://simvpn3.org',
'https://18.139.147.7',
'http://www.ouer.cyou',
'https://thuocnhanh.vn',
'https://www.thuocnhanh.vn',
'https://149.129.50.185',
'https://36.50.17.29',
'https://www.ouer.cyou',
'http://ouer.cyou',
'http://xxjc.nl',
'https://xxjc.nl',
'http://rocklandpage.com',
'https://dj.zuoyou.org.uk',
'http://dj.zuoyou.org.uk',
'http://xinsrr.pro',
'https://xinsrr.pro',
'http://ninetyhalf.com',
'https://www.ninetyhalf.com',
'https://ninetyhalf.com',
'http://www.nekossplay.xyz',
'http://nekossplay.xyz',
'https://nekossplay.xyz',
'https://www.nekossplay.xyz',
'http://www.ssbb520.top',
'http://www.ssbb520.xyz',
'https://www.ssbb520.xyz',
'https://ddyy.ssbb520.xyz',
'https://ssbb520.xyz',
'http://ssbb520.xyz',
'https://www.ssbb520.top',
'http://ddyy.ssbb520.xyz',
'https://43.154.84.34',
'https://catjun.lol',
'https://www.ripwall.us',
'http://www.ripwall.us',
'https://ripwall.us',
'https://portal.domeworld.me',
'https://oneairport.xyz',
'http://oneairport.club',
'http://132.226.170.164',
'http://www.myreminders.org',
'https://www.myreminders.org',
'http://www.ssbb520.sbs',
'http://45.32.58.103:100',
'http://198.13.39.228:100',
'https://sanduoyun.com',
'http://cp2.asiagame.cloud',
'https://cp2.asiagame.cloud',
'http://web.agnodes.com',
'https://web.agnodes.com',
'https://cdn.akanyoni.com',
'https://webapi.importal.top',
'http://www.xinsrr.pro',
'https://www.xinsrr.pro',
'https://freenekoss3.me',
'http://freenekoss3.me',
'http://www.freenekoss3.me',
'https://www.freenekoss3.me',
'https://xxjcdy.cfd',
'http://xxjcdy.cfd',
'http://old.shidongli161.xyz',
'https://old.shidongli161.xyz',
'http://ziyun.cyou',
'https://ziyun.cyou',
'http://02.ssttkk.com',
'http://www.mystic.lat',
'https://www.mystic.lat',
'https://mystic.lat',
'https://www.jiasugou.live',
'https://www.jiasugou.site',
'http://xiaosiqiu.xyz',
'https://xiaosiqiu.xyz',
'https://www.catjun.club',
'http://www.catjun.club',
'https://catjun.club',
'http://catjun.club',
'http://dash.joebuning.com',
'https://dash.joebuning.com',
'http://wbdlxs.xyz',
'http://www.wbdlxs.xyz',
'http://world.mucloud.one',
'https://world.mucloud.one',
'http://38.54.101.50',
'http://159.138.5.201',
'https://38.54.101.50',
'https://totorolsub.top',
'http://totorolsub.top',
'http://20240315.uk',
'https://20240315.uk',
'https://ouer.cc',
'https://192.210.207.215',
'https://www.520vip.sbs',
'https://spiritupgrade.com',
'https://ziyunv2.eu.org',
'https://515221104.fsgyaa2.xyz',
'http://515221104.fsgyaa2.xyz',
'https://purchase.seasideworkshop.net',
'http://purchase.seasideworkshop.net',
'https://web.shipv.net',
'https://ali.rkox5p.shop',
'http://vpn.chengchiinterglobal.com',
'http://ali.rkox5p.shop',
'https://vpn.chengchiinterglobal.com',
'http://mmxz.meimeifans123.cyou',
'https://mmxz.meimeifans123.cyou',
'http://b.ms66.vip',
'https://b.ms66.vip',
'https://192.252.178.228',
'http://47.74.181.232',
'https://34.222.176.191',
'https://ohwifi.online',
'http://ouer.cc',
'http://www.ouer.cc',
'https://www.ouer.cc',
'https://qq.899800.xyz',
'https://www.speednood.live',
'http://speednood.live',
'https://speednood.live',
'http://www.speednood.live',
'https://47.74.181.232',
'http://totorol-x.top',
'https://totorol-x.top',
'https://v1.jiasugou.top',
'https://gm.laalaa.top',
'http://gm.laalaa.top',
'https://dgadhk.zlnode.com',
'http://dgadhk.zlnode.com',
'http://47.57.233.238',
'http://4.kuangti9.xyz',
'https://47.74.189.6',
'https://154.12.179.60',
'https://139.180.140.203',
'https://ssp.zdd9999.xyz',
'http://ssp.zdd9999.xyz',
'https://47.128.155.8',
'http://speed.onloli.com',
'https://speed.onloli.com',
'http://sspanel.520555online.buzz',
'http://dj.zuo.org.uk',
'https://dj.zuo.org.uk',
'http://sblxs.xyz',
'https://sblxs.xyz',
'https://lapland.lol',
'http://lapland.lol',
'https://www.jiasugou.store',
'https://47.57.233.238',
'https://ganlxs.xyz',
'http://ganlxs.xyz',
'http://www.ganlxs.xyz',
'https://www.ganlxs.xyz',
'https://35.95.104.75',
'https://240706.duolaxin99.buzz',
'http://240706.duolaxin99.buzz',
'http://154.12.179.60',
'http://103.118.41.134',
'http://svip.7color.xyz',
'https://svip.7color.xyz',
'https://156.224.23.67',
'https://rinki.pw',
'http://rinki.pw',
'http://rinki.co',
'https://rinki.us',
'http://rinki.us',
'https://183.131.51.72',
'http://103.118.42.16',
'http://03.ssttkk.com',
'http://www.fucklxs.xyz',
'https://www.fucklxs.xyz',
'https://fucklxs.xyz',
'http://fucklxs.xyz',
'https://35.93.52.123',
'https://45.117.103.9:520',
'http://122.195.111.47:81',
'http://vip.jiasugou.life',
'https://svip.jiasugou.store',
'http://svip.jiasugou.live',
'http://svip.jiasugou.life',
'http://vip.jiasugou.live',
'https://vip.jiasugou.top',
'https://vip.jiasugou.live',
'http://svip.jiasugou.club',
'http://vip.jiasugou.store',
'http://v.jiasugou.top',
'https://svip.jiasugou.site',
'http://svip.jiasugou.store',
'https://v.jiasugou.site',
'https://svip.jiasugou.life',
'https://svip.jiasugou.live',
'http://vip.jiasugou.club',
'https://vip.jiasugou.life',
'http://v.jiasugou.site',
'https://svip.jiasugou.club',
'http://svip.jiasugou.top',
'http://vip.jiasugou.top',
'http://svip.jiasugou.site',
'https://svip.jiasugou.top',
'https://vip.jiasugou.store',
'https://v.jiasugou.top',
'http://wiki.fengchi.io',
'https://www.flyspeedcc.xyz',
'https://103.118.41.134',
'https://67.230.175.101',
'https://43.154.84.34:34',
'http://43.136.184.238:44443',
'http://43.227.112.240',
'http://172.93.221.93:2083',
'http://rinki.store',
'https://rinki.store',
'https://tz.tztznn.com',
'http://tz.tztznn.com',
'https://35.84.192.156',
'https://44.234.147.124',
'https://43.227.112.240',
'https://www.spadeeecho.top',
'http://www.spadeeecho.top',
'http://xxx.spadeeecho.top',
'https://104.128.91.95',
'https://44.242.248.253',
'https://13.113.61.38',
'https://148.135.15.87',
'https://35.82.26.178',
'http://520yun.xyz',
'https://www.520yun.xyz',
'https://520yun.xyz',
'http://www.520yun.xyz',
'https://www.wmjl.net',
'http://www.wmjl.net',
'http://wmjl.net',
'https://wmjl.net',
'http://staging.app.halug.com.br',
'https://staging.app.halug.com.br',
'https://45.63.61.150',
'http://hnd.relay.ssocksage.org',
'https://hnd.relay.ssocksage.org',
'https://52.229.157.117',
'https://13.251.35.58',
'http://www.mnschost.top',
'https://www.mnschost.top',
'https://www.lxshit.xyz',
'https://lxshit.xyz',
'http://www.lxshit.xyz',
'http://lxshit.xyz',
'https://34.223.110.132',
'http://pro.sy-sup.com',
'http://74.48.180.38',
'https://v7.xiaosiqiu.com',
'https://18.140.62.143',
'https://rinki.co',
'https://rinki.cc',
'http://rinki.cc',
'https://client.simvpn3.org',
'http://client.simvpn3.org',
'https://wan.ssbb520.top',
'https://www.myladder.de',
'http://myladder.de',
'http://wmjl.xyz',
'https://www.wmjl.xyz',
'https://myladder.pro',
'http://141.105.68.145',
'http://199.180.113.249:666',
'https://www.krucva.org.uk',
'http://www.krucva.org.uk',
'https://fastpeak.org',
'https://www.fastpeak.info',
'http://fastpeak.org',
'http://www.fastpeak.club',
'https://www.fastpeak.club',
'https://fastpeak.info',
'https://fastpeak.club',
'http://134.195.209.85',
'https://www.likuer.com',
'https://123.58.214.7',
'http://154.12.177.142',
'http://122.195.111.50:81',
'http://hxyx0526.xyz',
'https://hxyx0526.xyz',
'https://134.195.209.85',
'http://140.82.6.102',
'http://107.174.243.140',
'https://154.12.177.142',
'https://pro.sy-sup.com',
'https://54.212.71.226:8443',
'https://satori.top',
'https://vpnm.org',
'http://vpnm.org',
'http://rinki.vip',
'https://38.6.227.211',
'http://v8.xiaosiqiu.com',
'https://v6.xiaosiqiu.com',
'http://v6.xiaosiqiu.com',
'https://v8.xiaosiqiu.com',
'http://v9.xiaosiqiu.com',
'https://v9.xiaosiqiu.com',
'http://v7.xiaosiqiu.com',
'https://ssbb520.top',
'https://chaitin.speedflyc4432413.store',
'https://www.erha.life',
'http://www.erha.life',
'http://www.wmjl.xyz',
'http://205.198.65.202:9002',
'https://162.245.221.206',
'http://www.clicwren.org.uk',
'https://www.clicwren.org.uk',
'https://34yhh.mmy999.buzz:25588',
'https://13.250.115.2',
'http://icn.relay.ssocksage.org',
'https://icn.relay.ssocksage.org',
'https://89.208.245.203',
'https://www.daihp.org.uk',
'http://www.daihp.org.uk',
'http://54.92.18.172:98',
'https://www.fastpeak.life',
'http://fastpeak.life',
'https://www.fucklxs.com',
'https://www.curseurmum.com',
'http://www.fucklxs.com',
'https://www.mail.fastpeak.org',
'http://www.curseurmum.com',
'https://fastpeak.life',
'http://www.fastpeak.org',
'http://www.fastpeak.life',
'http://www.myladder.de',
'https://curseurmum.com',
'https://myladder.de',
'http://www.myladder.pro',
'https://www.myladder.pro',
'http://fucklxs.com',
'http://myladder.pro',
'https://fucklxs.com',
'https://likuer.com',
'https://www.fastpeak.org',
'http://www.likuer.com',
'https://34yhh.mmy999.buzz',
'http://likuer.com',
'https://fea3.mmy999.buzz',
'http://www.fastpeak.info',
'http://34yhh.mmy999.buzz',
'http://fea3.mmy999.buzz',
'http://curseurmum.com',
'https://54.255.214.46',
'https://141.105.68.145',
'https://54.212.71.226',
'https://520.baibao999.com',
'https://luobomix999.com',
'http://luobomix999.com',
'http://www.luobomix999.com',
'http://520.baibao999.com',
'http://baibao999.com',
'https://18.163.184.15',
'https://ssp.hoste.top',
'http://ssp.hoste.top',
'https://what.waimaotop.net',
'https://www.catjun.icu',
'http://www.catjun.icu',
'http://catjun.icu',
'https://catjun.icu',
'https://light.pqs.cloud',
'http://light.pqs.cloud',
'https://47.242.0.50',
'http://shejimao.trade',
'https://shejimao.trade',
'https://20.2.161.97',
'https://35.91.120.168',
'https://ww2.blinblin-taytay.top',
'https://35.91.120.168:8443',
'https://205.234.234.101',
'http://20.2.161.97',
'http://172.207.131.188',
'https://gg.wttkk.com',
'http://gg.wttkk.com',
'https://23.99.104.145',
'https://47.128.245.216',
'https://clashhk.azurewebsites.net',



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
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription_num`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription1`\n':
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription2`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription3`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription4`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription5`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription6`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription7`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {step}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription8`\n': # 目标行内容
                    lines.pop(index+1)
                    lines.insert(index+1, f'`Total number of merge nodes: {length-step*7}`\n')
                if lines[index] == '`https://raw.bgithub.xyz/w1770946466/Auto_proxy/main/Long_term_subscription3.yaml`\n': # 目标行内容
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
