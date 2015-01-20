import wx

'''
Created on 2014-9-15

@author: lsq
'''

class Widget():
    '''
    classdocs
    '''

    type = "type"
    id = 'id'
    pos = 'pos'
    size = 'size'               
    style = 'style'               
    label = 'label'       
    name = 'name'
    unkown = 'unknown'
    listener = 'listener'
    Module = __import__('wx')
    def __init__(self, panel, params):
        '''
        Constructor
        '''
        
        self.type = params.get(Widget.type)
        self.id = params.get(Widget.id, -1)
        self.pos = params.get(Widget.pos, wx.DefaultPosition)
        self.size = params.get(Widget.size, wx.DefaultSize)
        self.style = params.get(Widget.style)
        self.label = params.get(Widget.label, "")
        self.listenerName = params.get(Widget.listener)
        if self.style == None:
            self.style = 0
        else:
            self.style = getattr(Widget.Module, self.style)
        self.name = params.get(Widget.name, Widget.unkown)
        self.panel = panel
        
    def hasName(self):
        return self.name != Widget.unkown
    def getName(self):
        return self.name