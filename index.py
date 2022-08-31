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
    document.location = 'https://superboi211.github.io'

# bind event 'click' on button to function echo
document['echo'].bind('click', click)
document['AAAAA'].bind('click', redirect)