import smtplib, ssl

hostname = 'smtp.gmail.com'
port = 465

username = 'thycallmekutty1220@gmail.com'
password = 'evut tspx bkce lucg'

to_address = 'santhakumars12@outlook.com'

context = ssl.create_default_context()

message = """\
Subject: It's me
Hi da, How are you??
"""

with smtplib.SMTP_SSL(host=hostname, port=port, context=context ) as server:
    server.login(username, password)
    server.sendmail(username, to_address, message)