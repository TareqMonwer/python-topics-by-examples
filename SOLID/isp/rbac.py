class BasicUserService:
    def view_profile(self, user_id):
        pass


class AdminUserService(BasicUserService):
    def delete_user(self, user_id):
        pass


class ModeratorUserService(BasicUserService):
    def flag_user(self, user_id):
        pass
