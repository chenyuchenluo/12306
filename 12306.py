
# -- coding: utf-8 --

# 加载模块
import function

if __name__ == '__main__':
	print(format(u' 开始 ',"*^50"))

	# 初始化参数
	function.init()

	# 登录账户
	status = function.checkLoginStatus()
	if not status:
		print(format(u' 开始登录账户 ',"_^40"))
		result = False
		while not result:
			result = function.login()

	# # 设置查询参数
	print(format(u' 设置查询参数 ',"_^40"))
	function.inputCheckInfo()
	function.inputTrainInfo()
	function.inputSeatInfo()
	function.getTravers()

	# 开始查询余票
	print(format(u' 开始查询余票 ',"_^40"))
	function.timerDelay()
