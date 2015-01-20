'''
Created on 2014-9-15

@author: lsq
'''
import wx
import layout.widget
from Widget import Widget

class ListBox(Widget, wx.ListBox):
    '''
    classdocs
    '''

    list="list"
    def __init__(self, panel, params):
        '''
        Constructor
        '''
        Widget.__init__(self, panel, params)
        #self.mList = []
        self.mList = params.get(ListBox.list, [])
        wx.ListBox.__init__(self, self.panel, -1, choices = self.mList,
            pos=self.pos, size=self.size, style=self.style, name=self.name)
