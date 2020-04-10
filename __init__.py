from mycroft import MycroftSkill, intent_file_handler


class TestEntity(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('entity.test.intent')
    def handle_entity_test(self, message):
        code = message.data.get('code')

        self.speak_dialog('entity.test', data={
            'code': code
        })


def create_skill():
    return TestEntity()

