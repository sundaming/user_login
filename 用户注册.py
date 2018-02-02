import MySqlHelper
import hashlib

h = MySqlHelper.MySqlHelper("192.168.28.52")

#创建用户表的sql语句
# sql = """
#
# create table userinfos(
# id int primary key auto_increment not null,
# uname varchar(20),
# upwd  varchar(40),
# isdelete bit(1) default 0
# )charset=utf8;
# """


#注册-往数据添加账号和密码信息(密码要加密) sha1

uname = input("请输入您要注册的账号名:")
upwd = input("请输入您注册的密码:")
#加密后的密码
upwd = hashlib.sha1(upwd.encode("utf-8")).hexdigest()

# print("账号==%s,密码==%s"% (uname,upwd))

sql = "insert into userinfos(uname,upwd) value(%s,%s)"

params = [uname,upwd]

code = h.insert(sql,params)

if code == 1:
	print("恭喜%s注册成功" % uname)
else:
	print("抱歉%s注册失败" % uname)