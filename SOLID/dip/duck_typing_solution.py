class Notification:
    def __init__(self, service) -> None:
        self.service = service
    
    def send(self, message):
        self.service.notify(message)


class EmailService:
    def notify(self, message):
        print(f"{message} from {self.__class__.__name__}")


class SmsService:
    def notify(self, message):
        print(f"SMS: {message} from {self.__class__.__name__}")


notifier = Notification(EmailService())
notifier.send("Hi!")

notifier = Notification(SmsService())
notifier.send("Hola!")

