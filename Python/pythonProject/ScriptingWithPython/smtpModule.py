import smtplib

smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.login('rasikaprabhath@gmail.com', 'qispoweevkwkwtjs')
smtpobj.sendmail("rasikaprabhath@gamil.com", "rasikaprabhath@yahoo.com",
                 'Subject: Test Mail\n this si a test mail')
