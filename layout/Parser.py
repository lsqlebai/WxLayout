
'''
Created on 2014-9-15

@author: lsq
'''
import json
from Frame import Frame
from layout.widget.Panel import Panel
from layout.widget.WidgetManager import WidgetManager
import wx

class Parser(object):
    '''
    classdocs
    '''
    
    AppName = 'AppName'
    
    
    def __init__(self, manifest, layout):
        '''
        Constructor
        '''
        self.parseManifest(manifest)
        self.mLayout = layout
        self.widgetManager = WidgetManager()
        return
    def initFrame(self):
        frame = Frame(None, -1, self.name)
        panel = Panel(frame)
        
        self.parseLayout(panel)
        
        return frame

    def parseManifest(self, manifest):
        data = self.loadJsonFile(manifest)
        self.name = data[Parser.AppName];
    
    def loadJsonFile(self, filepath):
        try:
            data = json.load(file(filepath))
            return data
        except Exception as e:
            print 'This File:' + filepath + 'maybe have a json syntax error' 
            print e
            
    def parseLayout(self, panel):
        
        data = self.loadJsonFile(self.mLayout)
        if data == None:
            return
        self.mBoxer = wx.BoxSizer()
        columnSizer = wx.FlexGridSizer(len(data), 1, 0, 10)
        for row in data:
            rowSizer = wx.FlexGridSizer(1, len(row), 0, 20)
            for widget in row:
                widgetItem = self.initWedgit(widget, panel)
                rowSizer.Add(widgetItem)
            columnSizer.Add(rowSizer)
        self.mBoxer.Add(columnSizer)
        panel.SetSizerAndFit(self.mBoxer)
        return
    def initWedgit(self, widget, panel):
        return self.widgetManager.createWidget(widget, panel)
        

                