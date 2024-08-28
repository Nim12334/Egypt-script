import tkinter as tk
class button_create(tk.Button):
    def __init__(self, master,*args,**kwargs):
        super(button_create,self).__init__(master,*args,**kwargs)

class Window(tk.Tk):
    def __init__(self, screenName=None, baseName=None, className='Window',useTk=True, sync=False, use=None,*args,**kwargs):
        super(Window,self).__init__(screenName,className,*args,**kwargs)
class label_create(tk.Label):
    def __init__(self, master,*args,**kwargs):
        super(label_create,self).__init__(master,*args,**kwargs)
class entry_create(tk.Entry):
    def __init__(self, master,*args,**kwargs):
        super(entry_create,self).__init__(master,*args,**kwargs)















