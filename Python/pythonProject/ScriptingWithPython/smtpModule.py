import smtplib

smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login('aaaa@gmail.com', 'xxxxxxxxx')
smtpobj.sendmail("aaaaa@gamil.com", "aaaaa@yahoo.com",
                 'Subject: Test Mail\n this si a test mail')
