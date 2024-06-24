# main.py
from instabot import Bot
import os
import shutil
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

if __name__ == "__main__":

    folder_path = 'config'

    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)  # Use shutil.rmtree to remove the folder and its contents
            print(f"The {folder_path} config has been deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")
            print(f"{folder_path} not deleted")

    target_username = os.getenv("TARGET")
    message_to_send = os.getenv("MSG")
    send_message_to_friend(username=target_username, message=message_to_send)
