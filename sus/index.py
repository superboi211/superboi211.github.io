from browser import document
from browser.widgets.dialog import InfoDialog

def click(ev):
    document.location = 'https://ff0b-142-113-149-243.ngrok.io/'
document['btnRedirect2'].bind('click', click)