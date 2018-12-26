# coding=utf-8
# 2.7版本 字符串有两种编码格式（Unicode、utf-8） 防止输出错误

# 加载模块
import function

if __name__ == '__main__':
	print('>>>>> 开始程序')

	# 初始化参数
	function.init()

	# 登录账户
	status = function.checkLoginStatus()
	if not status:
		print('>>>>> Login account')
		result = False
		while not result:
			result = function.login()

	# # 设置查询参数
	print('>>>>> 初始化信息')
	function.inputCheckInfo()
	function.inputTrainInfo()
	function.inputSeatInfo()
	function.getTravers()

	# 开始查询余票
	print('>>>>> 查询余票')
	function.timerDelay()
