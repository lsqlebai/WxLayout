'''
Created on 2014-9-15

@author: lsq
'''
import wx

class Panel(wx.Panel):
    '''
    classdocs
    '''


    def __init__(self, frame):
        '''
        Constructor
        '''
        wx.Panel.__init__(self, frame, -1)
        
    def setSizer(self, box):
        self.SetSizerAndFit(box)
    