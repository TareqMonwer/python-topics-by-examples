import abc


class NotifierAbc(abc.ABC):
    def send(self, message: str) -> None:
        pass


class EmailService(NotifierAbc):
    def send(self, message: str) -> None:
        print("Sending mail: ", message)


class SmsService(NotifierAbc):
    def send(self, message: str) -> None:
        print("Sending mail: ", message)


class NotificationSystem:
    def __init__(self, notifier: NotifierAbc) -> None:
        self.notifier = notifier

    def send_notification(self, message: str):
        self.notifier.send(message)


email_svc = EmailService()
sms_svc = SmsService()


mail_notification = NotificationSystem(email_svc)
sms_notification = NotificationSystem(sms_svc)

mail_notification.send_notification("test mail")
sms_notification.send_notification("test sms")
