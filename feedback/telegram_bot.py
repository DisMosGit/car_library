import telebot


class Bot():
    def __init__(self, KEY: str = None, telegram_users: list = []):
        assert KEY is not None, "key argument not specified"
        self.bot = telebot.TeleBot(KEY)
        self.users = telegram_users

    def telegram_message(self, message: str, users: list):
        if users is None:
            users = self.users
        for user_id in users:
            self.bot.send_message(user_id, message)

    def form_and_send(self, users: list = None, **kwargs):
        if users is None:
            users = self.users
        self.telegram_message(self.form_feedback_message(**kwargs),
                              users=users)

    def form_feedback_message(self,
                              user_id: int,
                              user_name: str,
                              title: str = 'No title',
                              text: str = 'No message',
                              datetime: str = 'No datetime'):
        message: str = ""
        message += title.capitalize(
        ) + "\n\n" + text + "\n\n" + user_name + " [" + str(
            user_id) + "]" + "  " + datetime
        return message
