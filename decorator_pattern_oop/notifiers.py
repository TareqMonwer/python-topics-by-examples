from notification_abc import Notifier


class BasicNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending the notification: {message}")


class NotifierDecorator(Notifier):
    def __init__(self, notifier: Notifier) -> None:
        self._notifier: Notifier = notifier

    def send(self, message: str) -> None:
        self._notifier.send(message)


class LoggedNotifier(NotifierDecorator):
    def send(self, message: str) -> None:
        print("Logging.......")
        self._notifier.send(message)


class SmsNotifier(NotifierDecorator):
    def send(self, message: str) -> None:
        print("Sending SMS....")
        self._notifier.send(message)


if __name__ == "__main__":
    notifier = BasicNotifier()

    # notify and log only
    logged_notifier = LoggedNotifier(notifier)
    logged_notifier.send("Hi")

    # notify and send sms
    sms_notifier = SmsNotifier(notifier)
    sms_notifier.send("Hi")

    # notify, log and send sms
    sms_notifier = SmsNotifier(logged_notifier)
    sms_notifier.send("Hi")
