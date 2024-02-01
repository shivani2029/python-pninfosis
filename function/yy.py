import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_ =""
pwd = ""
to = from_

msg = MIMEMultipart()
msg["From"]= from_
msg["To"] = from_

html_text = """
<!Doctype>
<html>
<body>
<h1>This is h1 tag</h1>
<img src="https://ichef.bbci.co.uk/news/640/cpsprodpb/11827/production/_104191717_kukurtihar_friezathedog_umidpokharel.png/>
</body>
</html>
"""
html_mime = MIMEText(html_text, "html")
msg.attach(html_mime)


# connect to the server
print("Connecting to the server...")
conn = smtplib.SMTP("smtp.gmail.com", 587)
# secure connection
print("Starting secure connection...")
conn.starttls()
# login to the server
print("[-]Logging in to the server")
conn.login(from_, pwd)
# send the email
print("[-]Sending the email")
conn.sendmail(from_, to, msg.as_string())
# close the connection
print("[-]Closing the connection")
conn.close()
