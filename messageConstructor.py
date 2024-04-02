

class MessageConstructor:
    MESSAGE = dict()
    ATTACHMENTS_WRAPPER = dict()
    ATTACHMENTS = []
    PRETEXT = ''
    TEXT = ''
    ACTIONS = []

    BUTTON = {
        'id': '',
        'name': '',
        'integration': {
            'url': '',
            'context': {
                'action': ''
            }
        }
        
    }

    count_elements = 0

    def __init__(self, config=None):
        self.config = config
        

    def attachments(self):
        


        return self.ATTACHMENTS_WRAPPER

    def message_description(self,message_description_tupple):
        while len(message_description_tupple) > self.count_elements:

            self.PRETEXT = message_description_tupple[self.count_elements]
            self.TEXT = message_description_tupple[self.count_elements]

        

    def actions(self):
        pass

    def button(self, button_identification, integration=None):

        print(button_identification)

test = MessageConstructor()

test.button()
