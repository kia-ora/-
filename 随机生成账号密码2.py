# coding: utf-8
import random 

global userName, userPassword
userName = ''
userPassword = ''

def  get_userNameAndPassword():
	global userName, userPassword
#这里要是用全局变量，不然函数外的username、userPasswork仍然是之前定义的空白''、''
	usableName_char = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#可作为用户名的字符  
	usablePassword_char ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.1234567890'
#可作为密码的字符，根据所需可适当增减  
	e_userName = []
	e_userPassword = []
	for i in range(8): 
		e_userName.append(random.choice(usableName_char))

	for j in range(6):
		e_userPassword.append(random.choice(usablePassword_char))

	print 'e_userName = ', e_userName
	print 'e_userPassword = ', e_userPassword
	#此时打印出的是两个list

	userName = ''.join(e_userName)
	userPassword = ''.join(e_userPassword)
	print u'用户名:', userName
	print u'密码:', userPassword

#尝试
try:
	get_userNameAndPassword()
	print u'用户名:', userName
	print u'密码:', userPassword
except Exception,e:
	print u'出错了*_*'
	print e

#第一次运行时忘记了第一行的编码注释，出现乱码。
#第二次运行时出现缩进格式错误，indentationerror，出错在tab缩进和空格缩进是不一样的。
#第三次运行，忘记了for语句后的冒号':',真粗心啊。