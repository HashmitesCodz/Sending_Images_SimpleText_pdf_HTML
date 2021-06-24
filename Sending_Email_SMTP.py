import os
import smtplib
# import imghdr
from email.message import EmailMessage
Email = os.environ.get('User')
Pass = os.environ.get('Pass')
# Multiple emails sending
Emails = ['', ''] # to whome you wanna send email
message = EmailMessage()
message['Subject'] = 'Your favorite dinner at home'
message['From'] = Email
# message['To'] = '' # to whome you wanna send email
message['To'] = ', '.join(Emails)
# message.set_content('Image attached...')
# message.set_content('Cv sent...')
message.set_content('HTML sent...')

# SENDING HTML
message.add_alternative(
    """\
    <!DOCTYPE html>
    <html>
    <body>
    <h1>HTML Email from python</h1>
    </body>
    </html>
    
    """, subtype='html'
)

#  FOR SENDING PDF AND IMAGES STARTS

# files = ['img.jpeg', 'img_2.jpeg'] //images
# files = ['.pdf'] # name of pdf

# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         # file_type = imghdr.what(f.name) # no need for pdf
#         file_name = f.name

# message.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)
# message.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)

  # FOR SENDING PDF AND IMAGES ENDS

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(Email, Pass)
    smtp.send_message(message)