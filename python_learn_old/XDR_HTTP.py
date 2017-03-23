import re


xdr_http = '''1|460110670291360|13325736701|8653430282059585|ctlte.mnc011.mcc460.gprs|7.140.1.148|7.140.1.33|115.169.127.140|460110090194481|4601122026|46011|6|218.30.118.213|80|100.80.75.30|39066|24|1346|20160509144405|20160509144406|232|1418|1970|10|10|0|5|9|0|0|1462776245904|1462776245937|1462776245954|0|0|0|0|0|0|0|0|4|3|891|521|Dalvik/1.6.0 (Linux; U; Android 4.4.2; HUAWEI C199 Build/HuaweiC199)|/baohe/list?version=1&toid=1655249292&pst=21&os=19&vc=300050112&v=5.1.12&md=HUAWEI+C199&sn=4.330415746098476&cpu=qualcomm+msm8928&ca1=armeabi-v7a&ca2=armeabi&m=486814754a49c5f75a7585ad37a5a33a&m2=34558de13bb780d6dab478ae66a15456&ch=100166&ppi=720_1184&startCount=1&re=1&tid=0&cpc=1&snt=13&nt=7&s_3pk=1&br=Huawei|md.openapi.360.cn|143||1||6|200|36|0|1462776246032|1462776246068|0|1462776246068|0|0|0|
1|||||7.140.1.146|0.0.0.0|0.0.0.0|0|0|0|0|58.216.6.22|80|10.152.103.249|47637|18|434|20160509144405|20160509144406|140|21090|3450|28|14|0|0|0|0|0|1462776245906|1462776245928|1462776245956|0|0|0|0|0|5|0|5590|3|6|1301|2668|Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; SM-A9000 Build/LMY47V) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1|/zxpic_imtt/abstractimage/20160508/112117_9565401_2_192_144.jpg|zxpic.imtt.qq.com|8730|image/jpeg|1||6|200|22|0|1462776245964|1462776245986|0|1462776245986|0|0|0|3g_guest_id=-9054063169638494207; sd_userid=23961455372552993; sd_cookie_crttime=1455372552993; appsd_mid=1906; softdown_mid=1906; match_mid=3136; softdown_pid=14; pgv_pvi=7727290368; pgv_pvid=346162800; g_ut=3
1|460110191595107|18106510574|8652430294218058|ctlte.mnc011.mcc460.gprs|7.140.1.146|7.140.1.34|115.169.127.138|460110080583219|4601119457|46011|6|180.163.26.124|80|100.88.221.187|51840|18|437|20160509144405|20160509144406|112|1356|1950|10|12|0|5|9|0|0|1462776245906|1462776245917|1462776245960|0|0|0|0|0|0|0|0|3|3|318|490|MicroMessenger Client|/cgi-bin/micromsg-bin/getiosextensionkey|short.weixin.qq.com|98|application/octet-stream|1||5|200|21|0|1462776245960|1462776245981|0|1462776245981|0|0|0|
1|460110194625011|15356648817|3546020714735701|ctnet.mnc011.mcc460.gprs|7.140.1.148|7.140.1.34|115.169.127.140|460110078716466|4601119220|46011|6|114.80.130.97|80|100.91.84.23|40985|1|632|20160509144405|20160509144406|528|1076|3032|4|8|0|5|9|0|0|1462776245908|1462776245914|1462776245936|0|0|0|0|0|0|0|0|9|9|6119|3836|SohuNews/5.2.4 BuildCode/96|/api/function/location.go?cdma_lng%3D120.095790%26cdma_lat%3D30.302499%26cdma_acc%3D200.000000%26cdma_sTime%3D1462776290097%26bsid%3D21091%26nid%3D81%26sid%3D14121%26wifi_mac%3D%26wifi_ssid%3D%26wifi_bssid%3D%26wifi_rssi%3D%26net%3Dwifi%26apiVersion%3D30&p1=NjEzNDY5ODgyMDk0NjUzODU3MA%3D%3D&gid=02ffff110611116315e54403b69d188c367187f0cc1312&pid=-1|api.k.sohu.com|35|application/json;charset=UTF-8|1||5|200|38|0|1462776245945|1462776245983|0|1462776248012|0|0|0|
1|460110203917476|18058581070|8685640247855878|ctwap.mnc011.mcc460.gprs|7.140.1.149|7.140.1.33|115.169.127.141|460110089191218|4601121766|46011|6|14.18.245.161|80|100.89.151.15|38012|1|1995|20160509144406|20160509144407|104|1104|3184|8|10|0|6|9|0|0|1462776246909|1462776246940|1462776246967|0|0|0|0|0|0|0|0|3|2|1380|340||/mstat/report/?index=1462776290|omgmta.qq.com:80|885||1||5|0|30|0|1462776246967|1462776246997|0|1462776246997|0|0|0|
1|460110670604966|13306606486|8673030215196535|ctlte.mnc011.mcc460.gprs|7.140.1.149|7.140.1.33|115.169.126.137|460110081934385|4601119974|46011|6|122.228.234.49|80|100.80.204.116|43307|1|326|20160509144405|20160509144406|144|11460|2884|16|16|0|5|9|0|0|1462776245909|1462776245922|1462776245948|0|0|0|0|0|0|0|0|3|6|972|5542|Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; PLK-AL10 Build/HONORPLK-AL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/6.1 Mobile Safari/537.36|/timg?wisealaddin&size=8&quality=100&sec=1462776278&di=5d2796b33ceff7f222158129fc6fe1a3&src=http%3A%2F%2Ft11.baidu.com%2Fit%2Fu%3D4256681425%2C4003186393%26fm%3D58|cdn01.baidu-img.cn|4395|image/jpeg|1|http://m.baidu.com/s?from=1086k&word=%E6%8E%A5%E8%A7%A6%E6%9C%AA%E6%9D%A5|6|200|20|1|1462776245969|1462776245989|0|1462776245989|0|0|0|
1|460110191354328|17764522159|8640970223948700|ctlte.mnc011.mcc460.gprs|7.140.1.148|7.140.1.34|115.169.127.140|460110079406852|4601119218|46011|6|118.194.55.47|80|100.85.1.93|52541|15|996|20160509144400|20160509144406|5281|1848|3490|14|14|0|5|9|0|0|1462776240809|1462776240839|0|0|0|0|0|0|0|0|0|5|3|1525|500|Apache-HttpClient/UNAVAILABLE (java 1.4)|/Ring/v2/CheckEx.action|query.hicloud.com:80|767|application/json|1||5|0|34|0|2|36|0|37|0|0|0|
1|460110214049648|15356510809|8682230231897600|ctlte.mnc011.mcc460.gprs|7.140.1.145|7.140.1.33|115.169.127.137|460110085520435|4601120747|46011|6|115.239.210.27|80|100.91.10.131|51598|1|326|20160509144405|20160509144406|1660|1872|3426|10|14|0|5|9|0|0|1462776245249|1462776245252|1462776245268|0|0|0|0|0|0|0|0|3|3|1337|748|%E6%89%8B%E6%9C%BA%E7%99%BE%E5%BA%A6/7.3.0.9 CFNetwork/758.2.8 Darwin/15.0.0|/|www.baidu.com|0|text/html|0||0|200|14|0|1462776245304|1462776245318|0|1462776245318|0|0|0|H_PS_PSSID=18880_1453_19839_18280_19805_19900_19559_19807_19843_19902_19861_15538_11966_19595; path=/; domain=.baidu.com
1|460110201451555|15336608608|8678320240520585|ctlte.mnc011.mcc460.gprs|7.140.1.149|7.140.1.33|115.169.127.141|460110080827700|4601119726|46011|6|101.226.129.215|80|100.88.109.140|56137|18|437|20160509144405|20160509144406|127|1892|5720|14|16|0|5|9|2|0|1462776245916|1462776245923|1462776245956|0|0|0|0|0|1|0|314|6|1|2648|114|MicroMessenger Client|/cgi-bin/micromsg-bin/newreportkvcomm|minorshort.weixin.qq.com|1759|application/octet-stream|1||5|0|15|0|1462776245965|1462776245980|0|1462776245980|0|0|0|
7|460110192014479|15356190951|8605760317182203|ctnet.mnc011.mcc460.gprs|115.169.126.55|7.140.1.33|115.169.127.101|460110080143667|4601119461|46011|6|180.163.26.111|80|100.83.90.185|39546|18|437|20160509144350|20160509144406|15627|6406|1674|10|12|0|5|9|0|0|1462776230613|1462776230620|1462776230659|0|0|0|0|0|0|0|0|2|4|477|3117|Dalvik/2.1.0 (Linux; U; Android 5.0.1; MX4 Build/LRX22C)|/mmopen/Q3auHgzwzM4ia4s6icfQX3SwyfAjiczxEohxk1fWN1rj95wc7rocxHV7h3ICibxqbLZbAiaQAJFzN5rtSHGjMgqSfJnECAwUaA2hFQQYQ5dPiancI/96|wx.qlogo.cn|2439|image/jpeg|1||6|200|6|0|1462776230664|1462776230670|0|1462776230670|0|0|0|'''

def xdr_filter(xdr_http):
	xdr = xdr_http.split('\n')
	url_list = []
	refer_list = []
	for i in range(len(xdr)):
		if (re.search('Android', xdr[i])):
			url_list.append(xdr[i].split('|')[46])
			refer_list.append(xdr[i].split('|')[51])

str1 = 'abractyeyt'
str2 = 'dgdsaeactyey'

def LCS(str1, str2):
	len1 = len(str1)
	len2 = len(str2)
	lentotal = len1 + len2
	max1 = 0
	for i in range(lentotal):
		s1start = 0
		s2start = 0
		if i < len1:
			s1start = len1 - i
		else:
			s2start = i - len1
		curmax = 0
		idx = 0
		while idx:
			if s1start + idx >= len1 or s2start + idx >= len2:
				break
			if str1[s1start+idx] == str2[s2start+idx]:
				curmax += 1
			else:
				if curmax > max1:
					max1 = curmax
					curmax = 0
		if curmax > max1:
			max1 = curmax
	return max1

print LCS(str1, str2)

# xdr_filter(xdr_http)