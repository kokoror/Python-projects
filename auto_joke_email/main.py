# send a random joke every week
import smtplib
import requests
import datetime as dt

# connect to API
response = requests.get(url='https://official-joke-api.appspot.com/random_joke')
response.raise_for_status()
joke = response.json()
question = joke['setup']
answer = joke['punchline']

#send email
my_email = "xxxx@gmail.com"
my_password = "xxxx"
to_email = "xxxxxx@gmail.com"

# specify time to send email
now = dt.datetime.now()
weekday = now.weekday()
# send joke on every thursday
if weekday == 3:
    # smtp server for email provider, add port!!!!!
    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    # or with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    # indent the below connect and do not need connection.close()

    # secure the connection
    connection.starttls()

    # login and send email and close
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f'Subject:Weekly Joke From Rachel\n\n-{question}\n-{answer}')
    connection.close()
