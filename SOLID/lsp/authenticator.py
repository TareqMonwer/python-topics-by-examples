import abc


class Authenticator(abc.ABC):
    @abc.abstractmethod
    def authenticate(self, credentials):
        pass


class EmailAuthenticator(Authenticator):
    def authenticate(self, credentials):
        # Authentication logic for email
        return {"user_id": "123"}


class OAuthAuthenticator(Authenticator):
    def authenticate(self, credentials):
        # Authentication logic for OAuth
        return {"user_id": "456"}


def login(authenticator: Authenticator, credentials):
    return authenticator.authenticate(credentials)


user = login(OAuthAuthenticator(), {'user_id': 1})
print(user)
