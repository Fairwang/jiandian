#!/user/bin/python
# -*- coding:utf-8 -*-
import MySQLdb
class Query_database():
    def query_database(self,sql):

        #sql = "SELECT price,ispay,pay_way,pay_type FROM t_pay_order WHERE order_id='22201803211002369485679821597756' "
        # 建立连接，使用MMySQLdb模块的connect方法连接mysql，传入账号、密码、数据库、端口、ip和字符集

        coon = MySQLdb.connect( host='116.62.112.180',user='root', passwd='fr349fg97^*&#TY', db='jdshop_test', port=3306, charset='utf8')
        cursor = coon.cursor()
        try:
            cur=cursor.execute(sql)
            results=cursor.fetchall()
            # price=results[0][0]
            # ispay = results[0][1]
            # pay_way = results[0][2]
            # pay_type = results[0][3]
            # return price, ispay, pay_way, pay_type
            # #return  results[0][0],results[0][1],results[0][2],results[0][3]
        #取出的数据库为n列m行，需要得到某行的数据则是 results[n-1][m-1]
            return results
        except :
            print "Error: This is except"
            # coon.commit()
        coon.close()

# sql = "SELECT price,ispay,pay_way,pay_type FROM t_pay_order WHERE order_id='22201803211002369485679821597756' "
# a=shujuku(sql)

# print a
# print a[0],a[2],a[3]

#o=shujuku("SELECT * FROM t_sys_adminuser WHERE  username = '15868314566'")