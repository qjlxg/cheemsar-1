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

'https://cm-sub.pz.pe',
'https://hn1r5k7322.bitmusttw.com',
'https://fsc.jiediandingyuejiji.homes',
'https://mc.jiedianxielou.workers.dev',
'https://zjsub.gitpub.top',
'https://sublink.52cloud.eu.org',
'https://laosijicc.top',
'https://52pokemon.xz61.cn',
'https://kawaiifreevpn.pages.dev',
'https://pianyi.sub.sub.subsub123456789.co',
'https://speedx2net.postshup.ir:2096',
'https://2381bfde-8c93-4701-8f14-24f071067a1a.nginx24bit.xyz',
'https://cola.xn--chqu2nzsxv3y.com',
'https://sub123.71345.xyz',
'https://088ea81a-3547-85e0-4af6-dfcb3c6674aa.372372.xyz',
'https://sub.feiji.ip-ddns.com',
'https://bujidao.cc',
'https://mlshu.com',
'https://ymzx.jiedianxielou.workers.dev',
'https://pianyi.sub.sub.subsub123456789.com',
'http://xby2.op-house.top',
'https://linke.phantasy.life',
'https://kcsub.vip',
'https://zero.76898102.xyz',
'https://088EA81A-3547-85E0-4AF6-DFCB3C6674AA.372372.xyz',
'https://1321078938-11mmjf3qkb-hk.scf.tencentcs.com',
'https://52daishu.uk',
'http://em7.buzz',
'https://xn--yetu3xij4b.com',
'https://sub.cokecloud.world',
'https://yyds.emovpn.top',
'https://d7b12d59-21aa-9561-087f-89c834ac7fe8.372372.xyz',
'https://sub.xn--2vxn29amga.com',
'https://aimanman.me',
'https://s1.bnsubservdom.com',
'https://sub.372372.xyz',
'https://b3b0549e-160e-495a-a528-cccf5148bc48.372372.xyz',
'https://ch.cukug.website',
'https://www.066664.xyz',
'https://ch.vfkum.website',
'https://ch.louwangzhiyu.xyz',
'https://wpjlzq00.xiaoliyusub.top:8443',
'https://dlo3va.subxly.cfd:8443',
'http://filusdt.461553.best:1588',
'https://b.bbydy.org',
'https://xship.top',
'https://ts.xship.top',
'https://subscription-gov.lianjiasub.work',
'https://yuxi.fanqiev2.work',
'https://ch.owokkvsxks.store',
'https://s1.byte33.com',
'https://sub.eyujichang.com',
'https://server.fylink.link',
'http://1.1596666.xyz',
'http://1.1598888.xyz',
'http://101.200.14.80:3325',
'http://103.196.20.127',
'http://106.15.63.84:39391',
'http://113.31.116.212:13800',
'http://15.197.234.117:40329',
'http://175.178.3.157:39393',
'http://193.134.211.92',
'http://2ec535a5c35aa5a4b44249428dbb3d01.52pokemon.top',
'http://3093492f6b2332f8server.lycoris.one',
'http://372ae8252c9ce608c5f7066f2177dfb1.52pokemon.top',
'http://3ae4349382d5ae35b6e5dda2e68d3df0.52pokemon.top',
'http://42.51.33.241:88',
'http://47.239.210.43',
'http://47.243.59.73',
'http://47.83.197.147:13896',
'http://569cdn.1010520.click',
'http://6465307854ab0a2c82b66d32ffa2107e.52pokemon.top',
'http://66ds.dishujichang.xyz',
'http://6b.zhunchuanpb.com',
'http://6bsub.zhunchuanpb.com',
'http://8.134.181.161:12580',
'http://ant77.top',
'http://api-0609.m55u97uleod7lm5.download',
'http://api.123417.xyz',
'http://api.sgjc.xyz',
'http://api.xn--14ra41gd24b.xyz',
'http://best.momoxiaodian.cc',
'http://c9k.buzz',
'http://ciallo.elegy.icu:7001',
'http://cloudupup.com',
'http://csgo3.fask511.cfd:1588',
'http://dashabi.ping-zi-yun.icu',
'http://dingyue.myzone.site',
'http://dingyue2.qyjc.xyz',
'http://dingyue3.qyjc.xyz',
'http://dishujichang.xyz',
'http://dy.changyouVPN.top',
'http://dy.changyouvpn.top',
'http://dy.hpyjc.top',
'http://dy.xyyjc.top',
'http://dydz.xn--mesv8bx6xtx3b.com:2006',
'http://e8a580bd3a51b6050aabd8919a17d106.52pokemon.top',
'http://fbapiv1.fbsublink.com',
'http://fdgdr0dg3.xbvpn.vip',
'http://feigou.zhunchuanpb.com',
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
'http://n15uvht4r659107p.eastasia.cloudapp.azure.com',
'http://nangang.pro',
'http://on1vejas4m6z.w7yxefcx0i11.click',
'http://one.bblinks.top',
'http://panda.xn--i8sx78aisa52z.com',
'http://panda.xn--lbrx91akmhm30c.com',
'http://pf.juzimao01.cloud/Moe233-Subs',
'http://s.33y.run',
'http://s.kalaa.me',
'http://s1.subcsyun.online',
'http://s3.subcsyun.online',
'http://s4.subcsyun.online',
'http://sub.sub.sub.subsub123456789.com',
'http://sub.xn--54qu5qypuo1o.xn--fiqs8s',
'http://sub2086.fnyune.shop:2086',
'http://user.dafeiji.one',
'http://user.tsunaminet.cc',
'http://v2-1.806cms.top',
'http://vip.365cloud.me',
'http://vpn.gougouvpn.xyz:88',
'http://vps.huanshi88.sbs',
'http://vyysub.euquw.cn',
'http://www.crosswall.org',
'http://www.freeflyingcloud.xyz',
'http://www.mmsbs.buzz',
'http://www.pingzicloud.top',
'http://x1yjc.top',
'http://xbvpn.vip',
'http://xn--4gq62f8yih87b.site',
'http://xsj520.top',
'http://xyyjc.top',
'http://yy-cmi.mozhiti.top',
'http://yzxxy.top',
'http://yzxxy.top:7001',
'https://031216.xyz',
'https://0415.chun-auto-one.xyz',
'https://04hua.xiaoliyusub.top:8443',
'https://069059b7ef-1ytapi01.1ytsub.com',
'https://0d2th.no-mad-world.club',
'https://0e321902-dbed-4a68-9561-901b83ce9a4b.xn--l6qx3lcvp58x.com',
'https://0mv.top',
'https://1.bethebest.eu.org',
'https://1.mjjclub.top',
'https://1.xn--xc3ao8r.top',
'https://10th.sub-airport.com',
'https://12123.org',
'https://12222.xn--yfr360ebxhhsu.com',
'https://123abc.love',
'https://123x6y9z.d01olikp.thesyeec7l60ouav1lz0tesk.top',
'https://135841.xyz',
'https://15212712-20f5-40a5-b9aa-8363e0130171.ee137666-1e0a-46db-bbd6-cc18f9841234.accesscam.org',
'https://16th.sub-airport.com',
'https://17852.xyz',
'https://196284.nginxzfd.xyz',
'https://1st.sub-airport.com',
'https://1ytcom01.1yunti.net',
'https://20240802.canadapost-vip.com',
'https://20240913.sux.lol',
'https://231787.xyz',
'https://25054128.xyz',
'https://3.feiniaoyun01.life',
'https://3.mimoe4.ru',
'https://30178aeb-8299-045d-fb67-ae12ce73dd2c.buou.lol',
'https://30388d70-6f5c-4d7c-8daa-9d3df7c5c526.9150e878-8296-4798-a172-c3fe66b8dee5.ddnsgeek.com',
'https://3093492f6b2332f8server.lycoris.one',
'https://353g78qgfq.surfcat.store',
'https://38.181.25.67',
'https://3dxre.no-mad-world.club',
'https://3h.lv',
'https://3ra4214.tjsd.site',
'https://41be350f-5079-4195-8329-f6fa25f9906a.com',
'https://42.194.232.60:10387',
'https://422.jcool.cool',
'https://4259f1e1-ff0e-461a-b7ff-c734d374eb68.shandiannginx.com',
'https://45bcb080ade759e2.cdn.jiashule.com',
'https://47.237.21.85',
'https://47.239.42.117',
'https://47.242.186.70',
'https://4e60bafd-0633-4e8d-a02a-eef51cd1ad8e.xn--mes358a.art',
'https://4t7n4.subxly.cfd:8443',
'https://4ulgur4.wuxianliuliang.cfd',
'https://520.qjfjc.top',
'https://523qaweg246.pandafly.site',
'https://569cdn.1010520.click',
'https://595780.xyz',
'https://66c4d4.brighthorizon.cc',
'https://66c6d6.whisperingbreeze.cc',
'https://68123106-3e43-4958-b75a-b06e81eabf79.50d88e28-a870-497d-bf87-c20fb6802871.camdvr.org',
'https://6GWNE.subxly.cfd:8443',
'https://711.886511.xyz',
'https://78fb170a-8f5c-46e9-991c-2b12fe04c1d1.xn--mes358a.art',
'https://7cd49968.nmsubs.com',
'https://7jyrf.no-mad-world.club',
'https://8088.hssl8088.icu',
'https://893996753.xyz',
'https://8payj.no-mad-world.club',
'https://911tg3rs.com',
'https://9527.bigbigwatermelon.com',
'https://99ding.men',
'https://9bd4028e.ghelper.me/subs',
'https://9ddea9039d074ed4.cdn.jiashule.com',
'https://JpjfL54G.subxly.cfd:8443',
'https://NcLAhc.subxly.cfd:8443',
'https://QTjDQsor6e7D.configbit.com',
'https://YQZQQHGLWm.prosubnet02.eu:8443',
'https://a.aikllc.tech',
'https://a.fsyun.xyz',
'https://a.jiedianxielou.workers.dev',
'https://a.mtdwoodwork.com',
'https://a.qcsub.top',
'https://a.s2cat.cc',
'https://a.sdwan.im',
'https://a.suixincloud.top',
'https://a1.8jiasu.com',
'https://a241219.888545.xyz',
'https://a2673b60-aca1-48c2-a4ad-abeb518e18f9.fengchenginx.com',
'https://a2789293-639e-49f5-9506-c8040b488438.nginxxy.xyz',
'https://a76.aaa7.info',
'https://a94d418e-1898-42df-bcf2-d970a5f3a939.mysubsoft.com',
'https://aa.dabai.in',
'https://aaa.us123.icu',
'https://aaa.yunduanjc.top',
'https://aaaa.gay',
'https://ab.dabai.in',
'https://abyssvpnya.net',
'https://ac1f3b35-1d03-3a85-beab-258d8f23edc6.nginxdotu.xyz',
'https://ac59a7cd-11af-3e35-a098-b785688ec627.aliyunsub.com',
'https://acl.syyn.pw',
'https://admin.nezha.su',
'https://adtzwnkwqq.southeastasia.cloudapp.azure.com',
'https://ae86.235999.xyz',
'https://af078381-fcf9-457a-b03a-7bfaf506cd0b.xn--l6qx3lcvp58x.com',
'https://afun-waf.trafficmanager.net',
'https://ag.bnpm.dynu.net:30443',
'https://aicccc.top',
'https://aifun.trafficmanager.net',
'https://aigame.totwo.xyz',
'https://aini.200566.xyz',
'https://air.nicetive.site',
'https://airport.raloar.top',
'https://alpha.sagittarius-link.com',
'https://ap.niubi.site',
'https://api-hx.02000.net',
'https://api-qw.02000.net',
'https://api-zz.xn--14ra41gd24b.xyz',
'https://api.1vpn.sbs',
'https://api.abyssyun.top',
'https://api.acaisbest.shop',
'https://api.bigme.online:8211',
'https://api.e687699.top',
'https://api.e986532.top',
'https://api.fanss.vip',
'https://api.fenghuolun.xyz',
'https://api.fuckvps.net',
'https://api.fuckyun.cc',
'https://api.heima2u.com',
'https://api.hy2.lol',
'https://api.otcopusvpn.cc:18008',
'https://api.pithecia.com',
'https://api.prprcloud.life',
'https://api.ssrsub.com',
'https://api.touhou.center/sub',
'https://api.tshl.cc',
'https://api.xinyo.vip',
'https://api.xn--14ra41gd24b.xyz',
'https://api.xn--y20az5i.xyz',
'https://api.xn--yfr72t8r4bvhd.xyz',
'https://api.xqc.best',
'https://api.xtt777.com',
'https://api.xyurl.site',
'https://api.ymvpnpro.cc:8700',
'https://api.zzzzzl.me',
'https://api03.cjpaoche.xyz',
'https://api1.441166.xyz',
'https://api1.danidapigu.top',
'https://api1.fzdwf.top',
'https://api1.okaycloud.top',
'https://api1.xn--bnq37rc0nw50b.com',
'https://api2.mbo-xxx.top',
'https://api2.okaycloud.top',
'https://api2.xn--bnq37rc0nw50b.com',
'https://api3.6yuan.top',
'https://api7.6yuan.top',
'https://apiceshi.51alibaba.top',
'https://apidy.pqjc.site',
'https://apisub.mcwy.xyz',
'https://apisudunw.sudunv.com',
'https://apiv2.lemongg.top',
'https://apiv2.lipulai.com',
'https://apopcloud.com',
'https://app.cloudlion.me',
'https://app.gomeow.cloud',
'https://app.jisovpn.site',
'https://app.legeth.cc',
'https://app.lwjyj.com',
'https://app.tline.website',
'https://aq.louwangzhiyu.xyz',
'https://artislg.com',
'https://artislg.com/api',
'https://asa.lol',
'https://asa01.888545.xyz',
'https://asa035.888545.xyz',
'https://asdf.888545.xyz',
'https://atacyun.yydsii.com',
'https://atong88.top/klBrvxTYgGdWoqF0cLRi4AS93S',
'https://auth.newlikebooks.xyz',
'https://awacloud.online',
'https://b.jiedianxielou.workers.dev',
'https://b.xiaow.cc',
'https://b27479ca-869b-4d02-9e53-a3d6d7785d13.nginxmdss.xyz',
'https://baigou.kkhhddnn.cn',
'https://bajie.info',
'https://bajie.xyz',
'https://bansub7.bplink.xyz',
'https://bansub8.bplink.xyz',
'https://base64.bigwatermelon.org',
'https://bat.fcbjw.com',
'https://bav46z6c.nicecloud.win:8443',
'https://bayoeorescentpossessicoanseparateuneforescenphocommitte.adoptangelaboradvacotionclwonthorughconfrmcompimentdeseertaltar.org',
'https://bb.jmvks.cn',
'https://bbg.bbgjc.cc',
'https://bbgjc.cc',
'https://bbjc.xyz',
'https://bdsafhh.yiyuanlx.cc',
'https://bengalj.com',
'https://blueAir.colacloud.free.hr',
'https://board.nsde.date',
'https://board.queqiao.online',
'https://boou.colacloud.free.hr',
'https://bozhi.591haoka.com',
'https://bpjc.lol',
'https://bptz.xyz',
'https://bunnyspeedox.online',
'https://butppo.473221.xyz',
'https://bxy.re',
'https://c.066664.xyz',
'https://c3.notesync.org',
'https://c4.notesync.org',
'https://cainiao164.top',
'https://cainiao172.top',
'https://cainiaofit.cc',
'https://cat.ikkt.cn',
'https://cdn-web-api.moeu.top',
'https://cdn.1454250.xyz',
'https://cdn.fraternizey.com',
'https://cdn.qfyun.me',
'https://cdn.wumaojichang.com',
'https://cdn1.xr56385d.qianglie.cloud',
'https://cdn1711437153.ppgnginx.com',
'https://cdn1712594108.ppgnginx.com',
'https://cdn1715497317.ppgnginx.com',
'https://cdnbao.foxi4.com',
'https://cedb4ccc-89b7-3a24-962c-ea8f65b11deb.aliyunsub.com',
'https://ceshi.888451.xyz',
'https://cf.7854128.xyz',
'https://cf.lemshow.top',
'https://cf.loveqyun.cyou',
'https://cfj.chuifengji.top',
'https://cfyun.top',
'https://cfyun01.sbs',
'https://chaozhijc.xyz',
'https://checkhere.top',
'https://chiguayun.pro',
'https://china.huawei-cloud.shop',
'https://citi.terminal69.win',
'https://ck2.yunxiangvip.mom',
'https://cloud.anyijc.top',
'https://cloud.asdkd.top',
'https://cloud.chaozhijc.xyz',
'https://cloud.gomeow.tech',
'https://cloud.gyyun.top',
'https://cloud.jsfx.tech',
'https://cloud.optionwiney.com',
'https://cloud.xjyjc.top',
'https://cloud.ykkk.tech',
'https://cloud.yydschina.top',
'https://cloudcat.top',
'https://cloudflaresub.yuwan.link',
'https://cloudlion.me',
'https://cm.qc77.cn',
'https://cococloud.online',
'https://cokecloud.net',
'https://config.huojian111.com',
'https://csgo.fask511.cfd',
'https://csgo1.fask511.cfd',
'https://cshjc.xz61.cn',
'https://csicd782-isu.acyunv.buzz',
'https://csyun.t1csyun.shop',
'https://cyberguard.cfd',
'https://d.palu123.com',
'https://d.waka.plus',
'https://d1.dlsdist.net',
'https://d1to2me5cb4qc0.cloudfront.net',
'https://d2f42a86-2a1f-49b5-bd2f-d2154daa6a09.com',
'https://d3keb6jjtp861e.cloudfront.net',
'https://d57761d6-e86d-4f55-9a5d-aece8a55cc26.xn--mes358a.art',
'https://dadada.acaisbest.com',
'https://dash.djjc.cfd',
'https://dash.ftclashcloud.mom',
'https://dash.pqjc.site',
'https://dash.yfjc.xyz',
'https://datacenter_us.pithecia.com',
'https://datmicxg.mdssconfig.com',
'https://dawson0207.xn--3iq226gfdb94q.com',
'https://daxun.buzz',
'https://dd.csjc.win',
'https://dd.moonriver.cfd',
'https://dd.xz61.cn',
'https://ddd.trc20.top',
'https://df810594c639v.cloudfront.net',
'https://dfgsdfg.ghkjfgjkdfghrjfghjvbnm.cfd',
'https://dingyue.trojanws.xyz',
'https://dingyue.wenlianyun.vip',
'https://dingyue.xxss.org',
'https://dingyue1.b-cdn.net',
'https://dj.taipeicity.news',
'https://djjc.cfd',
'https://dkcc71fg830ah.cloudfront.net',
'https://dl.owokkvsxks.store',
'https://dl.vfkum.website',
'https://doata.net',
'https://doucat.top',
'https://douyun.sbs',
'https://duijie.cfyun.top',
'https://duijie.pingziyun.top',
'https://dump.facal.one',
'https://dxapp.jmvks.cn',
'https://dy-1.smjcdh.com',
'https://dy.chaozhijc.xyz',
'https://dy.jntm.ikun.moshen.tech',
'https://dy.kuailejc.xyz',
'https://dy.kunkun.v6.navy',
'https://dy.magicm.link',
'https://dy.naisicloud.xyz',
'https://dy.netfly.sbs',
'https://dy.pmy666.xyz',
'https://dy.qjfjc.top',
'https://dy.shihuijeidian.xyz',
'https://dy.smjc.top',
'https://dy.ssysub6.xyz',
'https://dy.tagsub.net',
'https://dy.tgmini.top',
'https://dy.tsmpi.xyz',
'https://dy.ucat.live',
'https://dy.yh13.xyz',
'https://dy0.mmydy.xyz',
'https://dy01.mmydy.xyz',
'https://dy1.hhyun.in',
'https://dy1.mmydy.xyz',
'https://dy2.mmydy.xyz',
'https://dy3.yunhu1.xyz',
'https://dy4.mmydy.xyz',
'https://dy5.mmydy.xyz',
'https://dy513.mmydy.xyz',
'https://dy6.mmydy.xyz',
'https://dy7.mmydy.xyz',
'https://dy9.mmydy.xyz',
'https://dyapp123.355m.cn',
'https://dycd.gsjc.sbs',
'https://dycd.knjc.cfd',
'https://dydz.csjc.win',
'https://dydz.xn--mesv8bx6xtx3b.com',
'https://dylj.wanwan1024.top',
'https://dyvip.ianong.cn',
'https://dzpd.jiedianxielou.workers.dev',
'https://e1452652-32ee-b946-e3e7-d9be7070058e.buou.lol',
'https://edu.dianping.men',
'https://edu.kuaifaka.me',
'https://ee7b114b-2dff-4e9d-b427-4d1c2ac2e12f.fengchenginx.com',
'https://efxxl.xyz',
'https://eggtartcloud.biz',
'https://faf047da-5e7e-4da7-8414-2799d48ad63a.nginxcatnet.xyz',
'https://falco.656266656.xyz',
'https://falco.pwzvd.cn',
'https://falcocloud.730894.xyz',
'https://fast.gfwstable.icu',
'https://fast.yt/sub',
'https://fast1.baipiaoi489hy0p44ty.xyz',
'https://fb.umgtb.cn',
'https://fbapiv2.fbsublink.com',
'https://feichanghaotlszuduanshiwodeyumingxuanzhuan.esucloud.com',
'https://feima.xn--fiqr3f3yq87hgq1c.com',
'https://feiniaoyun.top',
'https://feiniaoyun11.life',
'https://fellayun.cc',
'https://fengqunvpnvip.jmvks.cn',
'https://ff3a7d92-7568-4cca-a053-37087bee70b7.xn--mes358a.art',
'https://fgsfgs.12306.sbs',
'https://fhcloud.gweuc.cn',
'https://fhfdf.ghkjfgjkdfghrjfghjvbnm.cfd',
'https://fly.j-s.us.kg',
'https://fly0001.buzz',
'https://flybit.pages.dev',
'https://fn1.170809.xyz',
'https://followcloud.space',
'https://forks.giegie.loan',
'https://free.andiliba.cc',
'https://free.cfnode.shop',
'https://free.colacloud.free.hr',
'https://free.kcjs.me',
'https://free.ninecloud.co',
'https://free2.govmail.top',
'https://freeflyingcloud.com',
'https://freejc.xyz',
'https://fs123121.cdn.22.jiacdnd123456789.com',
'https://fuqing.ch',
'https://fxjc.xyz',
'https://gates.djjc.cfd',
'https://gateway.51tu.lol',
'https://gauss.life',
'https://gauss.lol',
'https://gawrgura.moe',
'https://gbshct.spphhnhg.top',
'https://gbtgurl.me',
'https://get.biu001.xyz',
'https://get.getccad.top',
'https://get.ninesub.us.kg',
'https://getafreenode.com',
'https://getinfo.bigbigwatermelon.com',
'https://getinfo.bigwatermelon.org',
'https://gfdlaw9.xiaoliyu.xyz:8443',
'https://gg2.hneko.buzz',
'https://ggiuwegivhe123.a123.bond',
'https://go.hhyun.in',
'https://grslfa.clashx.app',
'https://gs.kkhhddnn.cn',
'https://gsea.buzz',
'https://gsjc.sbs',
'https://guolicheng.cfd',
'https://guq3tjlp.subxly.cfd:8443',
'https://gx.591haoka.com',
'https://gyyun.top',
'https://h.bbydy.org',
'https://haitunyun.online',
'https://helloworld-gkhnaabtdcefa9d5.z01.azurefd.net',
'https://hh.haibucuo.xyz',
'https://hh.hnekoo.top',
'https://hktixcloud.pwzvd.cn',
'https://host.ssrbox.com',
'https://hrqiea.subxly.cfd:8443',
'https://hsaii.mejd.cn',
'https://htcmi-20240805.mozhiti.top',
'https://htdy02.mozhiti.top',
'https://huahe.link',
'https://huaikhwang.central-world.org',
'https://huaxia.tcekx.cn',
'https://huaxia.wueh.cn',
'https://huotuichang.top',
'https://hutaod.com',
'https://hx0618.xn--wqr30o34q.xn--io0a7i',
'https://hy-2.sbs',
'https://iBrRN.subxly.cfd:8443',
'https://iconsiam.terminal69.win',
'https://ierboryt.spphhnhg.top',
'https://ifaner.dd94wan.com',
'https://ihjlkbcueiwqnwior.duboji.vip',
'https://ikuajingbus.com',
'https://inangua.lwjyj.com',
'https://info.iic08924f5w3b65o.xyz',
'https://ins77.link',
'https://install.cdn-sd.xyz',
'https://ipngc.no-mad-world.club',
'https://j2s.buzz',
'https://jb.taipeicity.news',
'https://jc.sux.lol',
'https://jc.wuxianjc.top',
'https://jilu.uuvpn.xyz',
'https://jindoucloud.xyz',
'https://jindouyun88.life',
'https://jisovpn.site',
'https://jiumaojiu.jiumaojiu.net',
'https://jixingnetwork.sbs',
'https://jlhcloud.us.kg',
'https://jp.taishan1.pro',
'https://jshou.top',
'https://jsjc.cfd',
'https://jxpodzmq93s8etq0.wmcssw.org',
'https://k61kz.no-mad-world.club',
'https://kaochang.click',
'https://ki.hello1.xyz',
'https://kiking1223.xn--49st2e1z0f.xn--55qx5d',
'https://kitsch.xn--8stx8olrwkucjq3b.com',
'https://knjc.cfd',
'https://kobee.metatai.xyz',
'https://koumakan.quickline.top',
'https://ktmcloud.cc',
'https://ktmcloud.club',
'https://ktmcloud.co',
'https://ktmcloud.cool',
'https://ktmcloud.fun',
'https://ktmcloud.life',
'https://ktmcloud.link',
'https://ktmcloud.lol',
'https://ktmcloud.me',
'https://ktmcloud.men',
'https://ktmcloud.win',
'https://ktmcloud1.club',
'https://kuailejc.xyz',
'https://l.db-link01.top',
'https://lafuseevansbazc.only4subs.uk',
'https://lancloud.zichuanlan.top',
'https://lbxjc.online',
'https://let.bnsubservdom.com',
'https://liangyuandian.xyz',
'https://lianjia.me',
'https://lianjiajichang.com',
'https://lianjiasub.work',
'https://lianjievpn.com',
'https://linger.cc',
'https://link.esnclink.com',
'https://link.yes-elegant.world',
'https://link01.fliggylink.xyz',
'https://link01.pikachucloud.site',
'https://link02.pikachucloud.site',
'https://link1.db-sub.xyz',
'https://link2.proxylink.xyz',
'https://link4.proxylink.xyz',
'https://link5.proxylink.xyz',
'https://linka.lmscunb.cc:2087',
'https://llgjc.shop',
'https://lmaff01.lmspeed.co',
'https://lmjc.xyz',
'https://login.djjc.cfd',
'https://login.yfjc.xyz',
'https://ly.ccwink.cc',
'https://lzysub.online',
'https://m11.spwvpn.com',
'https://m2net.lol',
'https://m2net.sbs',
'https://m33.spwvpn.com',
'https://m4y2z.no-mad-world.club',
'https://magicae.pics',
'https://maho.chipsfuck.fish',
'https://maple.icu',
'https://mdmmra.subxly.cfd:8443',
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
'https://movie2.dianying.lat',
'https://mro5n.no-mad-world.club',
'https://music.easygourl.xyz',
'https://my.335570.xyz',
'https://my.cat66.lol',
'https://my.catfaka.com',
'https://my.mingri.icu',
'https://mydy.xlm.plus',
'https://myko.buzz',
'https://mymy.lanyanyun.co',
'https://mysub.cc',
'https://mytoken-1.huyun.nl',
'https://mytoken.huyun.nl',
'https://myu.best',
'https://n3.leensasub.net',
'https://nachoneko.cn',
'https://naiyun0315.xn--8stx8olrwkucjq3b.com',
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
'https://ni8.zxm.cc',
'https://ninjasub.com',
'https://nmsubs.com/interface',
'https://nn0310.xn--8stx8olrwkucjq3b.com',
'https://nn8qozmu.nn8qozmu.top',
'https://node.666666222.xyz',
'https://node.yifang02.men',
'https://node.zasublinkv1.com',
'https://nogin.djjc.cfd',
'https://nsm5o.no-mad-world.club',
'https://nuonuonet.uk',
'https://o7pl1.no-mad-world.club',
'https://oiiccdn.yydsii.com',
'https://okztwo.com',
'https://on1vejas4m6z.w7yxefcx0i11.click',
'https://onlysub.mjurl.com',
'https://osjdkdkk6469uajsm197.xn--5hqx9e52gdss.xyz',
'https://oss.pithecia.com',
'https://pavo.eu.org',
'https://pdda.me',
'https://pfjc.im',
'https://pincht.sbs',
'https://platform.djjc.cfd',
'https://pp.hnekoo.top',
'https://pqjc.site',
'https://pro.76898102.xyz',
'https://pro.xn--l9qyaz082a.cn',
'https://proa.xn--l9qyaz082a.cn',
'https://prob.xn--l9qyaz082a.cn',
'https://proc.xn--l9qyaz082a.cn',
'https://protal.xfxun.com',
'https://proxyinfo.net',
'https://pvn4hq.subxly.cfd:8443',
'https://pvn4hq.xiaoliyusub.top:8443',
'https://qianggewangluo.cc',
'https://qidijichang.xyz',
'https://qingchayun.icu',
'https://qkt83qnp2yuj.subconnect.org',
'https://qq.xlm.plus',
'https://qwe.097482.xyz',
'https://qwerzfdsfgrtds.mejd.cn',
'https://qxuig4.youxuan.wiki',
'https://qyoo.aibvs.cn',
'https://record.piao.news',
'https://rgergergergerg6555.saojc.xyz',
'https://rockvpn.4bmg9.online',
'https://rss-node.com',
'https://rss.biteb-sub.com',
'https://rss.paoluz.xyz',
'https://rss2024.jkl-sub.com',
'https://rss202407.mugua-sub.com',
'https://rsslinghun1.xyz',
'https://rxxqa.no-mad-world.club',
'https://s.33y.run',
'https://s.feisucloud.xyz',
'https://s.hajimi.icu',
'https://s.jiasu01.vip/bd',
'https://s.jockerchief.online',
'https://s.kalaa.me',
'https://s.kingarthor.online',
'https://s.princeseed.online',
'https://s.qzsub.live',
'https://s.suying666.info',
'https://s.youyun666.site',
'https://s1.bnpublicsub.com',
'https://s1.byte16.com',
'https://s1.daxun-link.com:8888',
'https://s1.iajsy.lol',
'https://s2.equinoxaa.com',
'https://s2.sub.gfw.gg',
'https://s6.ssysub1.xyz',
'https://s7.sub.gfw.gg',
'https://sakuracat1203.xn--3iq226gfdb94q.com',
'https://sanguayun.jiumaojiu.net',
'https://sb.swiftnet.cloud',
'https://sbs.fastfly.life:21600',
'https://sbsqwzfgh.santoku.cn',
'https://sdgvps.com',
'https://service-69kfaex1-1312645837.bj.apigw.tencentcs.com',
'https://service-6l9168iy-1312645837.gz.apigw.tencentcs.com',
'https://service-avmn443l-1312645837.sh.apigw.tencentcs.com',
'https://service-bmp1m9zg-1312645837.nj.apigw.tencentcs.com',
'https://service-e6np5k91-1312645837.sh.apigw.tencentcs.com',
'https://service-fy4hli0a-1312645837.nj.apigw.tencentcs.com',
'https://service-jr6u1e7c-1323936013.hk.tencentapigw.cn',
'https://service-p0v9tp46-1312645837.gz.apigw.tencentcs.com',
'https://shiyuanyinian.passwallwall.world',
'https://sinhvien4g.com',
'https://sinsocloud.top',
'https://smallairport-first-sub.top',
'https://snangua.com',
'https://soonlink.xn--wqr30o34q.xn--io0a7i',
'https://spr.278986.xyz',
'https://sq9xy6.cpminig.com',
'https://ss.81dlg.com',
'https://ss.cft.my',
'https://ss.hxcq.cc',
'https://ss.suyunti.cc',
'https://sss.xn--4gqt91ntld.space',
'https://ssvpn.org',
'https://st-sub.fly.dev',
'https://starlinkcloud.club',
'https://starlinkcloud.xyz',
'https://study1.v1999.sbs',
'https://su-b.yun.cat',
'https://su.hhbggy.com:8888',
'https://su.xfjhchr.com:8888',
'https://sub-01.767564.xyz',
'https://sub-go.xqxa.xyz',
'https://sub-jam.cfd',
'https://sub.19993999.xyz',
'https://sub.200566.xyz/share',
'https://sub.591haoka.com',
'https://sub.abcdefghijklmnopqrstuvwxyz1234567890.xyz',
'https://sub.alice.sale',
'https://sub.andaofu.xyz',
'https://sub.bailian.site',
'https://sub.bbjc.xyz',
'https://sub.bxy.org.uk',
'https://sub.cdcloud.mingri.icu',
'https://sub.cfnode.shop',
'https://sub.chasing.sbs:21600',
'https://sub.cjcloud.cc',
'https://sub.cloudlion.me',
'https://sub.cloudog.us.kg',
'https://sub.coo.ga',
'https://sub.cucloud.top',
'https://sub.czrk168.top',
'https://sub.dawanqukun.top',
'https://sub.daxun-link.top',
'https://sub.domiw.com',
'https://sub.feiji.ddns-ip.net',
'https://sub.fnf.one',
'https://sub.fnf.xyz',
'https://sub.gomeow.online',
'https://sub.gougou.live',
'https://sub.hktix.net',
'https://sub.jileiyun.top',
'https://sub.jileiyun.us.kg',
'https://sub.kaolacloud.site',
'https://sub.lingche.icu',
'https://sub.lzyjc.xyz',
'https://sub.marsix.cc',
'https://sub.mianfeiyun.online',
'https://sub.miaosusub.cfd',
'https://sub.miku.llc',
'https://sub.minizz.online',
'https://sub.mogufan.com',
'https://sub.netv2.cc',
'https://sub.nex7.us.kg',
'https://sub.no626.link',
'https://sub.nodeup.top/IBMQR',
'https://sub.nysubs.xyz',
'https://sub.onlineweb.work',
'https://sub.ouoboom.xyz',
'https://sub.passgfw.top',
'https://sub.pddf.shop',
'https://sub.pianyi.info',
'https://sub.pianyijichang.com',
'https://sub.qingfengyun.icu',
'https://sub.sanfen014.xyz',
'https://sub.sanfen017.xyz',
'https://sub.sanfen018.xyz',
'https://sub.sanfen021.xyz',
'https://sub.sanqianlijinxiuheshan.us.kg',
'https://sub.sheepcloud.xyz',
'https://sub.speed17sub.com',
'https://sub.sqfly.site',
'https://sub.sslinks.co.in',
'https://sub.ssr.sh',
'https://sub.tangping.cloud',
'https://sub.tianmaojichang.us.kg',
'https://sub.tku2.com',
'https://sub.tuanzi.site',
'https://sub.tuanzi.xyz',
'https://sub.tudou213.com',
'https://sub.vpntz.com',
'https://sub.vvcloud.us.kg',
'https://sub.wordvlog.link',
'https://sub.wukong.bond',
'https://sub.xiaomf.store',
'https://sub.xinyo.vip',
'https://sub.xn--14ra41gd24b.xyz',
'https://sub.xn--4gq62ffxz.net',
'https://sub.xn--4gq62fv6r4w0c.com',
'https://sub.xn--4gqp1u.com',
'https://sub.xn--9kqu5y58a.com',
'https://sub.xn--ioru3fc2t1hb.com',
'https://sub.xn--mesv7f5toqlp.com',
'https://sub.xn--wlqw2sc0nwqq.com',
'https://sub.xunlian.site',
'https://sub.yifenjichang.online',
'https://sub.yiri.dev',
'https://sub.yslink.cc',
'https://sub.yspeeds.uk',
'https://sub.yun.cat',
'https://sub.yz006.xyz',
'https://sub.zingfast.vn',
'https://sub01.jishu168.xyz',
'https://sub1.bbjc.xyz',
'https://sub1.efshop.cc',
'https://sub1.haiqilai.lol',
'https://sub1.huy.0.srl',
'https://sub1.jiatelin.cyou',
'https://sub1.ktyyun.com',
'https://sub1.liangxinjichang.com',
'https://sub1.smallstrawberry.com',
'https://sub1.tg-mfjd666.cloudns.be',
'https://sub1.timeneverchanges.com',
'https://sub1.twoyuanfun.online',
'https://sub1.xn--mesv7f5toqlp.com',
'https://sub2.591haoka.com',
'https://sub2.91qaq.lol',
'https://sub2.bighneko.top',
'https://sub2.download-hiccup.xyz',
'https://sub2.smallstrawberry.com',
'https://sub2.yunanyun.xyz',
'https://sub3.bbjc.xyz',
'https://sub3.gfw.gg',
'https://sub3.hanghai.xyz',
'https://sub3.huy.0.srl',
'https://sub3.jie-quick.buzz',
'https://sub3.mi.huy.ooo',
'https://sub3.smallstrawberry.com',
'https://sub3.yunanyun.xyz',
'https://sub4.91qaq.lol',
'https://sub4.bbjc.xyz',
'https://sub4.download-hiccup.xyz',
'https://sub4.gfw.gg',
'https://sub4.haiqilai.lol',
'https://sub4.huy.0.srl',
'https://sub4.yljc.online',
'https://sub4.yunanyun.xyz',
'https://sub5.gfw.gg',
'https://sub5.huy.0.srl',
'https://suba.lingche.icu',
'https://subcdn.cos.cat',
'https://submit.xz61.cn:22443',
'https://submit.xz61.cn:23443',
'https://subneko.v1999.sbs',
'https://subone.xyjc.xyz',
'https://subpanghujichang.xn--y20az5i.xyz',
'https://subs.doubao.one',
'https://subs.manatraffic.top',
'https://subs.pithecia.com',
'https://subs.xttlove.uk',
'https://subscribe.cloudlion.me',
'https://subscribe.cloudlion.top',
'https://subscribe.famint.net',
'https://subscribe.fastsocks.xyz',
'https://subscribe.iint.cc',
'https://subscribe.insidergame.xyz',
'https://subscribe.speedypro.xyz',
'https://subscribe.suwas.xyz',
'https://subscribe.xsus.net.co',
'https://subscribe.xxmad.com',
'https://subscribe.ztpxxx.com',
'https://subscribe2628.lanmaoyun.icu',
'https://subscribe3.000000online.life',
'https://subscribe511295.fengqun.info',
'https://subscribe85687.fengwo.info',
'https://subscription.slshenlong.top',
'https://subscriptionruc.slshenlong.top',
'https://subsubsubsubsub.keledydz.uk',
'https://subtest.mojc.xyz',
'https://subthree.996yyds.xyz',
'https://sulian.cc',
'https://sulian.life',
'https://sus.alicenetwork.cloud',
'https://suscribethenetword.beecloud.club',
'https://sux.lol',
'https://svip.365cloud.me',
'https://svip.dovenweb.com',
'https://swiftnet.wiki',
'https://syt.sytcloud.top',
'https://syyn.ianong.cn',
'https://syyn.xyz',
'https://syynweb.shop',
'https://syynweb.xyz',
'https://szdol.com',
'https://taoyuanjiasu.com',
'https://tcxf.hssl8088.icu',
'https://texon.io/portal/subscribe/546',
'https://thepoint1.free886.site',
'https://tiktokcn.xyz',
'https://time1717401601.nginxcaiyun.xyz',
'https://time1721057549.nginxcaiyun.xyz',
'https://tokenapi.fbcloud.lol',
'https://toysforyou.top/sub',
'https://ttc01.xyz',
'https://tudou.igken.com',
'https://tugeda.xyz',
'https://tuzi226.top',
'https://tv.modemhub.work',
'https://tz.vfkum.website',
'https://u4dqz2t0x576.syynweb.shop',
'https://upm8kfu.nicecloud.win:8443',
'https://url.409648.xyz/data',
'https://url.funhub.cc',
'https://url.mtdwoodwork.com',
'https://us.freecat.cloud',
'https://user.1vpn.sbs',
'https://user.dafeiji.one',
'https://user192.dukadi.one',
'https://user413.dukadi.one',
'https://user9125.eyudy.one',
'https://v.spwvpn.com',
'https://v2.545155.xyz',
'https://v2.ixlmo.com',
'https://v2.ixlmo.net',
'https://v2.udid8.com',
'https://v2b.hinetlove.site',
'https://vase.bengalj.com',
'https://vdmwy.itr.lol/link',
'https://vip.365cloud.me',
'https://vip.sgjc.top',
'https://vips.lol',
'https://vodfavor.top',
'https://vot.278986.xyz',
'https://vot.689861.xyz',
'https://vot.981176.xyz',
'https://vpn.linuxdo.pro',
'https://vpn6688.com',
'https://vt.louwangzhiyu.xyz',
'https://vtwoc1.top',
'https://vtwoc3.top',
'https://vyyy.vyunyunnode.top',
'https://wEHx49R5Z4CJWf9iNF0r.yun.cat',
'https://wangdazhuang.top',
'https://wap.nnpy.org',
'https://watch.szlatteart.com',
'https://wd-blue.com',
'https://wd-purple.com',
'https://wdsl88cc-sl.shenlong.wiki',
'https://web.coo.wiki',
'https://web.tline.website',
'https://web888.naixue222.com',
'https://web888.naixue222.net',
'https://webget.yfjc.xyz',
'https://webridge.pokeryun.link',
'https://wf.nekros.us',
'https://wg03u.no-mad-world.club',
'https://widget.yfjc.xyz',
'https://within.sephirah.icu',
'https://wjkc123.com',
'https://wly312.buzz',
'https://wm01dy.wmyun.men',
'https://wow.dogss-host.bond',
'https://wow.dogss-host.store',
'https://wub.zongyunti.site',
'https://wukong.baiwk.top',
'https://wumao.jiumaojiu.net',
'https://wvw.guanxi.cloudns.be',
'https://wwe.trx1.cyou',
'https://wws.s2fjeyeeyafe.bond',
'https://www.02er.com',
'https://www.360vpn.org',
'https://www.998877.best',
'https://www.antlink.cc',
'https://www.awa520.cloud',
'https://www.awyyds.one',
'https://www.baiyunvpn.xyz',
'https://www.bitduct.net',
'https://www.bptz.xyz',
'https://www.bqg888.com',
'https://www.catssr.host',
'https://www.catssr.one',
'https://www.catssr.top',
'https://www.catssr.xyz',
'https://www.ccsub.online',
'https://www.ccsub.org',
'https://www.chaojijichang.com',
'https://www.chituma.top',
'https://www.cloudshops.xyz',
'https://www.crosswall.org',
'https://www.cwy-water.us.kg',
'https://www.dabai.in',
'https://www.dma.icu',
'https://www.elinksapi.com',
'https://www.fdzdk.xyz',
'https://www.flyintpro01.com',
'https://www.flyintpro05.com',
'https://www.freeflyingcloud.xyz',
'https://www.ftclashcloud.mom',
'https://www.ginfem.com',
'https://www.hneko.world',
'https://www.itonlyasub.xyz',
'https://www.kuaidog008.top',
'https://www.kuaidog010.top',
'https://www.laoniu49.top',
'https://www.lbxjc.online',
'https://www.liangyuandian.at',
'https://www.liangyuandian.life',
'https://www.louwangzhiyu.xyz',
'https://www.m2net.cc',
'https://www.m2net.lol',
'https://www.miyun.me',
'https://www.mojie.cool',
'https://www.moonriver.sbs',
'https://www.mysubsoft.com',
'https://www.mz-fast.net',
'https://www.nertron.net',
'https://www.otcopusapp.cc',
'https://www.paofusub2.com',
'https://www.pddc.me',
'https://www.pkqcloud.com',
'https://www.qlgq.top',
'https://www.sstank.top',
'https://www.stewed.top',
'https://www.tannel.xyz',
'https://www.tianxianbaby.com',
'https://www.tiziwrops.com',
'https://www.tline.website',
'https://www.v2youzi.top',
'https://www.vtwoc4.top',
'https://www.w1y1.xyz',
'https://www.wexgc.com',
'https://www.xingsu.club',
'https://www.xmfsubscribe.com',
'https://www.xn--5hqx9equq.org',
'https://www.xn--9kq89dn23b.top',
'https://www.xn--gmq09hwyu.fun',
'https://www.ye-xiao.top',
'https://www.yfjc.xyz',
'https://www.yiyuanjichang.net',
'https://www16.bigairport-eleventh-sub.top',
'https://www6.1st-subscription-from-chickenfarmer.top',
'https://www6.2nd-subscription-from-chickenfarmer.top',
'https://www8.6th-subscription-from-chickenfarmer.top',
'https://www8.bigairport-fourteenth-sub.top',
'https://wwwjs.pro',
'https://x.dnsss.top',
'https://x.nsa.cc',
'https://xb.feiyi.mom',
'https://xb1.nets.pp.ua',
'https://xboard.sswiwi.com',
'https://xboard.texo.network',
'https://xf88j.no-mad-world.club',
'https://xfsnet.com',
'https://xhtoken.huyun.nl',
'https://xingcloud.659747.xyz',
'https://xingcloud.pwzvd.cn',
'https://xn--14ra41gd24b.xyz',
'https://xn--2dk290r.xn--p8jhn1a2d1epgoe.com',
'https://xn--94q649dc94a.com',
'https://xn--9krt36k.com',
'https://xn--cp3a08l.com',
'https://xn--ehq91fquq.com',
'https://xn--mest48anb1j.com',
'https://xn--mesz9ptugxg.com',
'https://xn--pbt777k.art',
'https://xn--pssq69d.xyz',
'https://xn--vpn-rw7eh25o.com',
'https://xn--vuqy45c.top',
'https://xn--wlqw2sc0nwqq.xyz',
'https://xn--wtq35pfyd55o.co/pianyi/v0',
'https://xn--yets78bbhi.top',
'https://xquig3.youxuan.wiki',
'https://xs.mashiroshina.top',
'https://xsj520.top',
'https://xsus.moe',
'https://xsus.wiki',
'https://xunlei-api.okay.casa',
'https://xxjsm.xn--nrqu89ap6f632c.xn--io0a7i',
'https://yaxianzhi.shop',
'https://ydapi.dingyuetot.vip',
'https://yes1.xn--mesv7f5toqlp.xyz',
'https://yexiaowork.fmvp.al',
'https://yfycdn.1010520.click',
'https://yiyolink.xyz',
'https://yjy.lol',
'https://ym.qingfan.xyz',
'https://ymjc.cfd',
'https://youxiu5004.xiaofeixia.click',
'https://youxiu5172.xiaofeixia.cfd',
'https://youxiu7540.xiaofeixia.click',
'https://youxiu8168.xiaofeixia.info',
'https://youxiu88.xiaofeixia.click',
'https://youxiu9571.xiaofeixia.click',
'https://ysjc.us.kg',
'https://yunzhiyidy.54188a.cyou',
'https://yuyun.yuyun.one',
'https://z.album.icu',
'https://z.playddt.com',
'https://z.upk.icu',
'https://zhenshihui.shop',
'https://zhenxunkeai.top',
'https://zhongzhuan.mxmxmx.lol',
'https://zhuiyun.shop',
'https://zlxz.80jm.com',
'https://zouma.guanhua.xyz',
'https://zqjc.org',













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
    # 对 Base64 编码后的字符串进行解码,得到字节字符串
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
        #获取时间,给文档命名用
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
            #将获得的节点变成base64加密,为了长期订阅
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
