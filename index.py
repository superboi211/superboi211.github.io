from browser import document
from browser.widgets.dialog import InfoDialog

def click(ev):
    if document['zone'].value == '':
        InfoDialog('Hey!', 'Please remember to enter a name!')
    elif document['zone'].value == 'sus':
        InfoDialog('Bruh...', f'You\'re {document["zone"].value}!')
    else:
        InfoDialog('Hi!', f'Hello, {document["zone"].value}!')

def redirect(ev):
    document.location = 'https://ff0b-142-113-149-243.ngrok.io/sus'

# bind event 'click' on button to function echo
document['echo'].bind('click', click)
document['btnRedirect'].bind('click', redirect)