
def attachments(buttons, add_button=lambda list_ , value: list_.append(value)):

    structure_attachments =  {
        "attachments": []
    }
    if type(buttons) != list:

        add_button(structure_attachments['attachments'], buttons)
        
    else:
        structure_attachments['attachments'] = buttons
        # add_button(structure_attachments['attachments'], buttons)
            

    return structure_attachments
        
        
def button(description, id, name, integration, manage_fuc=lambda desc,  button: {**desc, **button} ):
    button = {"id": id, "name": name, **integration}
    return manage_fuc( description , button)

def actions(button):
    actions_list = {'actions':[]}
    if type(button) != list:
        actions_list['actions'].append(button)
        return actions_list
    if type(button) == list:
        actions_list['actions'] = button
    return actions_list

def integration_structure(url, context_value):
    context = {
        'action': context_value
    }
    integration_structure = {"integration":{'url': url, 'context': context} }
    return integration_structure


    


