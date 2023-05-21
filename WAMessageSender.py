import pandas as pd
import pywhatkit
from datetime import datetime

# Import the numbers from a csv file, with one column containing phone numbers
phoneNumbers = pd.read_csv('Phone Numbers.csv', header=None)

imageCaption = """
Caption
"""
welcomeMessage = 'Hi there!'
imagePath = 'Message.jpg'

countryCode = '98' # Your country code
# hours of the day that the bot should send the automated message
startTime = 8
stopTime = 16

for phoneNumber in phoneNumbers[0]:
    now = datetime.now()
    if (startTime <= now.hour <= stopTime):
        try:
            pywhatkit.sendwhatmsg_instantly(
                f'{countryCode}{phoneNumber}', 
                welcomeMessage, 
                tab_close=True, 
                close_time=2,
                wait_time=5)
            pywhatkit.sendwhats_image(
                f'+{countryCode}{phoneNumber}',
                img_path=imagePath,
                caption=imageCaption, 
                tab_close=True, 
                close_time=10, 
                wait_time=2
                )

        except Exception as e:
            print(e)
    else:
        while (now.hour > stopTime or now.hour < startTime):
            now = datetime.now()
