from mycroft import MycroftSkill, intent_file_handler


class Fhhgb(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fhhgb.intent')
    def handle_fhhgb(self, message):
        self.speak_dialog('fhhgb')

    @intent_file_handler('fhhgbBaDegProg.intent')
    def handle_fhhgbBaDegProg(self, message):
        self.speak_dialog('fhhgbBaDegProg')

    @intent_file_handler('fhhgbMaDegProg.intent')
    def handle_fhhgbMaDegProg(self, message):
        self.speak_dialog('fhhgbMaDegProg')

def create_skill():
    return Fhhgb()
