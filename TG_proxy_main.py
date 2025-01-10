# w1770946466 北慕白  https://github.com/w1770946466/Auto_proxy

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
'https://sq9xy6.cpminig.com',
'https://ch.louwangzhiyu.xyz',
'https://www.kuaidog006.top',
'https://qingyun.zybs.eu.org',
'https://xn--4gqp1u.com',
'https://xueyejiasu.com',
'https://lanmaoyun.icu',
'https://needss.link',
'https://dashuai.us',
'https://hy-2.com',
'https://vpn.sudatech.store',
'https://changyouvpn.top',
'https://by.yunduanjc.top',
'https://yunduanjc.top',
'https://pmy666.xyz',
'https://air.aptlive.org',
'https://naisicloud.xyz',
'http://qingyunti.cc',
'https://pfjc.im',
'https://nexx.us.kg',
'https://w02.qytl2web01.cc',
'https://kaikaixinxin.me',
'https://kuailejc.xyz',
'https://dash.minizz.online',
'https://api114514.nuwaa.rest',
'https://yunlu.vip',
'https://vvcloud.us.kg',
'https://zouma.guanhua.xyz',
'https://kaolacloud.site',
'https://www.hj521.top',
'https://www.hj522.top',
'https://superbiu.com',
'https://my.pianyi.info',
'https://zxc.noseisei.com',
'https://abc.noseisei.com',
'https://bailian.site',
'https://passwall.link',
'https://xyz.noseisei.com',
'https://b.yousu.cc',
'https://www.xbyun.live',
'https://app.legeth.cc',
'https://c.yousu.cc',
'http://vyy.idsduf.com',
'https://a.yousu.cc',
'https://www.smcow.com',
'https://thecom.today',
'https://xmfwww.cc',
'https://a123.buzz',
'https://a.aik88.top',
'https://aikx.me',
'https://zzz.youxuan.wiki',
'https://maple.icu',
'https://1.vyunyun.top',
'https://pkq.xlm.plus',
'https://ddddd.site',
'https://zqjc.org',
'https://www.aaaspeed.cc',
'https://xx-ai.io',
'https://zhenshihui.life',
'http://1run.vip',
'https://zhenshihui.shop',
'https://abyssvpn.com',
'https://app.cloudlion.me',
'https://user.susucloud.net',
'https://zhuiyun.top',
'https://gg.mqs.xyz',
'https://sulink.pro',
'https://arisaka.io',
'https://www.eyujichang.com',
'https://www.mangshe.org',
'https://db.shellnet.net',
'https://aikx.me/api',
'https://jisovpn.site',
'https://fpacecloud.com',
'https://niercloud.com',
'https://my.catfaka.com',
'https://www.xfxssr.com',
'https://b.xiaow.cc',
'https://www.chaoyue.shop',
'https://snangua.com',
'https://client.3i.lol',
'https://www.strongswans.net',
'https://wumaojichang.com',
'https://f.wwwq.net',
'https://www.dukadi.one',
'https://cococloud.online',
'https://waterwheel.buzz',
'https://yingwuyun.top',
'https://www.yunanyun.com',
'https://app.lwjyj.com',
'https://leflycloud.com',
'https://ktmcloud.shop',
'https://ktmcloud.top',
'https://www.tencloud.net',
'https://xianyuwangluo.top',
'https://t.me/sulink01',
'https://zhuye2.sulink.one',
'https://page.sulink.one',
'https://ai.totwo.top',
'https://ai.totwo.link',
'https://totwo.top',
'https://a1.darkforest.cloud',
'https://syq.tw',
'https://cxk.lol',
'https://darkforest.cloud',
'https://sanxijichang.com',
'https://sidog.top',
'https://store.kakocloud.pro',
'https://gfw.best',
'https://www.genies.top',
'https://chiguayun.net',
'https://chiguayun.com',
'https://chiguayun.org',
'https://guanwang.me',
'https://liulangdiqiu.cc',
'https://qianggewangluo.com',
'http://nanbei.cloud',
'http://nanbei.buzz',
'https://www.1365365.xyz',
'https://bt3.one',
'https://tcity8.top',
'https://liangyuandian.club',
'https://shuimu.site',
'https://reborn.kaochang.ltd',
'https://fastestcloud.xyz',
'https://gd.kaxinzx.cc',
'https://kuaiqiangshou.xyz',
'https://neko.services',
'https://neko.yuriuni.com',
'https://vpn.gunyoung.top',
'http://dash.legeth.com',
'https://my.legeth.com',
'http://onefall.top',
'http://www.paopao.dog',
'https://app.birds.hk',
'https://www.1belt1road.vip',
'https://port.baozipu.cc',
'https://www.1655ss.com',
'https://usla.icola.top',
'https://22.lownet.xyz',
'https://suwayun.com',
'https://wayen.eu',
'https://mpddt.top',
'https://www.9yuan.top',
'https://jk-cloud.net',
'https://www.fooksun.xyz',
'https://jkcloud.net',
'https://cn.logseq.com',
'https://studygolang.com',
'https://www.zhujiechong.top',
'https://pkqjiasu.com/',
'https://bestssr.com',
'https://xpoti.com',
'https://大机场.net',
'https://jfcloud.net',
'https://ftzaffcom01.fliggyaff.xyz',
'https://www.chaojijichang.com',
'https://1yunti.org',
'https://baiyunvpn.com',
'https://docs.sakura-cat.club',
'https://vilavpn.net',
'https://www.dotsvpn.com',
'https://cokecloud.net',
'https://xbsj6.com',
'https://www.shaoshupaiss.com',
'https://haita.io',
'https://web3vpn.net',
'https://shuttle.gt-all.com',
'https://一元.org',
'https://sakuracat-003.com',
'https://du9so.com',
'https://www.akspeedy.com',
'https://us.oteacc.org',
'https://fscloud111.gitbook.io',
'https://aff.91jsq.org',
'https://ocguide.eyw015.com',
'https://www.skylinevpn.net',
'https://neoladder.com',
'https://www.09axjsq.com',
'https://v2free.net',
'https://jfcat.net',
'https://flyingbird-docs.gitbook.io',
'https://doc.boccc.co',
'https://www.cmynetwork.com',
'https://www.surfshark-china-get.com',
'https://b.ikunvpn.com',
'https://ztnet.io',
'https://01.tolinkdocs.com',
'https://www.cryxr1.net',
'https://www.gitbook.com',
'https://www.godualnet.com',
'https://ovofast.com',
'https://imginn.com',
'https://www.98kjsq.com',
'https://egjplmujirj2tbj9wuzy.wgetcloud.org',
'https://www.guru99.com',
'https://mistycloud.io',
'https://pj.telescope.name',
'https://dog.amnadog.com',
'https://wzpwmu.com',
'https://hideuvpn.gitlab.io',
'https://www.vyprvpn.com',
'https://xfltd.org',
'https://doveee.net',
'https://blog.xiaohuojianpro.com',
'https://azzico.com',
'https://azi.homes',
'https://portal.colacloud.net',
'https://helloshudong.com',
'https://quickq.io',
'https://nordvpn.com',
'https://jifengcloud.crisp.help',
'https://www.233network.com',
'https://慈善机场.com',
'https://a.smjcdh.com',
'https://www.libcyber.com',
'https://lineshort.com',
'https://www.telescope.name',
'https://www.wwwjs01.com',
'https://www.cyberghostvpn.com',
'https://jf97.net',
'https://www.accdream.com',
'https://kerrynotes.com',
'https://haojichang.com',
'https://qingyun.world',
'https://qingyunjia.cc',
'https://url.pdno.top',
'https://pannods.com',
'https://spanode.top',
'https://lponn.top',
'https://homepanda.top',
'https://www.tppnnnood.top',
'https://www.tnod.top',
'https://hhonode.top',
'https://tprenode.top',
'https://pandanodes.com',
'https://tpnoo.top',
'https://www.tpanda.top',
'https://tbnoes.top',
'https://panod.top',
'https://frenode.top',
'https://transnode.top',
'https://pnod.top',
'https://web.fscloud.cc',
'https://yiyuan1.com',
'https://xiaojicf.com',
'https://v2.xiaojikp.cc',
'https://ykxqn.com',
'https://feiniaoyun.top',
'https://ss.mba',
'https://youzi.win',
'https://my.bitzconnect.com',
'https://dash.fscloud.cc',
'https://mojie.la',
'https://www.hdyun.cc',
'https://a.hdyun.icu',
'https://cloudyu.top',
'https://www.tpnod.top',
'https://hello-yundong.com',
'https://okokcloud.com',
'https://tapfog.com',
'http://dash.fscloud.cc',
'https://www.maomaovpn.com',
'https://okokcloud.net',
'http://qiuyin.us/me',
'https://apanel.tinnyrick.com',
'https://a.sudacloud.top',
'http://776777.cc',
'http://www.bajie.pw',
'https://1元机场.com',
'https://www.ck971.com',
'https://www.linghunyun.com',
'https://www.gijsq.com',
'https://bajie.pw',
'https://doucat.top',
'https://geek.rrabits.com',
'https://www.sudun1.top',
'https://yuyan.lol',
'https://cat.1919810.com',
'https://clashverge.net',
'https://666.xbsj.org',
'https://user2.yuziyun.top',
'https://console.henet.uk',
'http://qiuyin.co/me',
'https://51tiger.cc',
'https://front.fishport.cloud',
'https://yuyan.online',
'https://cdn2.azzico.com',
'https://51ssr.com',
'https://kugou.cloud',
'https://okvpn.cc',
'https://www.789jiasu01.com',
'https://shandianpro.com',
'https://sd.369.cyou',
'https://cc01.xiaojikp.pro',
'https://www.hx666.info',
'https://doveee.com',
'https://static.golangjob.cn',
'https://mccloud.gay',
'https://teacat.cloud',
'https://www.dageyun.net',
'http://daishu.pro',
'http://yohaokun.com',
'https://byjc.top',
'https://miaona.org',
'https://91unicorn.cloud',
'https://zijieyunti.com',
'https://www.bixiny.com',
'http://www.gijsq.com',
'https://clashfor.org',
'https://yuyan.pro',
'https://cc.7en7.com',
'https://hongxingdl.com',
'https://abstract.vmssr.online',
'https://www.freedidi.com',
'https://cat77.org',
'https://www.clash.la',
'https://hide.mn',
'https://www.iovevpn.com',
'https://一元机场.art',
'https://pigeon-cloud.one',
'https://666.youtu2.com',
'https://v.xdy2.vip',
'https://qingyun.io',
'https://abstraction.vmssr.online',
'http://smjcdh.com',
'https://access.feishayun.com',
'https://feisha.369.cyou',
'https://sakura-cat1.com',
'https://azicloud.azzico.cc',
'https://www.leavescn.com',
'https://newhua99.com',
'https://www.kayuwang.com',
'https://next.geph.io/zhs',
'https://www.baiyuncloud.cc',
'https://直连机场.com',
'https://ajax.vmssr.cc',
'https://www.xfx01.com',
'https://justmysocks.github.io',
'https://totorocloud.cc',
'http://azicloud.azzico.cc',
'https://discuss.d2l.ai',
'https://ssr6.com',
'https://www.qf1.us',
'https://openclash.org',
'https://dashboard.vmssr.cc',
'https://www.jichang888.com',
'https://cloudfisher.net',
'https://v2b-user2-2goqpyj69b370c2b-1314147066.ap-shanghai.app.tcloudbase.com',
'https://getsingbox.com',
'https://m.qfacc.cn',
'https://h51.liebao2.com',
'https://docs.kuaiyin.pro',
'https://www.flowus.cn',
'https://www.jiasuff.com',
'https://www.mikasa.cloud',
'https://tolink.pro',
'https://58rocket.com',
'https://vip.taoqitu.pro',
'http://ant77.top',
'http://api.123417.xyz',
'http://api.sgjc.xyz',
'http://api.xn--14ra41gd24b.xyz',
'http://api-0609.m55u97uleod7lm5.download',
'http://ciallo.elegy.icu:7001',
'http://cloudupup.com',
'http://dashabi.ping-zi-yun.icu',
'http://dingyue.myzone.site',
'http://dingyue2.qyjc.xyz',
'http://dingyue3.qyjc.xyz',
'http://dishujichang.xyz',
'http://dy.changyouVPN.top',
'http://dy.changyouvpn.top',
'http://dy.hpyjc.top',
'http://dy.xyyjc.top',
'http://em7.buzz',
'http://fanqiang88.top',
'http://fbapiv1.fbsublink.com',
'http://fdgdr0dg3.xbvpn.vip',
'http://filusdt.461553.best:1588',
'http://free.ninecloud.co',
'http://fs123121.cdn.22.jiacdnd123456789.com',
'http://g3i.buzz',
'http://gbtgurl01.org',
'http://ggiuwegivhe123.a123.bond',
'http://hpyjc.top',
'http://jjz.31465.cfd',
'http://jshou.top',
'http://laobideng.xyz',
'http://lianjiasub.work',
'http://ly.ccwink.cc',
'http://mf.kejifan88.top',
'http://mine.subcsyun.online',
'http://msvpn.gougouvpn.xyz:88',
'http://nangang.pro',
'http://s.33y.run',
'http://s.kalaa.me',
'http://s1.subcsyun.online',
'http://s3.subcsyun.online',
'http://s4.subcsyun.online',
'http://user.tsunaminet.cc',
'http://v2-1.806cms.top',
'http://vip.365cloud.me',
'http://vpn.gougouvpn.xyz:88',
'http://vps.huanshi88.sbs',
'http://www.fanqiang88.top',
'http://www.freeflyingcloud.xyz',
'http://www.mmsbs.buzz',
'http://www.pingzicloud.top',
'http://x1yjc.top',
'http://xbvpn.vip',
'http://xsj520.top',
'http://xyyjc.top',
'http://yy-cmi.mozhiti.top',
'http://yzxxy.top',
'https://12123.org',
'https://123abc.love',
'https://17852.xyz',
'https://196284.nginxzfd.xyz',
'https://1g.gay',
'https://1st.sub-airport.com',
'https://1ytcom01.1yunti.net',
'https://231787.xyz',
'https://25054128.xyz',
'https://3h.lv',
'http://hy-2.com',
'http://lanmaoyun.icu',
'http://sq9xy6.cpminig.com',
'http://qingyun.zybs.eu.org',
'http://www.kuaidog006.top',
'http://vpn.sudatech.store',
'http://needss.link',
'http://xn--4gqp1u.com',
'http://ch.louwangzhiyu.xyz',
'http://sulink.pro',
'http://xueyejiasu.com',
'http://47.243.59.73',
'http://569cdn.1010520.click',
'https://523qaweg246.pandafly.site',
'https://9bd4028e.ghelper.me',
'https://aaa.yunduanjc.top',
'https://awacloud.online',
'https://ch.cukug.website',
'https://dy.kuailejc.xyz',
'https://dy.naisicloud.xyz',
'https://huahe.link',
'https://jb.taipeicity.news',
'https://ly.ccwink.cc',
'https://pianyi.sub.sub.subsub123456789.com',
'https://pro.xn--l9qyaz082a.cn',
'https://qq.xlm.plus',
'https://sub.mogufan.com',
'https://sub.sanfen018.xyz',
'https://sub.tgzdyz2.xyz',
'https://sub.tuanzi.xyz',
'https://sub.xn--4gq62ffxz.net',
'https://sub.xn--4gqp1u.com',
'https://submit.xz61.cn:23443',
'https://www.dabai.in',
'https://youxiu5172.xiaofeixia.cfd',
'https://dash2.moonriver.one',
'https://cn.newbee888.cc',
'https://6.needss.one',
'https://xc1.shishi1.buzz',
'https://mgxiaowu.net',
'https://dabai.in',
'https://db01.in',
'https://hy-2.sbs',
'https://aa.dabai.in',
'https://api.heima2u.com',
'https://www.meigui168.net',
'https://cn.newbee.cyou',
'https://mgnet.vip',
'https://portal.speedyyun.com',
'https://s1.equinoxaa.com',
'https://www.f2ray.com',
'https://www.littleqqq.co',
'https://懒猫.com',
'https://www.z1z1.top',
'https://honven20.dgywzc.com',
'https://reurl.cc',
'https://cloud.speedypro.xyz',
'https://www.qlgq.top',
'https://www.v2ny.com',
'https://ikuuu.me',
'https://xn--iiq540h.com',
'https://jgjs02.com',
'https://xn--4gq62f52gdss.com',
'https://board.jike99.xyz',
'https://www.mojie.me',
'https://besnow.me',
'https://lksi.xyz',
'https://www.taishan.pro',
'https://zhu.suyun.bio',
'https://glados.space',
'https://tly.sh',
'https://sockboom.love',
'https://panel.keleofficial.com',
'https://daniu.e300daniu.top',
'https://klxq.djgskc.top',
'https://px.bt3.one',
'https://chy.fit',
'https://v3ssy.xyz',
'https://www.proxyvip.xyz',
'https://daxun.club',
'https://bcast.ink',
'https://b0chi.r-yu.me',
'https://cd520.xyz',
'https://www.aoxiangyun.top',
'https://www.mickey.business',
'https://sp.nfsq.me',
'https://cocolink.org',
'https://oukasou.xyz',
'https://www.aimacloud.info',
'https://user.xinna.co',
'https://nanmin.xyz',
'https://qiaoxbbq.com',
'https://mxwljsq.xyz',
'https://www.okvpn.cc',
'https://my.jetfast.dev',
'https://shandiandog.com',
'https://tagss04.pro',
'https://suo.yt',
'https://cdn.ednovas.org',
'https://qytvipaffcc04.qytvipaff.pro',
'https://fengwo.pro',
'https://love.52pokemon.cc',
'https://ocloudvpn.com',
'https://mly01.miaolianyun.my',
'https://px.xinyo.me',
'https://airport.raloar.top',
'https://xunlian.site',
'https://www.cacapex.com',
'https://a.kpyun.live',
'https://main.cute-cloud.de',
'https://cloud.jisuba.me',
'https://便宜机场.co',
'https://site01.stardad.lol',
'https://mogufan.com',
'https://app.cloudog.me',
'https://invite6.cht.taipei',
'https://app.gomeow.cloud',
'https://guobaotegong.me',
'https://jjz2.31465.cfd',
'https://a.0123456789.us.kg',
'https://a.opk.icu',
'https://569.2.passwallwall.life',
'https://aeda2.asa.lol',
'https://user.dafeiji.one',
'https://web2.dogssr.sbs',
'https://web2.52pokemon.cc',
'https://ni8.zxm.cc',
'https://sub.ssrsub.com',
'https://www.kuaidog010.top',
'https://mlshu.com',
'https://dash.bigcow.cc',
'https://www.fawncloud.one',
'https://cloud.speedyweb.xyz',
'https://z.luxury',
'https://askahh.com',
'https://powerwan.net',
'https://afun.la',
'http://web.nnpy.org',
'https://syyn.1.passwallwall.life',
'https://www11.henet.uk',
'https://ikuuu.pw',
'https://xn--wtq35pfyd55o.co',
'https://asa.lol',
'https://www.huaxia.cyou',
'https://newserver.t1i.top',
'https://ins.ins66.com',
'https://www.flymetothemoon.work',
'http://ov2rayo.top',
'http://17yxyy.cc',
'https://54fxp.xyz',
'https://haoba.cloud',
'https://mianmd.ninja',
'https://www.gogocloud.cyou',
'https://planb.cat',
'https://v.cheerfun.dev',
'https://www.cantonx.com',
'https://air.yoyoss.xyz',
'https://www.v2ssr.top',
'https://91yun.buzz',
'https://portal.buddhajumpsoverthewall.com',
'http://network2.magic-in-china.com',
'https://kedouair.top',
'http://kaxin.cc',
'https://www.wkyun1688.com',
'https://ssr.giize.com',
'https://home.wkyuns.xyz',
'https://air.misakano.eu.org',
'https://yhcvpn.xyz',
'https://www.starlink9527.xyz',
'https://starlink.to',
'https://bajie.info',
'https://marslink.org',
'https://www.marslink.cc',
'https://8rkt.xyz',
'https://miaona.xyz',
'https://api.dashsp.top',
'https://miaona.co',
'https://latiao.club',
'https://58sd.net',
'https://latiao.us',
'https://glados.one',
'https://glados.network',
'https://bityun.org',
'http://bityun.org',
'http://sub.chbjpw.mobi',
'https://88catnet.com',
'https://www.99catnet.com',
'https://www.58mdss.com',
'https://mdss.cloud', 
'https://m11.spwvpn.com',
'https://m2net.lol',
'https://m2net.sbs',
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
