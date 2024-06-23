# Instagram Message Sender

This script uses Instabot to send a message to a friend on Instagram at a scheduled time. It's hosted on PythonAnywhere and utilizes environment variables for sensitive information.

## Prerequisites

Before running the script, ensure you have:

- PythonAnywhere account (sign up at [PythonAnywhere](https://www.pythonanywhere.com/))
- Basic knowledge of Python and command line usage

## Steps to Set Up

### Step 1: Prepare your PythonAnywhere environment

1. **Sign up and log in**: If you haven't already, sign up for PythonAnywhere and log in to your account.
   
2. **Create a new PythonAnywhere task**:
   - After logging in, navigate to the "Dashboard".
   - Click on "Tasks" to create a new task that will run your script periodically.

### Step 2: Upload your script and set up dependencies

1. **Upload `main.py`**:
   - Navigate to the "Files" tab on PythonAnywhere.
   - Upload your `main.py` script.

2. **Install dependencies**:
   - If `instabot` is not installed, open a Bash console on PythonAnywhere and run:
     ```
     pip install instabot
     ```

### Step 3: Set up environment variables

1. **Add environment variables**:
   - Navigate to the "Files" tab and create a new file named `.env`.
   - Inside `.env`, add your environment variables securely:
     ```
     INSTAGRAM_USERNAME=your_instagram_username
     INSTAGRAM_PASSWORD=your_instagram_password
     TARGET=your_friend_username
     MSG=your_message_to_send
     ```
   - Replace `your_instagram_username`, `your_instagram_password`, `your_friend_username`, and `your_message_to_send` with your actual Instagram credentials and message details.

2. **Load environment variables in your script**:
   - Modify `main.py` to load these environment variables using `python-dotenv`:
     ```python
     # main.py
     from instabot import Bot
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

     if __name__ == "__main__":
         target_username = os.getenv("TARGET")
         message_to_send = os.getenv("MSG")

         send_message_to_friend(username=target_username, message=message_to_send)
     ```

### Step 4: Configure and run your task

1. **Configure the task**:
   - Go to the "Tasks" tab on PythonAnywhere.
   - Click "Create a new scheduled task".
   - Choose the frequency (e.g., daily) and set the command to run:
     ```
     python3 /path/to/your/main.py
     ```
     - Replace `/path/to/your/main.py` with the actual path where your `main.py` file is located.

2. **Save and run the task**:
   - Save the task configuration.
   - PythonAnywhere will execute your script at the scheduled time (e.g., daily at 4:00 AM) using the provided environment variables.

### Step 5: Monitor and troubleshoot

- Check the task logs in PythonAnywhere regularly to monitor if your script executes as expected.
- If any errors occur during execution, PythonAnywhere will log them, aiding in troubleshooting any issues that arise.
