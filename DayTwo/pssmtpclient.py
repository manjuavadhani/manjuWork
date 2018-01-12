import smtplib
from sys import platform, version

from_addr = 'manjunath.ramachandra@emc.com'
to_addr = 'manjunath.ramachandra@emc.com'
subject = 'py version'
message = 'platform : {}\n version :{}'.format(platform,version)

mailbody = "From:{}\n\n".format(from_addr)
mailbody += "To:{}\n\n".format(to_addr)
mailbody += "Subject:{}".format(subject)
mailbody += message


smtp = smtplib.SMTP('mailhub.lss.emc.com')
smtp.sendmail(from_addr,to_addr, mailbody)
smtp.close()