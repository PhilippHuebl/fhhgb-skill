from mycroft import MycroftSkill, intent_file_handler


class Fhhgb(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fhhgb.intent')
    def handle_fhhgb(self, message):
        self.speak_dialog('fhhgb')


def create_skill():
    return Fhhgb()

