import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login( 'picuteness@gmail.com', 'agcc azzp fepz xjpn')
from_mail = 'picuteness@gmail.com'

to = '7133674069@tmomail.net'
body = '<ALARM>'
message = ("hi")
server.sendmail(from_mail, to, message)
print("ran")