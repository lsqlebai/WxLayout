'''
Created on 2014-9-15

@author: lsq
'''
from Widget import Widget
import wx

class Button(Widget, wx.Button):
    '''
    classdocs
    '''


    def __init__(self, panel, params):
        '''
        Constructor
        '''
        Widget.__init__(self, panel, params)
        
        
        wx.Button.__init__(self, self.panel, -1, label=self.label,
            pos=self.pos, size=self.size, style=self.style, name=self.name)
#         if self.listenerName != None:
#             print globals()
#             self.listener = globals()[self.listenerName]
#             if callable(self.listener):
#                 self.setOnclickListener(self.listener)
    def setOnClickListener(self, onClick):
        self.Bind(wx.EVT_BUTTON, onClick, self)