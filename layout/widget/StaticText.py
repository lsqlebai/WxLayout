'''
Created on 2014-9-15

@author: lsq
'''
from Widget import Widget
import wx

class StaticText(Widget, wx.StaticText):
    '''
    classdocs
    '''

    
    def __init__(self, panel, params):
        '''
        Constructor
        '''
        Widget.__init__(self, panel, params)
        
        wx.StaticText.__init__(self, panel, -1, label = self.label)
        #, pos=self.pos, size=self.size, style=self.style, name=self.name)
