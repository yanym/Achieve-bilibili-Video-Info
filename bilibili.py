#-*-coding:utf-8-*- 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def res(url):
	print('开始获取视频信息...')
	Info = []
	n = 0
	for aid in url:
		link = 'http://api.bilibili.com/archive_stat/stat?callback=jQuery17209407593795756368_1473066462019&aid=%s&type=jsonp&_=1473066462632'
		response = urlopen(link %aid).read().decode('utf-8')
		pattern = re.compile('.*\(\{.*\{"view":(\d*).*"favorite":(\d*)')
		res = pattern.search(response).groups()
		temp = (aid, int(res[0]), int(res[1]))
		Info.append(temp)
		n += 1
		print('正在获取第%d个视频信息...' %n)
	print('获取完毕! (第一个是Av号，第二个是点击量，第三个是收藏数)\r')
	return(Info)



def getAv():
	print('正在获取Av号...')
	n = 1
	AllAV = []
	while n <= 387:
		links = 'http://api.bilibili.com/archive_rank/getarchiverankbypartion?callback=jQuery172031403610740603116_1473216041993&type=jsonp&tid=32&pn=%s&_=1473216042288'
		page = str(n)
		response = urlopen(links %page).read().decode('unicode-escape')
		pattern = re.compile('{"aid":(\d*)')
		res = pattern.findall(response)
		for x in res:
			AllAV.append(x)
		n += 1
		print('正在获取第%d页视频AV号...' %n)
	print('获取完毕!')
	return AllAV

def ViewSort(Info):
	return sorted(Info, key = lambda x: x[1])

def FavoirteSort(Info):
	return sorted(Info, key = lambda x: x[2])

def ViewFile(ViewSortedInfo):
	with open('View.txt','a') as f:
		f.write('点击量排序: (第一个是Av号，第二个是点击量，第三个是收藏数)\r')
		for x in ViewSortedInfo:
			f.write(str(x)+'\r')

def FavoriteFile(FavoriteSortedInfo):
	with open('Favorite.txt','a') as f:
		f.write('收藏量排序: (第一个是Av号，第二个是点击量，第三个是收藏数)\r')
		for x in FavoriteSortedInfo:
			f.write(str(x)+'\r')


Info = res(getAv())
ViewFile(ViewSort(Info))
FavoriteFile(FavoirteSort(Info))

'''
JS
jQuery17209407593795756368_1473066462019
({"code":0,"data":{"view":514,"danmaku":5,"reply":0,
	"favorite":3,"coin":1,"share":0,"now_rank":0,"his_rank":0},
	"message":"ok"});
'''