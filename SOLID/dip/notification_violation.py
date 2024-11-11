import abc


class EmailServiceViolated:
    def send_email(self, message: str):
        print(f"Sending email: {message}")


class NotificationViolation:
    def __init__(self):
        self.email_service = (
            EmailServiceViolated()
        )  # High-level module depends on a low-level module

    def send(self, message: str):
        self.email_service.send_email(message)
