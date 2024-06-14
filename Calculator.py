from tkinter import *
from tkinter import ttk,messagebox
import webbrowser

GUI = Tk()
GUI.title("Uncle Calculator V.0.1")
GUI.iconbitmap('Calculater.ico')
GUI.geometry('500x650')

### FONT #####
FONT1 = ('impact',20)
FONT2 = ('Angsana new',16)
FONT3 = ('Angsana new',24,'bold')

######### Menu ########################
menubar = Menu(GUI)
GUI.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label='Test')
filemenu.add_command(label='Exit',command=GUI.quit)
menubar.add_cascade(label="File",menu=filemenu)

def Youtube():
    url = 'https://www.youtube.com'
    webbrowser.open(url)

helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label='Youtube',command=Youtube)
helpmenu.add_command(label='test2')
menubar.add_cascade(label='HELP',menu=helpmenu)

################### TAB
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

img_t1 = PhotoImage(file='images3.png')
img_t2 = PhotoImage(file='images1.png')
img_t3 = PhotoImage(file='images2.png')

Tab.add(T1,text='คำนวณพื้นที่วงกลม',image=img_t1,compound='left')
Tab.add(T2,text="คำนวณปริมาตร",image=img_t2,compound='left')
Tab.add(T3,text="Help",image=img_t3,compound='left')

################# TAB 1 ###############################################

L = ttk.Label(T1,text="กรุณากรอกรัศมีวงกลม (ตร.ม.)",font=FONT2).pack(pady=20)

v_radius = StringVar()
E1 = ttk.Entry(T1,textvariable=v_radius,font=FONT1,width=10)
E1.pack(pady=(5,5))
E1.focus()

def Calculate(event=None):
    try:
        unit = 'ตรม.'
        radius = float(v_radius.get())
        pi = 3.1416
        calc = pi * (radius**2)
        text = f"พื้นที่วงกลมนี้มีพื้นที่ {calc:,.2f} {unit}"
        v_result.set(text)
        v_radius.set("")
    except:
        messagebox.showwarning("Error","กรุณากรอกข้อมูลเป็นตัวเลข")

B1 = ttk.Button(T1,text="Calculate",command=Calculate)
B1.pack(ipadx=20,ipady=10,pady=10)

E1.bind('<Return>',Calculate)

v_result = StringVar()
v_result.set("-----------------")
R1 = ttk.Label(T1,textvariable=v_result,font=FONT2)
R1.pack(pady=10)

################# TAB 2 ###############################################

img = PhotoImage(file='images.png')
beam_img = ttk.Label(T2,image=img)
beam_img.pack(pady=10)

FTB = Frame(T2)
FTB.pack()

v_cube1 = StringVar()
v_cube2 = StringVar()
v_cube3 = StringVar()

L = ttk.Label(FTB,text="( 1 )",font=FONT1).grid(row=0,column=0,pady=10,padx=10)
ET21 = ttk.Entry(FTB,textvariable=v_cube1,font=FONT1,width=10)
ET21.grid(row=0,column=1,pady=10)

L = ttk.Label(FTB,text="( 2 )",font=FONT1).grid(row=1,column=0,pady=10,padx=10)
ET22 = ttk.Entry(FTB,textvariable=v_cube2,font=FONT1,width=10)
ET22.grid(row=1,column=1,pady=10)

L = ttk.Label(FTB,text="( 3 )",font=FONT1).grid(row=2,column=0,pady=10,padx=10)
ET23 = ttk.Entry(FTB,textvariable=v_cube3,font=FONT1,width=10)
ET23.grid(row=2,column=1,pady=10)

def CalculateCube(evnet=None):
    try:
        calc = float(v_cube1.get()) * float(v_cube2.get()) * float(v_cube3.get())
        text = f'ปริมาตร {calc:,.2f} ลูกบาศเมตร'
        v_result2.set(text)
        v_cube1.set('')
        v_cube2.set('')
        v_cube3.set('')
    except:
        messagebox.showwarning("Error","กรุณากรอกข้อมูลเป็นตัวเลข")
        v_cube1.set('')
        v_cube2.set('')
        v_cube3.set('')


B2 = ttk.Button(T2,text="Calculate Cube",command=CalculateCube)
B2.pack(ipadx=20,ipady=10,pady=10)

ET21.bind('<Return>',lambda x:ET22.focus())
ET22.bind('<Return>',lambda x:ET23.focus())
ET23.bind('<Return>',CalculateCube)


v_result2 = StringVar()
v_result2.set("-----------------")
R1 = ttk.Label(T2,textvariable=v_result2,font=FONT3,foreground='green')
R1.pack(pady=10)



GUI.mainloop()