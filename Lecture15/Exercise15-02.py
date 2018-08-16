import tkinter


def printtimes():
    global times
    for i in range(times):
        print("Hey neighbor.")


class Application(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.hello_button = tkinter.Button(self)
        self.hello_button["text"] = "Print repeatedly"
        self.hello_button["command"] = printtimes
        self.hello_button.pack(side="bottom")


times = 1
root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
