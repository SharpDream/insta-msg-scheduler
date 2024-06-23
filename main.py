# main.py
from instabot import Bot
import schedule
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_message_to_friend(username, message):
    try:
        bot = Bot()
        bot.login(username=os.getenv("INSTAGRAM_USERNAME"), password=os.getenv("INSTAGRAM_PASSWORD"))
        bot.send_message(message, [username])
        print(f"Message sent to {username}: {message}")
        bot.logout()
    except Exception as e:
        print(f"An error occurred: {e}")

def schedule_message():
    # Schedule the send_message_to_friend function
    schedule.every().day.at("04:00").do(send_message_to_friend, username=os.getenv("TARGET"), message=os.getenv("MSG"))

    print("Scheduler started. Waiting for the scheduled tasks...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_message()
