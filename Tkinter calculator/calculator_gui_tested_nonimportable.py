import tkinter as tk


window=tk.Tk()
window.title("Calculator")
window.geometry("300x500")
storeno1 = 0.0
storeno2 = 0.0
current_fontsize=80
frame_display = tk.Frame(master=window, height=100, width=500)
frame_display.pack()
frame_display.pack_propagate(0)
label = tk.Label(master=frame_display, text=0, font=('Helvetica bold', current_fontsize))
label.pack()
operator = ""
decimal_flag=0
decimal_count=0

def changestate(Current_Charachter):
    global operator
    global decimal_flag
    global decimal_count
    global current_fontsize

    if Current_Charachter == "." and decimal_flag==1:
        pass
    elif Current_Charachter=="." and decimal_flag==0:
        decimal_flag=1
    elif Current_Charachter in ["+","-","*","/"]:
        operator=Current_Charachter
        decimal_count=0
        decimal_flag=0
        label.config(text=str(storeno1)+operator)
    elif  Current_Charachter == "=" and operator!="":
        _=calculate(storeno1,operator,storeno2)
        label.config(text=_,font=('Helvetica bold', (90-(10*len(str(_)))) if (90-(10*len(str(_))))>10 else 10))
    elif Current_Charachter=="=" and operator=="":
        pass
    elif int(Current_Charachter) in range(0,10) and operator not in ["+","-","*","/"]:
        label.config(text=changestoreno1(int(Current_Charachter)))
    elif int(Current_Charachter) in range(0,10) and operator in ["+","-","*","/"]:
        label.config(text=changestoreno2(int(Current_Charachter)))
    if operator=="" and len(str(storeno1))>3 and current_fontsize>=10:
        current_fontsize-=10
        label.config(font=('Helvetica bold', current_fontsize))
    elif operator!="" and len(str(storeno2))>3 and current_fontsize>=10:
        current_fontsize-=10
        label.config(font=('Helvetica bold', current_fontsize))

def changestoreno1(_):
    global storeno1
    global decimal_count
    if decimal_flag==0:
        storeno1=(storeno1*10)+_
        return int(storeno1)
    else:
        decimal_count+=1
        storeno1=storeno1+(_/(10**decimal_count))
        return storeno1

def changestoreno2(_,*args):
    global storeno2
    global decimal_count
    if decimal_flag==0:
        storeno2=(storeno2*10)+_
        return int(storeno2)
    else:
        decimal_count+=1
        storeno2=storeno2+(_/(10**decimal_count))
        return storeno2


def calculate(no1,operator,no2):
    match operator:
        case "+":
            return (no1+no2)
        case "-":
            return (no1-no2)
        case "*":
            return (no1*no2)
        case "/":
            return (no1/no2)
        case "%":
            return (no1%no2)
        case default:
            return None

def reset():
    global storeno1
    global storeno2
    global operator
    global decimal_flag
    global decimal_count
    global current_fontsize
    storeno1=0
    storeno2=0
    operator=""
    decimal_count=0
    decimal_flag=0
    current_fontsize=80
    label.config(text="0", font=('Helvetica bold', 80))


frame_pad=tk.Frame(master=window, height=300, width=500)
frame_pad.pack()
frame_pad.grid_propagate(0)
frame_pad.grid_anchor(anchor="center")
frame_pad.grid_columnconfigure(index=4, pad=10)
button_1=tk.Button(master=frame_pad, text=" 1 ",font=('Helvetica bold', 26), command=lambda: changestate("1"))
button_1.grid(column=1,row=3)
button_2=tk.Button(master=frame_pad, text=" 2 ",font=('Helvetica bold', 26), command=lambda: changestate("2"))
button_2.grid(column=2,row=3)
button_3=tk.Button(master=frame_pad, text=" 3 ",font=('Helvetica bold', 26), command=lambda: changestate("3"))
button_3.grid(column=3,row=3)
button_4=tk.Button(master=frame_pad, text=" 4 ",font=('Helvetica bold', 26), command=lambda: changestate("4"))
button_4.grid(column=1,row=2)
button_5=tk.Button(master=frame_pad, text=" 5 ",font=('Helvetica bold', 26), command=lambda: changestate("5"))
button_5.grid(column=2,row=2)
button_6=tk.Button(master=frame_pad, text=" 6 ",font=('Helvetica bold', 26), command=lambda: changestate("6"))
button_6.grid(column=3,row=2)
button_7=tk.Button(master=frame_pad, text=" 7 ",font=('Helvetica bold', 26), command=lambda: changestate("7"))
button_7.grid(column=1,row=1)
button_8=tk.Button(master=frame_pad, text=" 8 ",font=('Helvetica bold', 26), command=lambda: changestate("8"))
button_8.grid(column=2,row=1)
button_9=tk.Button(master=frame_pad, text=" 9 ",font=('Helvetica bold', 26), command=lambda: changestate("9"))
button_9.grid(column=3,row=1)
button_0=tk.Button(master=frame_pad, text=" 0 ",font=('Helvetica bold', 26), command=lambda: changestate("0"))
button_0.grid(column=2,row=4)
button_dot=tk.Button(master=frame_pad, text=" .  ",font=('Helvetica bold', 26), command=lambda: changestate("."))
button_dot.grid(column=1,row=4)
button_equal=tk.Button(master=frame_pad, text=" = ",font=('Helvetica bold', 26), command=lambda: changestate("="))
button_equal.grid(column=3,row=4)
button_plus=tk.Button(master=frame_pad, text="+",font=('Helvetica bold', 26), command=lambda: changestate("+"))
button_plus.grid(column=4,row=1)
button_minus=tk.Button(master=frame_pad, text="- ",font=('Helvetica bold', 26), command=lambda: changestate("-"))
button_minus.grid(column=4,row=2)
button_multiply=tk.Button(master=frame_pad, text="x",font=('Helvetica bold', 26), command=lambda: changestate("*"))
button_multiply.grid(column=4,row=3)
button_division=tk.Button(master=frame_pad, text="/ ",font=('Helvetica bold', 26), command=lambda: changestate("/"))
button_division.grid(column=4,row=4)
button_clear=tk.Button(master= window, text="  clear  ", font=('Helvetica bold', 35), command=reset)
button_clear.pack()


window.mainloop()