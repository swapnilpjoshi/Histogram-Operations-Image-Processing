from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import ttk,filedialog
import numpy as np
import cv2
import matplotlib.pyplot as plt

root = Tk()
root.title('Histogram operations')
root.iconbitmap('histogram.ico')
root.configure(background='#077089')


def open():
    global display
    global img
    global image_label
    global myimg
    global l1,b1,l2,b2
    global r1,count1,r2,count2,r3,count3,r4,count4
    global cdf, idealcdf
    globals()['img_dict'] = dict()
    root.filename = filedialog.askopenfilename(
                                                initialdir="D:\\GNR Academics\\GNR607 - SIP\\SIP Project\\Final py files",
                                                title="Select file",
                                                filetypes=(("jpg", "*.jpg"),("png","*.png"),("all files","*.*"))
                                               )
    img_gray = cv2.cvtColor(cv2.imread(root.filename), cv2.COLOR_BGR2GRAY)
    img = np.ndarray.tolist(img_gray)
    img_dict['source_img'] = img

    root.withdraw()
    window1(img)
    a = root.filename
    myimg=cv2.imread(a, 0)
    l1,b1 = myimg.shape
    r1, count1 = hist_plot_myimg(myimg)
    cdf = cum_freq_myimg(myimg)
    # print(cdf)
    idealcdf = cumm_ideal_histogram(cdf)
    # print(idealcdf)

    updated_dn=[]
    for i in range(len(r1)-1):
        if cdf[i]<= idealcdf[0]:
            x=0
            updated_dn.append(x)

    for i in range(len(r1)-1):
        for a in range(len(r1)):
            if idealcdf[i] < cdf[a] <= idealcdf[i+1]:
                updated_dn.append(i+1)
    print("Your image will be available shortly!!!....")
    for k in range(0, 256):
        for i in range(l1):
            for j in range(b1):
                if myimg[i,j] == k:
                    myimg[i,j] = updated_dn[k]
                else: continue
    r3, count3 = hist_plot_myimg(myimg)
    # list_xyz = input_image_parameters()
    
def open2():
    global display
    global img
    global image_label
    global myimg, myimg1
    global l1,b1,l2,b2, list_xyz
    global r1,count1,r2,count2,r3,count3,r4,count4
    global cdf, idealcdf, refcdf
    globals()['img_dict'] = dict()

    root.filename = filedialog.askopenfilename(
                                                initialdir="D:\\GNR Academics\\GNR607 - SIP\\SIP Project\\Final py files",
                                                title="Select input image",
                                                filetypes=(("jpg", "*.jpg"),("png","*.png"),("all files","*.*"))
                                               )
    img_gray = cv2.cvtColor(cv2.imread(root.filename), cv2.COLOR_BGR2GRAY)
    img = np.ndarray.tolist(img_gray)
    img_dict['source_img'] = img
    a = root.filename

    globals()['img_dict'] = dict()
    root.filename = filedialog.askopenfilename(
                                                initialdir="D:\\GNR Academics\\GNR607 - SIP\\SIP Project\\Final py files",
                                                title="Select reference image",
                                                filetypes=(("jpg", "*.jpg"),("png","*.png"),("all files","*.*"))
                                               )
    img_gray = cv2.cvtColor(cv2.imread(root.filename), cv2.COLOR_BGR2GRAY)
    img = np.ndarray.tolist(img_gray)
    img_dict['source_img'] = img

    b = root.filename

    # root.withdraw()
    # window1(img)
    window_2.destroy()

    myimg=cv2.imread(a, 0)
    l1,b1 = myimg.shape
    r1, count1 = hist_plot_myimg(myimg)
    cdf = cum_freq_myimg(myimg)
    # print(cdf)
    # a = root.filename


    refimg=cv2.imread(b, 0)
    l2,b2 = refimg.shape
    r2, count2 = hist_plot_refimg(refimg)
    refcdf = cum_freq_refimg(refimg)
    # print(refcdf)
    updated_dn=[]
    for i in range(len(r1)-1):
        if cdf[i]<= refcdf[0]:
            x=0
            updated_dn.append(x)

    for i in range(len(r1)-1):
        for a in range(len(r1)):
            if refcdf[i] < cdf[a] <= refcdf[i+1]:
                updated_dn.append(i+1)
    print('You Are Almost There')
    for k in range(0, 256):
        for i in range(l1):
            for j in range(b1):
                if myimg[i,j] == k:
                    myimg[i,j] = updated_dn[k]
                else: continue
  
    r4,count4 = hist_plot_myimg(myimg)
    print('Execution Successful...')
    root.withdraw()



def savefile(image):
    file_name = filedialog.asksaveasfile(title="Save as",mode='w')
 
    if file_name is None:
        return
    # saved_image = np.array(image,dtype=np.uint8)
    # saved_image.save(file_name,np.array(image,dtype=np.uint8)) 
    cv2.imwrite(file_name.name,image)
    

def list_to_PIL(image):
    new_width = 0
    new_height = 0
    image = np.array(image,dtype=np.uint8)
    if len(image.shape) == 3:
        image = np.flip(image,axis=-1)
    image = Image.fromarray(image)  
    image = np.array(image,dtype=np.uint8)
    if len(image.shape) == 3:
        image = np.flip(image,axis=-1)
    image = Image.fromarray(image)  
    width,height = image.size
    if width<height:
        new_height = 300
        new_width = (width/height)*300 

    elif width>height:
        new_width = 300
        new_height = ((width/height)**-1)*300

    elif height==width:
        new_width = 300
        new_height = 300 
    size = (int(new_width), int(new_height))

    image = image.resize(size)
    return ImageTk.PhotoImage(image)

def window1(image):
    global display
    global image_label
    global combo_img
    global img_size
    
    image_label.grid_forget()
    window1 = tk.Toplevel()
    window1.title('Histogram operations')
    window1.iconbitmap('histogram.ico')
    window1.configure(background='#077089')
    
    # image_label = tk.Label(window1)
    # image_label.grid(column=0, row=4, padx=100, pady=4)

    heading = Label(window1,text="Histogram Operations\n", font=("helvetica", 15,"bold"),bg='#077089',fg="white",relief=FLAT)
    heading.grid(column=2, row=0, padx=4, pady=4)

    credits = Label(window1,text="\nA project by\nSwapnil Joshi & Vishvesh Kodihal", font=("helvetica", 10),bg='#077089',fg="white")
    credits.grid(column=2, row=15, padx=4, pady=10)


    btn1 = tk.Button(window1, text="Choose reference Image", width=30, command=window2,relief=FLAT)
    btn1.grid(column=3, row=1, padx=10, pady=10)

    btn2 = tk.Button(window1, text="Histogram Equalisation", width=30, command=lambda: histogram_equalization(),relief=FLAT)
    btn2.grid(column=1, row=1, padx=10, pady=10)

    btn3 = tk.Button(window1, text="Histogram Specification", width=30, command=lambda: histogram_specification() ,relief=FLAT)
    btn3.grid(column=2, row=1, padx=10, pady=10)

    btn_plot = tk.Button(window1, text='Histogram (Input image)', width=30, command=lambda: (graph_hist_input(), 1))
    btn_plot.grid(column=1, row=7, padx=4, pady=4)

    btn_plot1 = tk.Button(window1, text='Histogram (Reference image)', width=30, command=lambda: (graph_hist_ref(), 1))
    btn_plot1.grid(column=1, row=8, padx=4, pady=4)

    btn_plot2 = tk.Button(window1, text='Histogram (Equalised image)', width=30, command=lambda: (graph_hist_equalised_output(), 1))
    btn_plot2.grid(column=3, row=7, padx=4, pady=4)

    btn_plot2 = tk.Button(window1, text='Histogram (Specified output)', width=30, command=lambda: (graph_hist_specifeid_output(), 1))
    btn_plot2.grid(column=3, row=8, padx=4, pady=4)
  
    btn_parameters = tk.Button(window1, text='Parameters',width=30, command=lambda: (window3(),1))
    btn_parameters.grid(column=2, row=8, padx=4, pady=10)

    btn_save = tk.Button(window1, text='Save to disk', width=14, command=lambda: savefile(myimg))
    btn_save.grid(column=1, row=9, padx=10, pady=10)

    btn_exit = tk.Button(window1,text="Exit",width=14,bg="#FF665C", fg="black",command=lambda: window1.destroy(),  font=("helvetica", 10))
    btn_exit.grid(column=3,row=9,padx=10,pady=10)
    
    display = list_to_PIL(image)
    image_label = tk.Label(window1, image=display)
    image_label.grid(column=2, row=4,padx=10, pady=10)

def window2():
    global display
    global image_label
    global combo_img
    global img_size
    global window_2
    # image_label.grid_forget()
    
    window_2 = tk.Toplevel()
    window_2.title('Histogram Specification')
    window_2.iconbitmap('histogram.ico')
    window_2.configure(background='#FFF470')

    btn_open = tk.Button(window_2,text="Choose a File",command=lambda:open2(),width=14,bg="#FFF470", fg="black",  font=("helvetica", 10))
    btn_open.grid(column=0, row=2, padx=4, pady=10)
    image_label = tk.Label(window_2)
    image_label.grid(column=0, row=4, columnspan=9999, padx=100, pady=14)
    btn_exit = tk.Button(window_2,text="Exit",width=14,bg="#FF665C", fg="black",command=lambda: window_2.destroy(),  font=("helvetica", 10))
    btn_exit.grid(column=0,row=3,padx=100,pady=14)


def hist_plot_myimg(img):
    m,n = img.shape
    count =[]
    r = []
    for k in range(0, 256):
        r.append(k)
        count1 = 0
        for i in range(m):
            for j in range(n):
                if img[i, j]== k:
                    count1+= 1
        count.append(count1)
    return (r, count)


def hist_plot_refimg(img):
    m,n = img.shape
    countx =[]
    r = []
    for k in range(0, 256):
        r.append(k)
        count2 = 0
        # loops to traverse each pixel in
        # the image
        for i in range(m):
            for j in range(n):
                if img[i, j]== k:
                    count2+= 1
        countx.append(count2)
    return (r, countx)


#ideal Histogram
def cumm_ideal_histogram(cumm):
    b = 0
    max_count= 0
    ideal_count = []
    max_count= cumm[len(r1)-1]
    for i in range(len(r1)):
        b = (max_count/len(r1))*(i+1)
        ideal_count.append(b)
    return ideal_count

def cum_freq_myimg(myimg):
    cdf =[]
    cfk=0
    for i in range(0,256):
        cfk = (cfk + count1[i])
        x=cfk/(l1*b1)
        cdf.append(x)
    return(cdf)

def cum_freq_refimg(refimg):
    cdf =[]
    cfx=0
    for i in range(0,256):
        cfx = (cfx + count2[i])
        y=cfx/(l2*b2)
        cdf.append(y)
    return(cdf)



def graph_hist_input():
    plt.stem(r1, count1)
    plt.xlabel('intensity value')
    plt.ylabel('number of pixels')
    plt.title('Histogram of the original image')
    plt.show()

def graph_hist_ref():
    plt.stem(r2, count2)
    plt.xlabel('intensity value')
    plt.ylabel('number of pixels')
    plt.title('Histogram of the reference image')
    plt.show()

def graph_hist_equalised_output():
    plt.stem(r3, count3)
    plt.xlabel('intensity value')
    plt.ylabel('number of pixels')
    plt.title('Histogram of the output image')
    plt.show()

def graph_hist_specifeid_output():
    plt.stem(r4, count4)
    plt.xlabel('intensity value')
    plt.ylabel('number of pixels')
    plt.title('Histogram of the output image')
    plt.show()

def histogram_equalization():
    cv2.imshow('Histogram Equalization image.png', myimg)

def histogram_specification():
    cv2.imshow('Histogram specification image.png', myimg)


heading = Label(root,text="Histogram Operations\n", font=("helvetica", 15,"bold"),bg='#077089',fg="white")
heading.grid(column=0,row=1,columnspan=9999,padx=100,pady=2,sticky="")

credits = Label(root,text="\nA project by\nSwapnil Joshi & Vishvesh Kodihal", font=("helvetica", 10),bg='#077089',fg="white")
credits.grid(column=0,row=8,columnspan=9999,padx=100,pady=1)

btn_open = tk.Button(root,text="Choose a File",command=lambda:open(),width=14,bg="#FFF470", fg="black",font=("helvetica", 10), relief=FLAT)
btn_open.grid(column=0,row=2,columnspan=9999,padx=100,pady=8)

image_label = tk.Label(root)
#image_label.grid(column=0, row=4, columnspan=9999, padx=100, pady=4)

btn_exit = tk.Button(root,text="Exit",width=14,bg="#FF665C", fg="black",command=lambda: root.destroy(),  font=("helvetica", 10))
btn_exit.grid(column=0,row=3,columnspan=9999,padx=100,pady=14)

def input_image_parameters():
    a=0
    b=0
    sum_freq = 0
    max_DN= max(r1)
    min_DN= min(r1)
    # print(count1)
    # print(r1)
    for i in range(len(r1)):
        sum_freq = sum_freq + (count1[i]*r1[i])
        a = a +count1[i]
    mean_DN= sum_freq/a
    x="Max DN ="+ str(max_DN),"Min DN ="+ str(min_DN),"Mean DN ="+ str(round(mean_DN))
    return x

def reference_image_parameters():
    a=0
    b=0
    sum_freq = 0
    max_DN= max(r2)
    min_DN= min(r2)
    # print(count1)
    # print(r1)
    for i in range(len(r2)):
        sum_freq = sum_freq + (count2[i]*r2[i])
        a = a +count2[i]
    mean_DN= sum_freq/a
    x="Max DN ="+ str(max_DN),"Min DN ="+ str(min_DN),"Mean DN ="+ str(round(mean_DN))
    return x

def equalized_output_parameters():
    a=0
    b=0
    sum_freq = 0
    max_DN= max(r3)
    min_DN= min(r3)
    # print(count1)
    # print(r1)
    for i in range(len(r3)):
        sum_freq = sum_freq + (count3[i]*r3[i])
        a = a +count3[i]
    mean_DN= sum_freq/a
    x="Max DN ="+ str(max_DN),"Min DN ="+ str(min_DN),"Mean DN ="+ str(round(mean_DN))
    return x

def specified_output_parameters():
    a=0
    b=0
    sum_freq = 0
    max_DN= max(r4)
    min_DN= min(r4)
    # print(count1)
    # print(r1)
    for i in range(len(r4)):
        sum_freq = sum_freq + (count4[i]*r4[i])
        a = a +count4[i]
    mean_DN= sum_freq/a
    x="Max DN ="+ str(max_DN),"Min DN ="+ str(min_DN),"Mean DN ="+ str(round(mean_DN))
    return x

def window3():

    window_3 = tk.Toplevel()
    window_3.title('Histogram Parameters')
    window_3.iconbitmap('histogram.ico')
    window_3.configure(background='#FFF470')

    # btn_open = tk.Button(window_3,text="Choose a File",command=lambda:open2(),width=14,bg="#FFF470", fg="black",  font=("helvetica", 10))
    # btn_open.grid(column=0, row=2, padx=4, pady=10)


    frame1 = LabelFrame(window_3, text="Input Parameters",padx=1,pady=1,bg='#FFF470')
    frame1.grid(row=1, column=0,padx=10,pady=10)

    frame2 = LabelFrame(window_3, text="Reference Parameters",padx=1,pady=1,bg='#FFF470')
    frame2.grid(row=2, column=0,padx=10,pady=10)

    frame3 = LabelFrame(window_3, text="Equalised Output Parameters",padx=1,pady=1,bg='#FFF470')
    frame3.grid(row=3, column=0,padx=10,pady=10)

    frame4 = LabelFrame(window_3, text="Specified Output Parameters",padx=1,pady=1,bg='#FFF470')
    frame4.grid(row=4, column=0,padx=10,pady=10)

    a=input_image_parameters()
    label_1 = Label(frame1,text=a, font=("helvetica", 10),background='#FFF470',fg="black")
    label_1.grid(column=0, row=0, padx=4, pady=10)

    c=equalized_output_parameters()
    label_3 = Label(frame3,text=c, font=("helvetica", 10),background='#FFF470',fg="black")
    label_3.grid(column=0, row=0, padx=4, pady=10)

    b=reference_image_parameters()
    label_2 = Label(frame2,text=b, font=("helvetica", 10),background='#FFF470',fg="black")
    label_2.grid(column=0, row=0, padx=4, pady=10)

    d=specified_output_parameters()
    label_4 = Label(frame4,text=d, font=("helvetica", 10),background='#FFF470',fg="black")
    label_4.grid(column=0, row=0, padx=4, pady=10)

root.mainloop()
