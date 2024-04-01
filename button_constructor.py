from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import Optional, Sequence, Union, get_args, get_origin
from pprint import pprint
import json
@dataclass
class MessageStructure:
    attachments: Sequence[dict] = field(default_factory=list)
    pretext: str = 'pretext'
    text:str = 'text'
    author_name:str = 'author_name'
    title: str = 'title'
    footer: str = 'footer'
    actions: Sequence[dict] = field(default_factory=list)
    id: str = 'id'
    name: str = 'name'
    integration: dict = field(default_factory=dict)
    url: str = 'rul'
    context: dict = field(default_factory=dict)
    action: str = 'action'

   
    def create_message_structure(self):
        test_dict = dict()
        test_dict2 = dict()
        
        default_structure = {
            self.pretext: 'pretext', 
            self.text: 'text',
            self.author_name: 'author_name',
            self.title: 'title',
            self.footer: 'footer',

            
        }

        for key in self.__annotations__:
            default_value_message = self.__getattribute__(key)

            try:

                if type(default_structure[key]) == str:
                    test_dict[key] = default_value_message
                 
            except KeyError as e: 
                test_dict2[key] = default_value_message
        
        attachments_list_key = list(test_dict2.keys())

        attachments = attachments_list_key[0]
        actions = attachments_list_key[1]

        id = attachments_list_key[2]
        name = attachments_list_key[3]

        integration = attachments_list_key[4]
        url = attachments_list_key[5]
        context = attachments_list_key[6]
        action = attachments_list_key[7]

        
        integration_container = test_dict2[integration]
        context_container = test_dict2[context]
        context_container[action] = test_dict2[action]

        integration_container[url] = test_dict2[url]
        integration_container[context] = context_container

        

        button = dict()

        button[id] = test_dict2[id]
        button[name] = test_dict2[name]
        button[integration] = integration_container
        

        actions_list = test_dict2[actions]
        actions_list.append(button)

        attachments_list = test_dict2[attachments]
        attachments_list.append({**test_dict, actions: actions_list})
        main_dict = {attachments: test_dict2[attachments]}
        
        self.result_structure = main_dict


    def add_description_interactive_message(self,description_interactive_message):
        


        
    
        


       
    
test = MessageStructure()
test.create_message_structure()
test.add_value_message()

        
# testStruct = MessageStructure(attachments=[dict()],pretext='sdfs', text='sfsdfd', author_name='dfsdf', title='dsfsdf', footer='dsfdsf', actions=[dict()], button=dict(), id='asda', name='sfdsf', integration=dict(), url='dsfs', context=dict(), action='asdasd')



        





# class ButtonConstructor:

    

#     def __init__(self):
#         pass


    



# button = ButtonConstructor()



# def attachments(attachments_value):

#     return [{**attachments_value}]


# def button(payload_button, description_button):
#     result = {**description_button, **payload_button}
#     return result

# def button_description(*description, chunk_size=2):
#     size_description_identifiocator = len(list(description))
#     require_chunk_size = int(size_description_identifiocator / chunk_size)
#     cut_range = range(0 , size_description_identifiocator , require_chunk_size)
#     button_description_result = dict(tuple(description[el:el + require_chunk_size] for el in cut_range ))
#     return button_description_result

    

# def button_integration(externel_sevice_url, integration)
   
    
    
    




# print(attachments(button(button_description('id','update', 'name', 'Update'), {"integration": {"url": 'url', "context": {'action': 'test'}}})))




