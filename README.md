文档
fetchPorxy.main
├── .github──workflows──getSub.yml(actions Deploy)
├── config
│   ├── provider──config.yml(转clash订阅用的配置)
│   ├── subsource──subsource.yaml(网络获取的订阅源)
│   ├── sublist_free.json(免费airport订阅列表) 
│   └── sublist_mining.json(爬取的可用订阅列表) 	
├── sub
│   ├── free(免费airport订阅)
│   │   ├── clash---(clash格式订阅)
│   │   ├── test---(test新资源)
│   │   └── 其它v2ray订阅
│   ├── miningUrl(未测速节点合集url格式)
│   ├── miningUrl64(未测速合集base64格式)
│   └── miningClash.yml(未测速合集Clash格式)
├── utils(程序功能模块)
│   ├── getSubSource──getSubSource.py((获取爬取到的订阅源文件放入'./config/source/subsource.yaml'))
│   ├── checkUrllist
│   │   ├── check.py(检测订阅源列表的可用性)
│   │   ├── ip_update.py(下载country.mmdb文件)
│   │   ├── urllist2sub.py(转换节点文件到'./sub/'目录下的订阅文件)
│   │   └── sub_convert.py(转换订阅格式的功能模块)
│   ├── free(获取免费airport)
│   │   ├── myUseClash ---(获取自用clash)
│   │   ├── test ---(测试新的airport)
│   │   ├── config.yaml(免费airport网站列表)
│   │   ├── main.py(主程序开始)
│   │   ├── freev2.py(获取'V2board'网站Gmail注册订阅)
│   │   ├── qqfreev2.py(获取'V2board'网站QQ邮箱注册订阅)
│   │   └── freess.py(获取'SSpanel'网站订阅)
│   └── requirements.txt(依赖库)
└── README.md
使用注意
转码功能用到的subconverter工具

IP库country.mmdb

已备份到'rx/all/githubTools'
