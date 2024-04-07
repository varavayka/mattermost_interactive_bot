# from config_reader import config_reader

def attachments(buttons, add_button=lambda list_ , value: list_.append(value)):
    
    structure_attachments =  {
        "attachments": []
    }
    if type(buttons) != list:

        add_button(structure_attachments['attachments'], buttons)
        
    else:
        add_button(structure_attachments['attachments'], buttons)
    
    return structure_attachments
        
        
def button(description, id, name, integration, manage_func=lambda action_list, button: action_list.append(button)):
    button = {"id": id, "name": name, **integration}

    button_structure = {**description,   "actions": [] }
    manage_func(button_structure["actions"], button)
   
    return button_structure

def integration_structure(url, context_value):
    context = {
        'action': context_value
    }
    integration_structure = {"integration":{'url': url, 'context': context} }
    return integration_structure


    

