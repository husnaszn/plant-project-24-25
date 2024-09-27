import smtplib



class water1:
    
    # functions
    def beingwat():
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login( 'picuteness@gmail.com', 'agcc azzp fepz xjpn')
        from_mail = 'picuteness@gmail.com'
        to = '8325960650@mms.att.net'

        body = '<ALARM>'
        message = "plant is being watered yayyy!!"
        server.sendmail(from_mail, to, message)

    def needwat():
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login( 'picuteness@gmail.com', 'agcc azzp fepz xjpn')
        from_mail = 'picuteness@gmail.com'
        
        to = '8325960650@mms.att.net'
        # 7133674069@tmomail.net - husna
        # 8325960650@mms.att.net - claire

        body = '<ALARM>'
        message = "i need water pls.."
        server.sendmail(from_mail, to, message)
    # print(message)


    #   calling functions
   

