import requests
from bs4 import BeautifulSoup 


# 获取网页
def geturl(url):
	headers={
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate, br",
	"Accept-Language":"zh-CN,zh;q=0.9",
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive",
	"Cookie":"_pk_hi_ssid=1b43c06761a544edaa63014ac8e3edeb; deviceid=b36a8b6a2c154140b1ea28f66e6ee90f; UM_distinctid=166828033583d7-0617ad904d3c12-43480420-1fa400-1668280335918f; CNZZDATA4754392=cnzz_eid%3D1267623338-1539785185-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1542029843; Hm_lvt_a08b68724dd89d23017170634e85acd8=1541517006,1541517125,1542030982,1542031078; cps_id=91190; _pk_ref.www.vmall.com.d1b9=%5B%22%22%2C%22%22%2C1547559164%2C%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAHSKs0kDu902kIAsjd3jdT000005O0a7C00000ILVrIj.THveJ_lJzTz1ksK85yF9pywdpAqVuNqsusK15H6vuWw-ujDdnj0snj9-PW60IHY4PWw7wW9APHNjnHIAPW6zPW-Df1n4PRPKrRm4fHmvwfK95gTqFhdWpyfqn1D3nHb4njnvPiusThqbpyfqnHm0uHdCIZwsrBtEmvkGmvVWQh7bUy71IANzQhPEUi4WUBqWQvDvPWfznikBnH63njT3nzkWnW0kQAbsQAYknjD_rADkQj9BnBkCQZNCIZwsT1CEQLILIz4vUy7_Ua4WUvYEpZN9IvNG5vPGujY4nHD4n0KWThnqnWmvnjb%26tpl%3Dtpl_11735_18848_14842%26l%3D1510523135%26attach%3Dlocation%253D%2526linkName%253D%2525E8%2525A7%252586%2525E9%2525A2%252591%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525B0%2525B4%2525E5%2525B9%2525B3%2525E5%2525AE%2525B9%2525E5%252599%2525A8_1-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DHUAWEI%252520Mate%25252020%2525E7%2525B3%2525BB%2525E5%252588%252597%252520%2525E6%252599%2525BA%2525E6%252585%2525A7%2525E6%252596%2525B0%2525E9%2525AB%252598%2525E5%2525BA%2525A6%2526xp%253Did(%252522m3181990365_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%22%5D; _pk_ses.www.vmall.com.d1b9=*; _dmpa_ref=%5B%22%22%2C%22%22%2C1547559164%2C%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fAHSKs0kDu902kIAsjd3jdT000005O0a7C00000ILVrIj.THveJ_lJzTz1ksK85yF9pywdpAqVuNqsusK15H6vuWw-ujDdnj0snj9-PW60IHY4PWw7wW9APHNjnHIAPW6zPW-Df1n4PRPKrRm4fHmvwfK95gTqFhdWpyfqn1D3nHb4njnvPiusThqbpyfqnHm0uHdCIZwsrBtEmvkGmvVWQh7bUy71IANzQhPEUi4WUBqWQvDvPWfznikBnH63njT3nzkWnW0kQAbsQAYknjD_rADkQj9BnBkCQZNCIZwsT1CEQLILIz4vUy7_Ua4WUvYEpZN9IvNG5vPGujY4nHD4n0KWThnqnWmvnjb%26tpl%3Dtpl_11735_18848_14842%26l%3D1510523135%26attach%3Dlocation%253D%2526linkName%253D%2525E8%2525A7%252586%2525E9%2525A2%252591%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525B0%2525B4%2525E5%2525B9%2525B3%2525E5%2525AE%2525B9%2525E5%252599%2525A8_1-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DHUAWEI%252520Mate%25252020%2525E7%2525B3%2525BB%2525E5%252588%252597%252520%2525E6%252599%2525BA%2525E6%252585%2525A7%2525E6%252596%2525B0%2525E9%2525AB%252598%2525E5%2525BA%2525A6%2526xp%253Did(%252522m3181990365_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%22%5D; _dmpa_ses=5a28209e3313df8c318568198bf9cdaa2e4dc520; CASLOGIN=true; CASLOGINSITE=1; LOGINACCSITE=1; displayName=%E6%A0%A1%E9%95%BF; aliToken=; uid=260086000249535476; name=%E6%A0%A1%E9%95%BF; user=%E6%A0%A1%E9%95%BF; ts=1547559202787; valid=1; sign=851E0C29CE65AD0C8C1851AE90717C28D36FD7993BA4FC6B67CBA6C151D14D2F; ticket=1ST-952744-Hs4qjAwdivldXlkkZY34-cas; hasphone=1; hasmail=2; logintype=2; weChatInfo=false; euid=a7156a454aa54eb387d01012662eadb6; isAuthCust=false; isEnterpriseUser=true; companyUser=false; isFirstLogin=0; ac_loNa=18507*****; ac_lus=1; ac_lgc=3; ac_ltp=7797; ac_li=true; ac_cp=1500721829297|1500721876445|1500721912154|1500721969899|1500722007821; rush_info=260086000249535476_1547559210_08EB35F26D03F178F7615B78130FE31367203F6975B281092B23551EF37B23FD; __ukmc=aff78a7634ae3b91157018a924a160b8260086000249535476; _pk_cvar.www.vmall.com.d1b9=%7B%221%22%3A%5B%22uid%22%2C%22260086000249535476%22%5D%2C%2210%22%3A%5B%22uid%22%2C%22260086000249535476%22%5D%7D; isAuthByUid=true; vmallMyCenterMsg=0; vmallOrderCount=1; optBanding=1; vmallOrderCountWechat=NaN; sc_p=undefined; salePortal=1; _pk_id.www.vmall.com.d1b9=6eebf8a96ed70156.1539787732.5.1547560602.1545397009.; _dmpa_ses_time=1547563209185; _dmpa_id=65240eb8ce90c741d4dee860232351530888385899.1539787775.4.1547561409.1545397803.",
	# "Host":"www.vmall.com",
	# "Referer":="https://www.vmall.com/member/enterprise?showListId=4&categoryId=9&p=10&priceRange=0"
	# Upgrade-Insecure-Requests:="1
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
	}
	r=requests.get(url,headers=headers)
	print(r.text)




if __name__ == '__main__':
	url="https://www.vmall.com/member/enterprise?showListId=4&categoryId=9&p=11&priceRange=0"
	geturl(url)