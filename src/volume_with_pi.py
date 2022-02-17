import tkinter as tk

root = tk.Tk()
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
window_w = 250
window_h = 100
root.geometry(f'{window_w}x{window_h}' + 
                f'+{int((screen_w-window_w)/2)}+{int((screen_h-window_h)/2)}')
root.resizable(0,0)
label_volume = tk.Label(root,text = 'Volume')
pi_61 = '31415926535897932384626433832795028841971693993751058209749445'
label_pi = tk.Label(root,text = pi_61)
btn_last = tk.Button(root,text = 'Last')

pi_x = 10

def go_last(event):
    global pi_x
    pi_x -= 10
    label_pi.place(x = pi_x,y = 20)
def go_next(event):
    global pi_x
    pi_x += 10
    label_pi.place(x = pi_x,y = 20)
    


btn_next = tk.Button(root,text='Next')
check_mute = tk.Checkbutton(root,text='Mute')
label_volume.pack()
label_pi.place(x = pi_x,y = 20)
btn_last.pack(side='left',expand = True)
btn_last.bind('<Button-1>',go_last)
check_mute.pack(side='left',expand = True)
btn_next.pack(side='left',expand=True)
btn_next.bind('<Button-1>',go_next)
root.mainloop()
