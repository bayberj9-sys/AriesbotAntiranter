import os
from fbchat_muqit import Client
from fbchat_muqit.models import Message

class AriesBot(Client):
    def on_message(self, mid, author_id, message_object):
        self.mark_as_seen(author_id)
        text = message_object.text
        if not text:
            return
        if "hello" in text.lower():
            self.send(Message(text="Hey there! 👋"), thread_id=author_id, thread_type=1)
        elif "help" in text.lower():
            self.send(Message(text="I'm Aries Bot!"), thread_id=author_id, thread_type=1)
        else:
            self.send(Message(text=f"You said: {text}"), thread_id=author_id, thread_type=1)

if __name__ == "__main__":
    email = os.getenv("FB_EMAIL")
    password = os.getenv("FB_PASSWORD")
    if not email or not password:
        print("Error: FB_EMAIL and FB_PASSWORD required")
        exit(1)
    bot = AriesBot(email, password)
    print("Bot started, listening for messages...")
    bot.listen()
