from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap('im_logo.ico')
frame=LabelFrame(root, text="I am here",padx=5,pady=5).grid(row=0,column=0)
b= Button(frame,text="This will make you exit",command=root.quit).grid(row=0,column=1)

image1 = ImageTk.PhotoImage(Image.open("im1 (1).png"))
image2 = ImageTk.PhotoImage(Image.open("im1 (2).png"))
image3 = ImageTk.PhotoImage(Image.open("im1 (3).png"))
image4 = ImageTk.PhotoImage(Image.open("im1 (4).png"))
image5 = ImageTk.PhotoImage(Image.open("im1 (5).png"))
image6 = ImageTk.PhotoImage(Image.open("im1 (6).png"))
image7 = ImageTk.PhotoImage(Image.open("im1 (7).png"))
image8 = ImageTk.PhotoImage(Image.open("im1 (8).png"))
image9 = ImageTk.PhotoImage(Image.open("im1 (9).png"))
image10 = ImageTk.PhotoImage(Image.open("im1 (10).png"))
image11 = ImageTk.PhotoImage(Image.open("im1 (11).png"))
image12 = ImageTk.PhotoImage(Image.open("im1 (12).png"))
image13 = ImageTk.PhotoImage(Image.open("im1 (13).png"))
image14 = ImageTk.PhotoImage(Image.open("im1 (14).png"))
image15 = ImageTk.PhotoImage(Image.open("im1 (15).png"))
image16 = ImageTk.PhotoImage(Image.open("im1 (16).png"))
image17 = ImageTk.PhotoImage(Image.open("im1 (17).png"))
image18 = ImageTk.PhotoImage(Image.open("im1 (18).png"))
image19 = ImageTk.PhotoImage(Image.open("im1 (19).png"))
image20 = ImageTk.PhotoImage(Image.open("im1 (20).png"))
image21 = ImageTk.PhotoImage(Image.open("im1 (21).png"))
image22 = ImageTk.PhotoImage(Image.open("im1 (22).png"))
image23 = ImageTk.PhotoImage(Image.open("im1 (23).png"))
image24 = ImageTk.PhotoImage(Image.open("im1 (24).png"))
image25 = ImageTk.PhotoImage(Image.open("im1 (25).png"))

image_list = [image1,image2,image3,image4,image5,image6,image7,image8,image9,image10,image11,image12,image13,image14,image15,image16,image17,image18,image19,image20,image21,image22,image23,image24,image25,
]


status=Label(root, text=f"Image 1 of{len(image_list)}",bd=1,relief=SUNKEN,anchor=E).grid(row=3 ,column=0,columnspan=3,sticky=W+E)
my_label = Label(image=image1)
my_label.grid(row=1, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(frame, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(frame, text="<<", command=lambda: back(image_number - 1))

    if image_number == len(image_list):
        image_number=1

    my_label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=2, column=0)
    button_forward.grid(row=2, column=2)
    status = Label(frame, text=f"Image {str(image_number)} of{len(image_list)}", bd=1, relief=SUNKEN, anchor=E).grid(row=3, column=0,
                                                                                                  columnspan=3,
                                                                                                  sticky=W + E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(frame, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(frame, text="<<", command=lambda: back(image_number - 1))

    if image_number == 0:
        image_number=len(image_list)

    my_label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=2, column=0)
    button_forward.grid(row=2, column=2)
    status = Label(frame, text=f"Image {str(image_number)} of{len(image_list)}", bd=1, relief=SUNKEN, anchor=E).grid(
        row=3, column=0,
        columnspan=3,
        sticky=W + E)


button_back = Button(frame, text="<<", command=back, state=DISABLED)
button_exit = Button(frame, text="Exit Program", command=root.quit)
button_forward = Button(frame, text=">>", command=lambda: forward(2))

button_back.grid(row=2, column=0)
button_exit.grid(row=2, column=1,pady=10)
button_forward.grid(row=2, column=2)


root.mainloop()
