from tkinter import*
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')

my_img = ImageTk.PhotoImage(Image.open("D:/Kuliah/All Matakuliah/Semester 7/Pengolahan Citra/UTS/ProjectTransform-tkinter/finalimage.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Keluar Program", command=root.quit)
button_quit.pack()

root.mainloop()