import tkinter as tk
import numpy as np

class button_create(tk.Button):
    def __init__(self, master,*args,**kwargs):
        super(button_create,self).__init__(master,*args,**kwargs)

class Window(tk.Tk):

    def __init__(self, screenName=None, baseName=None, className='Window',useTk=True, sync=False, use=None,*args,**kwargs):
        super(Window,self).__init__(screenName,className,*args,**kwargs)
        self.className=className

class label_create(tk.Label):
    def __init__(self, master,*args,**kwargs):
        super(label_create,self).__init__(master,*args,**kwargs)
class entry_create(tk.Entry):
    def __init__(self, master,*args,**kwargs):
        super(entry_create,self).__init__(master,*args,**kwargs)
class check_create(tk.Checkbutton):
    def __init__(self, master, *args, **kwargs):
        super(check_create, self).__init__(master, *args, **kwargs)
def write(text,while1):
     for x in range(while1):
      print(text)
class trigonometry():
    def cos(number,while1):

        for x in range(while1):
         print(np.cos(number))
    def sin(number,while1):
        for x in range(while1):
            print(np.sin(number))

    def tan(number, while1):
        for x in range(while1):
            print(np.tan(number))

    def cotan(number, while1):
        for x in range(while1):
            print(1/np.tan(number))
class math():
    def exp(number, while1):
        for x in range(while1):
            print(np.exp(number))

    def log(number, while1):
        for x in range(while1):
            print(np.log(number))
    def pi(while1):
        for x in range(while1):
            print(np.pi)
    def e(while1):
        for x in range(while1):
            print(np.e)
    def root(number,while1):
        for x in range(while1):
            print(np.sqrt(number))





















