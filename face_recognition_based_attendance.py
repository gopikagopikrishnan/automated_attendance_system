from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Face_Recognition_System(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Face Recognition System")
        self.grid()
        self.canvas_width = 1000
        self.canvas_height = 1000
        self.canvas = Canvas(self, 
                             width=self.canvas_width, 
                             height=self.canvas_height, 
                             bg="white")
        self.canvas.grid()

        img = Image.open(r"C:\Users\Gopika\MEENU\MINIPROJECT CSD481\NSS1.jpeg")
        img = img.resize((1000,1000), Image.ANTIALIAS)
        img = img.rotate(-90)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self, image = self.photoimg)
        f_lbl.place(x = 0, y = 0, width = 1000, height = 1000)
        
        bg_img = Label(self, image = self.photoimg)
        bg_img.place(x = 0, y = 0, width = 1000, height = 1000)

        title_lbl = Label(bg_img, text = "Face Recognition Attendance System Software", font = ("Calibri", 35, "bold"), bg = "white", fg = "black")
        title_lbl.place(x = 0, y = 0, width = 1000, height = 50)

        #student button
        img1 = Image.open(r"C:\Users\Gopika\MEENU\MINIPROJECT CSD481\button1.jpg")
        img1 = img1.resize((220,220), Image.ANTIALIAS)
        
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(bg_img, image = self.photoimg1, cursor = "hand2")
        b1.place(x = 100, y = 100, width = 220, height = 220)

        
        






def main():
    Face_Recognition_System().mainloop()

main()