import smtplib
import credentials as ts
from email.message import EmailMessage
import pandas as pd 

df = pd.read_csv('ps.csv')
nearone = df[(df['# of Skill Badges Completed in Track 1']>=1) & (df['# of Skill Badges Completed in Track 1']<6) & (df['# of Skill Badges Completed in Track 2']<6)| 
  (df['# of Skill Badges Completed in Track 2']>=1) & (df['# of Skill Badges Completed in Track 2']<6) & (df['# of Skill Badges Completed in Track 1']<6)]
 #send request mail
list_done = nearone[['Student Name' , 'Student Email']].values.tolist()

def sendmail():
	for p in list_done:

		EMAIL_ADDRESS = ts.email
		EMAIL_PASSWORD = ts.password
		msg = EmailMessage()
		msg['Subject'] = '30 Days of Google Cloud | Congratulations '
		msg['From'] = EMAIL_ADDRESS
		msg['To'] = p[1]
		msg.set_content('Plain text')

		msg.add_alternative(
			"""
			<!-- enter html file here -->
			""".format(Student = p[0]), subtype='html', 
			)

		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
			smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

			smtp.send_message(msg)

sendmail()
