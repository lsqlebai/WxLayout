'''
Created on 2014-9-15

@author: lsq
'''

from layout.widget import * 

class WidgetManager(object):
    '''
    classdocs
    '''
    type = "type"
    
    
    def __init__(self):
        '''
        Constructor
        '''
        self.widgetMap = {}
    def createWidget(self, params, panel):        
        type = params[Widget.type]
        widgetCls = globals()[type]
        widget = widgetCls(panel, params)
        
        if widget.hasName():
            self.widgetMap[widget.getName()] = widget
        return widget
        
    def findWidgetByName(self, name):
        return self.widgetMap.get(name)