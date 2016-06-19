import webbrowser
import tempfile
import urllib.request
import urllib.parse
import re
from tkinter import *
from tkinter.colorchooser import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename





class Browser:
    """This creates a relay that allows a user to directly view data sent from a web server."""
    def __init__(self, master):
        """Sets up a browsing session."""
        # Explicit global declarations are used to allow certain variable to be used in all methods.
        global e1

        # Here we create some temporary settings that allow us to create a client that ignores proxy settings.
        self.proxy_handler = urllib.request.ProxyHandler(proxies=None)
        self.opener = urllib.request.build_opener(self.proxy_handler)

        # This sets up components for the GUI.
        menu=Menu(root)
        root.config(menu=menu)
        subMenu=Menu(menu)
        menu.add_cascade(label="Apps",menu=subMenu)
        subMenu.add_command(label="Gmail")
        subMenu.add_command(label="Y! Mail")
        subMenu.add_command(label="Youtube")
        subMenu.add_command(label="Facebook")
        subMenu.add_command(label="Github")
        subMenu.add_command(label="LinkedIn")
        subMenu.add_separator()
        editMenu=Menu(menu)
        menu.add_cascade(label="Settings",menu=editMenu)
        editMenu.add_command(label="Themes and Colors", command=getColor)
        editMenu.add_command(label="History")
        editMenu.add_command(label="Connect account...")
        editMenu.add_command(label="Exit", command=root.quit)
        editMenu=Menu(menu)
        menu.add_cascade(label="Bookmarks",menu=editMenu)
        editMenu.add_command(label="View")
        editMenu.add_command(label="Add bookmark")
        editMenu=Menu(menu)
        menu.add_cascade(label="Tools",menu=editMenu)
        editMenu.add_command(label="Inspect Element")
        editMenu.add_command(label="Manage Extensions")
        editMenu.add_command(label="Developer Tools")
        editMenu=Menu(menu)
        menu.add_cascade(label="Downloads",menu=editMenu)
        editMenu.add_command(label="Open Downloads Folder", command=callback)
      
        Label(root, text='Enter URL',font=("Helvetica",14)).pack(side=TOP)
      
        e1 = Entry(root,width=100)
        e1.pack(side=TOP)
        
        Button(root, text='Go', width=10, relief=RAISED, font=("Helvetica",12), command=self.browse).pack(side=TOP)

        Label(root,text='Quick Links : ',font=("Helvetica",16)).pack(side=BOTTOM)



        # This binds the return key to self.browse as an alternative to clicking the button.
        root.bind_all('<Enter>', self.browse)

    @staticmethod
    def parsed(data):
        """Cleans up the data so the file can be easily processed by the browser."""
        # This removes removes all python-added special characters such as b'' and '\\n' to create understandable HTML.
        initial = str(data)[2:-1]
        lines = initial.split('\\n')
        return lines

    def navigate(self, query):
        """Gets raw data from the queried server, ready to be processed."""
        # This gets the opener to query our request, and submit the response to be parsed.
        response = self.opener.open(query)
        html = response.read()
        return html

    def browse(self):
        """Wraps all functionality together for data reading and writing."""
        # This inputs and outputs the necessary website data from user-specified parameters.
        raw_data = self.navigate(e1.get())
        clean_data = self.parsed(raw_data)

        # This creates a temporary file in which we store our HTML data, and open it in the default browser.
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as cache:
            cache.writelines(line.encode('UTF-8') for line in clean_data)
            webbrowser.open_new_tab(cache.name)
    

# Creates a Tk() window that is always in front of all other windows.
root = Tk()
root.title("Fennec Browser")
photo=PhotoImage(file="Fennec.png")
label=Label(root,image=photo)
label.pack(side=TOP)
url1='http://www.google.com'
url2='http://www.bing.com'
url3='http://www.yahoo.com'

def OpenUrl(url):
    webbrowser.open_new(url)

from tkinter.colorchooser import *
def getColor():
    color = askcolor()

def callback():
    name= askopenfilename() 


frame=Frame(root)
frame.pack(side=BOTTOM)
b1=ttk.Button(frame, command=lambda aurl=url1:OpenUrl(aurl))
b1.pack(side=LEFT)
m1=PhotoImage(file="g.png")
b1.config(image=m1)
tm1=m1.subsample(7,7)
b1.config(image=tm1)
b2=ttk.Button(frame, command=lambda aurl=url2:OpenUrl(aurl))
b2.pack(side=LEFT)
m2=PhotoImage(file="bing.png")
b2.config(image=m2)
tm2=m2.subsample(6,6)
b2.config(image=tm2)
b3=ttk.Button(frame, command=lambda aurl=url3:OpenUrl(aurl))
b3.pack(side=LEFT)
m3=PhotoImage(file="y.png")
b3.config(image=m3)
tm3=m3.subsample(6,6)
b3.config(image=tm3)
b4=ttk.Button(root)
b4.pack(side=LEFT)
m4=PhotoImage(file="lef.png")
b4.config(image=m4)
tm4=m4.subsample(2,2)
b4.config(image=tm4)
b5=ttk.Button(root)
b5.pack(side=RIGHT)
m5=PhotoImage(file="rig.png")
b5.config(image=m5)
tm5=m5.subsample(2,2)
b5.config(image=tm5)
# Starts the program by initializing the Browser object and main-looping the Tk() window.
info_from_server = Browser(root)
root.mainloop()
