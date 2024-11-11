import abc


class NotificationSender:
    """The OCP Violator Class"""
    def send_notification(self, notification_type: str, message: str):
        if notification_type == "email":
            print(f"Sending email with message: {message}")
        elif notification_type == "sms":
            print(f"Sending SMS with message: {message}")
        else:
            print("Unsupported notification type.")


# ### Solution of the above class.####

class Notification(abc.ABC):
    @abc.abstractmethod
    def notify(self) -> None:
        pass


class EmailNotification(Notification):
    def notify(self) -> None:
        print("Sending email notification")


class SmsNotification(Notification):
    def notify(self) -> None:
        print("Sending sms notification")


class NotificationFactory:
    @staticmethod
    def fetch(notification_type: str) -> Notification:
        match notification_type:
            case "sms":
                return SmsNotification()
            case "email":
                return EmailNotification()
            case _:
                raise NotImplementedError("Not implemented")


notification_sender = NotificationFactory.fetch("email")
notification_sender.notify()

sms_sender = NotificationFactory.fetch("sms")
sms_sender.notify()
