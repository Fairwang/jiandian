#!/user/bin/python
# -*-coding:utf-8-*-
import time ,os
#project_path=os.path.abspath()
#
# smtp_server='smtp.exmail.qq.com'
# email_name='1273265323@qq.com'
# email_password=''
# email_To=''
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
import smtplib

class Send_mail():
    def send_mail(self,file_new):
        def fromat_addr(s):
            name,addr=parseaddr(s)
            return  formataddr((Header(name,'utf-8').encode(),addr.encode('utf-8') if isinstance(addr,unicode) else addr))

        from_addr="1273265323@qq.com"
        password="pmqtsszlydusfegj"
        smtp_server=("smtp.qq.com")
        to_addr="860827713@qq.com"

        # msg=MIMEText('hello','plain','utf-8')
        # msg=MIMEMultipart()
        # print file_new
        f=open(file_new,'rb')

        mail_body=f.read()
        print"dd%s" %mail_body
        msg=MIMEText(mail_body,'html','utf-8')
        msg['From']=fromat_addr('测试组1号<%s>' %from_addr)
        msg['To']=fromat_addr('测试收件人<%s>' %to_addr)
        msg['Subjiect']=Header('邮件测试','utf-8').encode()
        try:
            server=smtplib.SMTP(smtp_server,25)
            server.set_debuglevel(1)
            server.login(from_addr,password)
            server.sendmail(from_addr,[to_addr],msg.as_string())
            server.quit()
        except smtplib.SMTPException:
            print "send email error"
#
# a=Send_mail()
#
# a.send_mail('D:\\Users\Asus\\PycharmProjects\\untitled1\\jiandiandenglu\\report\\zappium_report.html')

# report=glob.glob( "D:\\Users\Asus\\PycharmProjects\\untitled1\\jiandiandenglu\\report")
# l=[]
# for files in os.walk("D:\\Users\Asus\\PycharmProjects\\untitled1\\jiandiandenglu\\report"):
#     print files
#     for file in files:
#         l.append(file)
# print l
#
# print l[0],l[1],l[2],l[3],l[4]


