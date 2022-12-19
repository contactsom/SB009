import smtplib

try:

    s= smtplib.SMTP('smtp.gmail.com',587)
    sender_email_id="" # from
    sender_email_pass = ""
    reciver_Email="" # to
    message="Hello How are you "
    s.starttls()
    s.login(sender_email_id,sender_email_pass)
    s.sendmail(sender_email_id,reciver_Email,message)
    s.quit()

except Exception as e :
    print(e)