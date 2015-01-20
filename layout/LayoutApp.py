import wx
from Parser import Parser
from Frame import Frame
    
# Every wxWidgets application must have a class derived from wx.App
class LayoutApp(wx.App):
    def __init__(self, manifest, layout):
        self.parser = Parser(manifest, layout)
        wx.App.__init__(self)
        return
    # wxWindows calls this method to initialize the application
    def OnInit(self):

        # Create an instance of our customized Frame class
        frame = self.parser.initFrame() 
        frame.Fit()
        frame.Show(True)
 
        # Tell wxWindows that this is our main window
        self.SetTopWindow(frame)

        # Return a success flag
        return True
    def getWidgetManager(self):
        return self.parser.widgetManager