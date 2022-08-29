from browser import document
from browser.widgets.dialog import InfoDialog

def click(ev):
    document.location = 'https://superboi211.github.io'
document['btnRedirect2'].bind('click', click)