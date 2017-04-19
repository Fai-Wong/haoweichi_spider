# shaoweichi_spider

## 作业：

http://www.haoweichi.com/Index/random 这个网站，爬取1000个个人信息，保存成cvs文件

- ### 分析:

**主要用到:** requests，lxml（xpath），re正则表达式

访问这个url能自动生成美国人信息，但是每个ip访问次数有限制，访问次数上限就只能隔天再访问，所以需要大量ip切换去访问url。
但是试了下以下url，其他国家的信息生成好像又没有限制==。。。

**生成其他国家的信息url：**
http://www.haoweichi.com/Others/ying_guo_shen_fen_sheng_cheng
http://www.haoweichi.com/Others/jia_na_da_shen_fen_sheng_cheng
http://www.haoweichi.com/Others/ao_da_li_ya_ren_shen_fen_sheng_cheng
http://www.haoweichi.com/Others/de_guo_ren_shen_fen_sheng_cheng
http://www.haoweichi.com/Others/fa_guo_ren_shen_fen_sheng_cheng
http://www.haoweichi.com/Others/yi_da_li_ren_shen_fen_sheng_cheng
http://www.haoweichi.com/More/xi_ban_ya_ren_shen_fen_sheng_cheng
http://www.haoweichi.com/Others/ba_xi_ren_shen_fen_sheng_cheng

**大量ip从哪里来？** 寻找免费ip代理网站，网上有很多，不过质量参差不齐，有可能很多不能用，这里有一些我认为还可以的免费ip

http://www.kuaidaili.com/free/inha/1/

http://proxydb.net/?offset=0

http://www.xicidaili.com/nn/

http://proxylist.me/proxys/index

https://list.proxylistplus.com/

http://www.freeproxylists.net/zh/

http://ipaddress.com/proxy-list/

http://www.66ip.cn/

http://www.mimiip.com/gngao/

写几个爬虫分别取他们的网站把ip爬下来保存到本地，验证ip的有效性可以试着访问百度、淘宝这些大网站，有效即写入文件。

然后再写方法遍历这些ip去访问url，如果访问成功即进行无限次访问，达到上限即换ip进行下次访问，以此类推。

后来运行过程发现，效率不行，因为检查ip有效性需要时间，保存的ip实际还是很多不能访问的，索性干脆不验证有效性，直接去试着访问url，效率比之前还是好很多。

有几个网站的免费ip有效能用的还是挺多的。

这里写了三个分别对应的免费ip网站的爬虫（获取ip ，遍历ip，访问url，保存信息），以此类推可以写其他网站的。一起去把信息爬下来。


现在想想！这么简单！！！
第一次做~,是我我想歪了。记录下想法少走弯路。
