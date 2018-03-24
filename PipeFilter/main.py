import tkinter as tk
from modules.pipe import Pipe
from modules.filters import *
from modules.imagefilter import *

class Demo:

    def __init__(self, srcImage = 'resources/ktna.png'):
        window = tk.Tk()
        image = tk.PhotoImage(file = srcImage)
        
        pipe = Pipe()
        self.channelPipe(pipe)
        newImage = pipe.run(image)
        
        d = tk.Label(image = image)
        d.image = image
        d.pack()
        c = tk.Label(image = newImage)
        c.image = newImage
        c.pack()

        window.mainloop()

    def channelPipe(self, pipe):
        
        pipe.addFilter(GrayScale())
        pipe.addFilter(BlueTint())
        pipe.addFilter(Vivify(2))
        pipe.addFilter(Contrast(1.2))
        pipe.addFilter(Brighten(1.1))
    

Demo()
