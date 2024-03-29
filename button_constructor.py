from dataclasses import dataclass, field, fields
from typing import Optional, Sequence, Union, get_args, get_origin

@dataclass
class MessageStructure:
    attachments: Sequence[dict]
    pretext: str 
    text:str
    author_name:str
    title: str
    footer: str
    actions: Sequence[dict]
    button: dict
    id: str
    name: str
    integration: dict
    url: str
    context: dict
    action: str



    def create_message_structure(self):
        





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




