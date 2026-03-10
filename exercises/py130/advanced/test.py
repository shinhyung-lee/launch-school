class EmailSender:
    def send(self, message):
        print(f'Sending email: {message}')

class SmsSender:
    def send(self, message):
        print(f'Sending SMS: {message}')

class PushNotifier:
    def send(self, message):
        print(f'Sending push: {message}')
        
class NotificationManager:
    def __init__(self):
        pass 
    
    def notify(self, notifier, message):
        notifier.send(message)
        
# Example usage:
email = EmailSender()
sms = SmsSender()
push = PushNotifier()

manager = NotificationManager()
manager.notify(email, "Hello via Email!")
manager.notify(sms, "Hello via SMS!")
manager.notify(push, "Hello via Push Notification!")

# Expected output:
# Sending email: Hello via Email!
# Sending SMS: Hello via SMS!
# Sending push notification: Hello via Push Notification!