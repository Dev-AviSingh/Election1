import tkinter as  tk
from tkinter import messagebox
from tkinter import filedialog
import shutil, os
from PIL import Image
from time import sleep

class app(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.config(height = 400, width = 320, bg = "#2B3252")
        self.state = []
        for _ in range(12 + 1):
            self.state.append(False)
        
        self.pack()

        self.entries = []
        self.buttons = []
        self.logos = []
        self.names = []
        self.finaldata = None
        for x in range(0, 12):
            self.logos.append("")
            self.names.append("")
            
        self.submit = tk.Button(text = "Submit", font = ("timesnewroman", 30), bg = "#EF5455", fg = "#FAD744", command = self.submitdata)
        self.submit.pack()
        self.submit.place(x = 5, y = 330, height = 65, width = 310)
        

        self.headboy = tk.Label(text = "Head\nBoy", bg = "lightblue", font = ("timesnewroman", 20))
        self.headboy.pack()
        self.headboy.place(x = 215, y = 5, height = 100, width = 100)
        
        self.headgirl = tk.Label(text = "Head\nGirl", bg = "red", font = ("timesnewroman", 20))
        self.headgirl.pack()
        self.headgirl.place(x = 215, y = 115, height = 100, width = 100)
        
        self.sports = tk.Label(text = "Sports\nCaptain", bg = "green", font = ("timesnewroman", 20))
        self.sports.pack()
        self.sports.place(x = 215, y = 225, height = 100, width = 100)
        
        for x in range(0, 12):
            self.entries.append(tk.Entry())
        del x


        for x in range(12 + 1):
            self.buttons.append(tk.Button(relief = "groove", text = "Choose Logo", height = 50, width = 100, bg = "#EF5455", fg = "#FAD744", font = ("timesnewroman", 10, 'bold')))
        del x

        
        for x in range(0, 12):
            self.entries[x].pack()
            self.entries[x].bind("<Button-1>", self.selectall)
            self.buttons[x].pack()
            self.buttons[x].bind("<Button-1>", self.choosefile)
        del x


        
        for x in range(0, 4):
            self.buttons[x].place(x = 5, y = (x * 25) + 5, height = 25, width = 100)
            self.entries[x].place(x = 110, y = (x * 25) + 5, height = 25, width = 100)
            self.entries[x].insert(0, "Candidate {}".format(str(x + 1)))
        del x
        for x in range(4, 8):
            self.buttons[x].place(x = 5, y = (x * 25) + 5 + 10, height = 25, width = 100)
            self.entries[x].place(x = 110, y = (x * 25) + 5 + 10, height = 25, width = 100)
            self.entries[x].insert(0, "Candidate {}".format(str(x + 1)))
        del x
        for x in range(8, 12):
            self.buttons[x].place(x = 5, y = (x * 25) + 5 + 20, height = 25, width = 100)
            self.entries[x].place(x = 110, y = (x * 25) + 5 + 20, height = 25, width = 100)
            self.entries[x].insert(0, "Candidate {}".format(str(x + 1)))
        self.intro = tk.Label(text = "The only supported formats\n are bmp png and jpg. \nMade By - Avanish Kumar Singh", bg = "#111", fg = "white", font = ("timesnewroman", 15))
        self.intro.pack()
        self.intro.bind("<1>", lambda x: x.widget.destroy())
        self.intro.place(x = 0, y = 0, height = 400, width = 320)
        

        
    def selectall(self, event):
        i = None
        for x in self.entries:
            if event.widget == x:
                y = self.entries.index(x)
                i = y
        if not self.state[i]:
            event.widget.delete(0, tk.END)
            self.state[i] = True

        event.widget.icursor = 0

        self.update()
    def choosefile(self, event):
        i = None
        for x in self.buttons:
            if event.widget == x:
                y = self.buttons.index(x)
                i = y
                break
        filename = filedialog.askopenfilename(title = "Select Logo")
        print(filename)
        x['state'] = 'disabled'
        #event.widget.config(bg = "lightblue")
        self.logos[i] = filename
        print(self.logos)

    def submitdata(self):
        for x in range(0, 12):
            self.names[x] = self.entries[x].get()

        self.change()
        xx = open("candidatelist.txt", 'w')
        xx.write("")
        xx.close()
        for x in self.names:
            candidatelist = open("candidatelist.txt", "a")
            candidatelist.write(str(x) + ",")
            candidatelist.close()
        candidatelist = open("candidatelist.txt", "r")
        xx = candidatelist.read()
        xx = xx.split(",")
        for x in xx:
            print(x)
        
        for x in self.entries:
            x.delete(0, "end")

    def change(self):
        htmlfile = open("static/reserve/index.html", mode = 'r')
        data = htmlfile.read()
        htmlfile.close()
        
        for x in range(0, 12):
            data = data.replace(("<!--Cand{}-->Candidate {}<!--Cand{}/-->".format(x + 1, x + 1, x + 1)),
                         ("<!--Cand{}-->{}<!--Cand{}/-->".format(x + 1, self.names[x],x + 1))
                         )
            #print(x)
        #print(data)
        htmlfile = open("templates/index.html", mode = 'w')
        htmlfile.write(data)
        htmlfile.close()
        

        for y in range(0, 12):
            try:
                if ".png" in self.logos[y]:
                    im = Image.open(self.logos[y])
                    rgb_im = im.convert('RGB')
                    rgb_im.save(self.logos[y].replace('.png', '.jpg'))
                elif ".bmp" in self.logos[y]:
                    img = Image.open(self.logos[y])
                    img.save( self.logos[y], 'jpeg')
                else: pass

                shutil.copy(os.path.join("static/reserve/", "cand{0}.jpg".format(y + 1)),
                            os.path.join("static/".format(y + 1), "cand{}.jpg".format(y + 1))
                            )
            except FileNotFoundError as e:
              #print(str(e))
              pass

        
        for y in range(0, 12):
            try:
                shutil.move(os.path.join(self.logos[y]),
                            os.path.join("static/", "cand{}.jpg".format(y + 1))
                            )
                print(self.logos[y])
            except FileNotFoundError as e:
              print(str(e) + " move")
              pass
            
        

root = tk.Tk()
root.geometry("320x400")
root.maxsize(320, 400)
root.minsize(320, 400)
root.resizable = False
root.title("School Election Nomination")
ap = app(root)

ap.mainloop()
