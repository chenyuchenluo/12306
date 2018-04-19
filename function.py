
# -- coding: utf-8 --
# 2.7版本 字符串有两种编码格式（Unicode、utf-8） 防止输出错误

import time 		# 时间
import threading 	# 线程
import requests		# 发送网络请求
import json			# 解析
# import getpass		# 隐藏密码输入
import random 		# 随机数
import os 			# 系统
import platform 	# 设备
import re 			# 正则匹配
from PIL import Image 	# 图片操作
import urllib 		# 用于urldecode

import sys 			# 系统
reload(sys)
sys.setdefaultencoding('utf8')


# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 全局
c_js = '@bji|北京|BJP|0@sha|上海|SHH|1@tji|天津|TJP|2@cqi|重庆|CQW|3@csh|长沙|CSQ|4@cch|长春|CCT|5@cdu|成都|CDW|6@fzh|福州|FZS|7@gzh|广州|GZQ|8@gya|贵阳|GIW|9@hht|呼和浩特|HHC|10@heb|哈尔滨|HBB|11@hfe|合肥|HFH|12@hzh|杭州|HZH|13@hko|海口|VUQ|14@jna|济南|JNK|15@kmi|昆明|KMM|16@lsa|拉萨|LSO|17@lzh|兰州|LZJ|18@nni|南宁|NNZ|19@nji|南京|NJH|20@nch|南昌|NCG|21@sya|沈阳|SYT|22@sjz|石家庄|SJP|23@tyu|太原|TYV|24@wlq|乌鲁木齐南|WMR|25@wha|武汉|WHN|26@xni|西宁|XNO|27@xan|西安|XAY|28@ych|银川|YIJ|29@zzh|郑州|ZZF|30@szh|深圳|SZQ|shenzhen|sz|31@xme|厦门|XMS|xiamen|xm|32'
url_request_img_code = 'https://kyfw.12306.cn/passport/captcha/captcha-image'
url_check_img_code = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
url_login_account = 'https://kyfw.12306.cn/passport/web/login'
url_login_check_one = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
url_login_check_two = 'https://kyfw.12306.cn/otn/uamauthclient'
url_init_travels = 'https://kyfw.12306.cn/otn/passengers/init'
url_left_ticket = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'

# 点击 预定 后发送的消息
url_user_status = 'https://kyfw.12306.cn/otn/login/checkUser'
url_order_ticket_one = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'
url_order_ticket_two = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
url_order_ticket_three = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
# 点击 提交订单 后发送的消息
url_order_ticket_four = 'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo'
url_order_ticket_five = 'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount'
# 点击 确定 后发送的消息
url_order_ticket_six = 'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue'
url_order_ticket_seven = 'https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime'
# url_order_ticket_eight = 'https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue'


session = requests.session()
home_path = os.path.dirname((sys.argv[0]))

img_code_row = ['35','105','175','245','35','105','175','245']
img_code_col = ['35','35','35','35','105','105','105','105']
seat_index = {1:32,2:31,3:30,4:23,5:28,6:29,7:26}
seat_desc = {1:'商务座',2:'一等座',3:'二等座',4:'软卧',5:'硬卧',6:'硬座',7:'无座'}
seat_code = {1:'9',2:'M',3:'O',4:'4',5:'3',6:'1',7:'1'}

City = {}
CityR = {}
SecretStrs = {}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>1
# 初始化、基本函数
def init():
	initCity(c_js)

	global from_station
	global to_station
	global queryDate

	file = open(home_path + os.sep + '信息表.txt','a+')
	file.close()

	file = open(home_path + os.sep + '信息表.txt','r')
	content = file.readline()
	file.close()

	content = re.sub("\n","",content)

	info = content.split('=')
	if len(info) < 5:
		print u'缺少必要信息，请先完善 信息表.txt。'
		exit()

	from_station  = info[3]
	to_station    = info[4]
	queryDate     = info[2]

	global Account
	global Password
	Account = info[0]
	Password = info[1]

	global goal_train
	global goal_seat
	global traveler_index
	goal_train = ''
	goal_seat = 0
	traveler_index = 0


def timerDelay():
	timer = threading.Timer(1,requestsLeftTickets)
	timer.start()

def getSplitChar():
	sysName = platform.system()
	if sysName == 'Windows':
		return '\\'
	else:
		return '/'

def inputNum(min_v, max_v):
	temp = min_v
	try:
		temp = input()
	except Exception as e:
		print u'输入错误，重新输入'
		return [False]
	
	if type(temp) == int and temp >= min_v and temp <= max_v:
		return [True,temp]
	else:
		print u'输入错误，重新输入'
		return [False]

def getANum(min_v,max_v):
	status = False
	while not status:
		temp = inputNum(min_v, max_v)
		status = temp[0]
	return temp[1]

def initCity(city):
	for S in city.split('@'):
		if not S:
			continue
		City[S.split('|')[1]] = S.split('|')[2]
		CityR[S.split('|')[2]] = S.split('|')[1]

def inputTrainInfo():
	global input_Trains
	print(format(u'','-^40'))
	print u'例如:k2276 g1890 k4792'
	print u'请输入期望的车次，默认全部'
	trains = raw_input()
	trains = trains.upper()
	input_Trains = trains.split()
	# input_Trains = ['G4314','G1874','G1862','G1882','G1894','G1870']

def inputSeatInfo():
	global input_Seats
	input_Seats = []
	print(format(u'','-^40'))
	for index in seat_desc:
		print u'* %d:%s'%(index,seat_desc[index])
	print u'例如:5 4 6 3 2 1 7，多个按先后判断'
	temp = raw_input()
	temp = temp.split()
	for index in temp:
		if type(int(index)) == type(1) and int(index) >= 1 and int(index) <= 7 :
			input_Seats.append(index)
		else:
			print('ERROR 输入中存在错误，请重新输入')
			inputSeatInfo()
			return

	if not input_Seats:
		input_Seats = [5,6,3]

def inputCheckInfo():
	checkInputStationAndTime()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2
# 请求验证码
def requestImgCode():
	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		"Referer":"https://kyfw.12306.cn/otn/leftTicket/init",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
	}
	data = {
		'login_site':'E',
		'module':'login',
		'rand':'sjrand',
	}
	response = session.get(url_request_img_code, headers = headers, params = data, verify = False)
	# 把验证码图片保存到本地
	with open(home_path + getSplitChar() + 'img_code.jpg','wb') as f:
		f.write(response.content)
	try:
		im = Image.open(home_path + getSplitChar() + 'img_code.jpg')
		# 展示验证码图片，会调用系统自带的图片浏览器打开图片，线程阻塞
		im.show()
		# 关闭，只是代码关闭，实际上图片浏览器没有关闭，但是终端已经可以进行交互了(结束阻塞)
		im.close()
	except:
		print u'图片错误或不存在'
		return requestImgCode()
# 验证验证码
def checkImageIds():
	#=======================================================================
	# 根据打开的图片识别验证码后手动输入，输入正确验证码对应的位置，例如：2 5  
	# ---------------------------------------  
	#         |         |         |  
	#    1    |    2    |    3    |     4  
	#         |         |         |  
	# ---------------------------------------  
	#         |         |         |  
	#    5    |    6    |    7    |     8  
	#         |         |         |  
	# ---------------------------------------  
	#=======================================================================

	imageIds = raw_input('请输入验证码位置 1~4 5~8，以空格分隔[例如:1 7]\n')
	answerIds = imageIds.split(' ')

	tempList = []

	for Id in answerIds:
		if type(int(Id)) == type(1) and int(Id) >= 1 and int(Id) <= 8 :
			tempList.append(img_code_row[int(Id) - 1])
			tempList.append(img_code_col[int(Id) - 1])
		else:
			print u'验证码坐标错误'
			return False

	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		"Referer":"https://kyfw.12306.cn/otn/leftTicket/init",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
	}

	Code = ','.join(tempList)
	data = {
		'login_site':'E',
		'rand':'sjrand',
		'answer':Code
	}
	# 发送验证
	response = session.post(url = url_check_img_code, data = data, headers = headers, verify = False)
	result = json.loads(response.content)
	code = result['result_code']
	
	# 取出验证结果，4：成功  5：验证失败  7：过期
	print u'%s'%result['result_message']
	if str(code) == '4':
		return True
	else:
		return False
# 登录
def login():
	checkImgResult = False
	while not checkImgResult :
		requestImgCode()
		checkImgResult = checkImageIds()

	data = {
		'username':Account,
		'password':Password,
		'appid':'otn'
	}
	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/login/init',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	print u'发送登录请求...'
	state = False
	while not state:
		try:
			response = session.post(url = url_login_account, data = data, headers = headers, verify = False)
			result = json.loads(response.content)
			state = True
		except Exception as e:
			pass
	print u'%s'%result['result_message']
	if result['result_code'] == 0:
		pass
	else:
		initAccount()
		return False

	# {"result_message":"密码输入错误次数过多，用户将锁定20 分钟,请稍后再试。","result_code":1}

	dada = {
		'appid':'otn'
	}

	print u'发送验证登录请求...'
	response = session.post(url = url_login_check_one, headers = headers, data = data)
	if response.status_code == 200:
		result = json.loads(response.text, encoding = 'utf8')
		print u'检查验证登录请求返回值...'
		print u'%s'%result['result_message']
		if result['result_code'] != 0:
			return False
		else:
			global newapptk 
			newapptk = result.get('newapptk')
	else:
		return False

	data = {
		'tk':newapptk
	}

	print u'发送确认登录请求...'
	response = session.post(url = url_login_check_two, headers = headers, data = data)
	if response.status_code == 200:
		result = json.loads(response.text, encoding = 'utf8')
		print u'检查确认登录请求返回值...'
		print u'%s'%result['result_message']
		if result['result_code'] == 0:
			print u'用户: %s 登录成功'%result['username']
			global apptk
			apptk = result['apptk']
			return True
		else:
			return False
	else:
		return False

def getTravers():
	print u'获取乘车人信息...'
	hander = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded',
		'Content-Length':'10',
		'Host':'kyfw.12306.cn',
		'Upgrade-Insecure-Requests':'1',
		'Referer':'https://kyfw.12306.cn/otn/index/initMy12306',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	data = {
		'_json_att':''
	}

	index = 1
	response = session.post(url = url_init_travels, headers = hander, data = data, verify = False)
	if response.status_code == 200:
		names = re.findall("'passenger_name':'(.*?)',", response.content)
		print(format(u'',"_^25"))
		for string in names:
			print u'序号:%d 名字:%s'%(index,string.decode('unicode-escape') )
			index += 1
		print(format(u'',"_^25"))

		global traveler_index
		traveler_index = getANum(1,index)
	else:
		print u'重新获取联系人...'
		# getTravers()

# 检查用户登录状态
def checkLoginStatus():
	data = {
		'_json_att':''
	}
	headers = {
		'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'If-Modified-Since':'0',
		'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}
	response = session.post(url = url_user_status, data = data, headers = headers, verify = False)
	result = json.loads(response.content)

	# {
	#     "validateMessagesShowId":"_validatorMessage",
	#     "status":true,
	#     "httpstatus":200,
	#     "data":{
	#         "flag":false
	#     },
	#     "messages":[],
	#     "validateMessages":{}
	# }

	if result['status'] and result['httpstatus'] == 200:
		if result['data']["flag"]:
			return True
		else:
			return False
	else:
		return checkLoginState()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>3
# 查询车次函数
def getStation(Station):
	try:
		Station = City[Station]
	except Exception as e:
		return None
	return Station

def checkInputStationAndTime():
	global from_station
	global to_station
	global queryDate

	from_station = getStation(from_station)
	if not from_station:
		print u'出发站错误'
		exit()
		return
	to_station = getStation(to_station)
	if not to_station:
		print u'到达站错误'
		exit()
		return

	timeArray = time.strptime(queryDate, '%Y-%m-%d')
	goalTime = int(time.mktime(timeArray))
	nowTime = int(time.time())

	if nowTime > goalTime + 86400 or nowTime + 30 * 86400 < goalTime :
		print u'日期错误'
		exit()
		return

def requestsLeftTickets():
	try:
		response = session.get(url_left_ticket%(queryDate,from_station,to_station))
		Data = json.loads(response.content)
		bHaveTicket = True
	except Exception as e:
		print u'没有查询到车辆信息'
		bHaveTicket = False

	text = ''
	global goal_train
	global goal_seat
	goal_train = ''
	goal_seat = 0

	#解析车辆信息
	if bHaveTicket:
		print(format(u' 检测时间： %s '%time.strftime('%Y-%m-%d %H:%M:%S'),"*^101"))
		for data in Data['data']['result']:
			trainInfo = data.split('|')
			
			if not SecretStrs.get(trainInfo[3]) and trainInfo[0]:
				SecretStrs[trainInfo[3]] = trainInfo[0]

			# textmp = u'车次:%6s %+5s:%-5s %+5s-%s 共 %-7s 商务座:%s 一等座:%s 二等座:%s 软卧:%s 硬卧:%s 硬座:%s 无座:%s\n' %(
			# 	trainInfo[3],CityR[trainInfo[6]],CityR[trainInfo[7]],trainInfo[8],trainInfo[9],trainInfo[10],
			# 	trainInfo[32] or '--',trainInfo[31] or '--',trainInfo[30] or '--',trainInfo[23] or '--',trainInfo[28] or '--',trainInfo[29] or '--',trainInfo[26] or '--')
			# text += textmp
			if not input_Trains:
				for s_id in input_Seats:
					tempInt = int(s_id)
					if goal_seat == 0 and trainInfo[seat_index[tempInt]] and trainInfo[seat_index[tempInt]] != '无':
						goal_train = trainInfo[3]
						goal_seat = tempInt
			else:
				for trainId in input_Trains:
					if trainInfo[3] == trainId:
						for s_id in input_Seats:
							tempInt = int(s_id)
							if goal_seat == 0 and trainInfo[seat_index[tempInt]] and trainInfo[seat_index[tempInt]] != '无':
								goal_train = trainInfo[3]
								goal_seat = tempInt

		if goal_seat == 0:
			timerDelay()
		else:
			print u'恭喜你，%s 车次 %s %s 有票'%(queryDate,goal_train,seat_desc[goal_seat])
			# 检查账户登录状态
			status = checkLoginStatus()
			if not status:
				print(format(u' 重新登录账户 ',"_^40"))
				result = False
				while not result:
					result = login()
			print(format(u' 开始预定车票 ',"_^40"))
			orderTicket()
			# timerDelay()
			exit()
	else:
		timerDelay()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>4
# 订票函数
def orderTicket():
	# 第一条消息
	print u'发送预定请求...'
	headers = {
		'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	# print(urllib.quote(SecretStrs[goal_train])) 编码
	# print(urllib.unquote(SecretStrs[goal_train])) 解码
	data = {
		'secretStr':urllib.unquote(SecretStrs[goal_train]),
		'train_date':queryDate,
		'back_train_date':time.strftime('%Y-%m-%d',(time.localtime(time.time() + 15 * 86400))),
		'tour_flag':'dc',
		'purpose_codes':'ADULT',
		'query_from_station_name':CityR[from_station],
		'query_to_station_name':CityR[to_station],
		'undefined':'',
	}

	response = session.post(url = url_order_ticket_one, headers = headers, data = data, verify = False)
	result = json.loads(response.content, encoding = 'utf8')
	if not result['status']:
		print result['messages'][0]
		# orderTicket()
		return

	# 第二条消息
	print u'获取票信息...'
	headers = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0'
	}
	data = {
		'_json_att':''
	}
	
	response = session.post(url = url_order_ticket_two, headers = headers, data = data, verify = False)
	initDcData = response.content

	REPEAT_SUBMIT_TOKEN = re.search("globalRepeatSubmitToken = '(.*?)';",initDcData).group(1)
	# print REPEAT_SUBMIT_TOKEN

	# 第三条消息 得到所有乘车人信息
	print u'获取乘车人列表...'
	headers = {
		'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest'
	}
	data = {
		'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN,
		'_json_att':''
	}
	
	status = False
	while not status:
		response = session.post(url = url_order_ticket_three, headers = headers, data = data, verify = False)
		result = json.loads(response.content)
		status = result['status']

	travelers = result['data']['normal_passengers']
	# print(format(u'',"_^25"))
	# for string in travelers:
	# 	print u'序号:%s %s 	%s  %s'%(string['code'],string['passenger_name'],string['sex_name'],string['passenger_type_name'])
	# print(format(u'',"_^25"))
	# print u'请输入一个乘车人序号'
	# traveler_index = getANum(1,len(travelers))

	session.get('https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=passenger&rand=randp&' + str(random.uniform(0,1)))
			
	# 第四条消息
	print u'提交乘车人信息...'
	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	person = travelers[traveler_index - 1]
	item1 = []
	item2 = []

	# 座位编号,0,乘客类型,乘客名,证件类型,证件号,手机号码,保存常用联系人(Y或N(1个)/N_(多个))
	item1.append(seat_code[goal_seat])
	item1.append('0')
	item1.append(person['passenger_type'])
	item1.append(person['passenger_name'])
	item1.append(person['passenger_id_type_code'])
	item1.append(person['passenger_id_no'])
	item1.append(person['mobile_no'])
	item1.append('N')

	# 乘客名,证件类型,证件号,乘客类型
	item2.append(person['passenger_name'])
	item2.append(person['passenger_id_type_code'])
	item2.append(person['passenger_id_no'])
	item2.append(person['passenger_type'] + '_')

	passengerTicketStr = ','.join(item1)
	oldPassengerStr = ','.join(item2)
	# print passengerTicketStr
	# print oldPassengerStr

	data = {
		'cancel_flag':'2',
		'bed_level_order_num':'000000000000000000000000000000',
		'tour_flag':'dc',
		'randCode':'',
		'whatsSelect':'1',
		'_json_att':'',
		'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN,
		'passengerTicketStr':passengerTicketStr,
		'oldPassengerStr':oldPassengerStr,
	}

	response = session.post(url = url_order_ticket_four, headers = headers, data = data, verify = False)
	result = json.loads(response.content)

	if not result['status']:
		print u'%s'%result['messages']
		timerDelay()
		return

	# 第五条消息
	print u'获取订单队列...'
	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	train_date = re.findall("'time':(.*?)000,",initDcData)
	train_no = re.search("train_no':'(.*?)'",initDcData).group(1)
	stationTrainCode = re.search("station_train_code':'(.*?)'",initDcData).group(1)
	leftTicket = re.search("leftTicketStr':'(.*?)',",initDcData).group(1)
	train_location = re.search("train_location':'(.*?)'",initDcData).group(1)
	purpose_codes = re.search("purpose_codes':'(.*?)'",initDcData).group(1)

	# print train_date
	# print train_no
	# print stationTrainCode
	# print leftTicket
	# print train_location
	# print purpose_codes

	data = {
		'train_date':time.strftime('%a %b %d %Y %H:%M:%S GMT+0800 (%Z)',time.localtime(float(train_date[len(train_date) - 1]))),
		'train_no':train_no,
		'stationTrainCode':stationTrainCode,
		'seatType':seat_code[goal_seat],
		'fromStationTelecode':from_station,
		'toStationTelecode':to_station,
		'leftTicket':leftTicket,
		'purpose_codes':purpose_codes,
		'train_location':train_location,
		'_json_att':'',
		'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN
	}

	response = session.post(url = url_order_ticket_five, headers = headers, data = data, verify = False)
	result = json.loads(response.content, encoding = 'utf8')
	if not result['status']:
		print u'%s'%result['messages'][0]
		timerDelay()
		return

	# 第六条消息
	print u'确认订单...'
	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	key_check_isChange = re.search("key_check_isChange':'(.*?)',",initDcData).group(1)

	data = {
		'randCode':'',
		'purpose_codes':purpose_codes,
		'passengerTicketStr':passengerTicketStr,
		'oldPassengerStr':oldPassengerStr,
		'seatDetailType':'000',
		'whatsSelect':'1',
		'roomType':'00',
		'dwAll':'N',
		'_json_att':'',
		'choose_seats':'',
		'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN,
		'leftTicketStr':leftTicket,
		'train_location':train_location,
		'key_check_isChange':key_check_isChange,
	}

	response = session.post(url = url_order_ticket_six, headers = headers, data = data, verify = False)
	result = json.loads(response.content, encoding = 'utf8')
	if not result['status']:
		print u'%s'%result['messages'][0]
		timerDelay()
		return

	# 第七条
	print u'获取订单编号...'
	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}
	data = {
		'random':int(round(time.time() * 1000)),
		'tourFlag':'dc',
		'_json_att':'',
		'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN,
	}

	times = 1
	orderId = ''
	while times < 5:
		response = session.get(url_order_ticket_seven, headers = headers, params = data)
		if response.status_code == 200:
			result = json.loads(response.content, encoding = 'utf8')
			if result['data']:
				if not result['data'].get('orderId'):
					if result['data'].get('msg'):
						print result['data']['msg']
					else:
						print u'返回错误,重新获取'

					time.sleep(2)
				else:
					orderId = result['data']['orderId']
					break
		times += 1

	if orderId != '':
		print u'订票成功 订单号: %s，请于30分钟内付款'%orderId
		suucessTip = Image.open(home_path + getSplitChar() + 'success.jpg')
		suucessTip.show()
		suucessTip.close()
	else:
		print u'请登录12306查看未完成订单详情'
		errorTip = Image.open(home_path + getSplitChar() + 'error.png')
		errorTip.show()
		errorTip.close()
	
