import wx

class InfoWin(wx.Frame):
    def __init__(self):
        super().__init__(None, title="MSGR", size=(230, 300), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        panel = wx.Panel(self)
        self.name_entry = wx.TextCtrl(panel, pos=(49, 100), size=(120, 30))
        self.ip_entry = wx.TextCtrl(panel, pos=(49, 160), size=(120, 30))
        self.label = wx.StaticText(panel, label="Name:", pos=(50, 85))
        self.ip_label = wx.StaticText(panel, label="IP:", pos=(50, 145))
        self.image = wx.Image(r"C:\MSGR\msgr_logo.png", wx.BITMAP_TYPE_ANY)
        self.image_resized = self.image.Scale(90, 50)
        self.image_resized.SetMaskColour(255, 255, 255)
        self.image_resized.SetMask(True)
        self.bitmap = wx.Bitmap(self.image_resized)
        self.image = wx.StaticBitmap(panel, bitmap=self.bitmap, pos=(61, 10))
        exit_button = wx.Button(panel, label="Go", pos=(73, 230))
        exit_button.Bind(wx.EVT_BUTTON, self.do_everything)

    def do_everything(self, event):
        self.get_name(event)
        self.open_main(event)
        
    def get_name(self, event):
        global name
        name = self.name_entry.GetValue()

    def open_main(self, event):
        app = wx.App(False)
        wx.GetKeyState(wx.WXK_SHIFT)
        frame = MSGR()
        frame.Show()    
        self.Close()
        app.MainLoop()
        

class MSGR(wx.Frame):
    def __init__(self):
        super().__init__(None, title="MSGR", size=(315, 300), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        panel = wx.Panel(self)
        self.input_box = wx.TextCtrl(panel, pos=(6, 230), size=(200, 30), style=wx.TE_PROCESS_ENTER)
        send_button = wx.Button(panel, label="Send", pos=(210, 233))
        self.message_list = wx.TextCtrl(panel, pos=(0, 0), size=(315, 230), 
                                        style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_WORDWRAP)
        self.message_list.Disable()
        send_button.Bind(wx.EVT_BUTTON, self.on_send)
        self.input_box.Bind(wx.EVT_TEXT_ENTER, self.on_send)

    def on_send(self, event):
        message = self.input_box.GetValue()
        if message:
            self.message_list.AppendText(f"{name}: {message}\n")
            self.input_box.Clear()

       
if __name__ == "__main__":
    app = wx.App(False)
    wx.GetKeyState(wx.WXK_SHIFT)
    frame = InfoWin()
    frame.Show()
    app.MainLoop()
