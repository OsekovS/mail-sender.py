from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import os
from fpdf import FPDF
import smtplib
 
def email(ip_array, password="your_password", from_mail="your_email", to_mail="their_email"):
	# create message object instance
	msg = MIMEMultipart()
	# setup the parameters of the message
	msg['From'] = from_mail
	msg['To'] = to_mail
	msg['Subject'] = "Subscription"

	for i in range(len(ip_array)):
		print(ip_array[i])
		message = "Thank you"
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font("Arial", size=24)
		pdf.cell(200, 10, ip_array[i], ln=1, align="C")
		pdf.output(ip_array[i]+".pdf")

		filename = ip_array[i]+".pdf"
		#открытие на чтение в двоичном режиме
		with open(filename, "rb") as attachment:
		    # Add file as application/octet-stream
		    # Email client can usually download this automatically as attachment
		    part = MIMEBase("application", "octet-stream")
		    part.set_payload(attachment.read())
		# Encode file in ASCII characters to send by email    
		encoders.encode_base64(part)
		# Add header as key/value pair to attachment part
		part.add_header(
		    "Content-Disposition",
		    f"attachment; filename= {filename}",
		)

		# Add attachment to message and convert message to string
		msg.attach(part)

	#create server
	#server = smtplib.SMTP('smtp.mail.ru', 587)
	#server.starttls()
	server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
	server.ehlo()
	# Login Credentials for sending the mail
	server.login(msg['From'], password)
	# send the message via the server.
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	#msg.as_string()
	server.quit()
	 
	print("successfully sent email to %s:")
def delete(ip_array):
	for i in range(len(ip_array)):
		if os.path.isfile(ip_array[i]+".pdf"):
		    os.remove(ip_array[i]+".pdf")
		else:    ## Show an error ##
		    print("Error: %s file not found" % myfile)
email(['1','2','3','4','5','6'])
delete(['1','2','3','4','5','6'])
