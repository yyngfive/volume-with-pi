import tkinter as tk

root = tk.Tk()
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
window_w = 250
window_h = 100
root.geometry(f'{window_w}x{window_h}+' + 
              f'{int((screen_w-window_w)/2)}+{int((screen_h-window_h)/2)}')
root.resizable(0,0)
label_volume = tk.Label(root,text = 'Volume')
pi_61 = '31415926535897932384626433832795028841971693993751058209749445'
pi = pi_61
current = tk.StringVar()
label_pi = tk.Label(root,text = pi,font={'Arial',10})
label_current = tk.Label(root,textvariable=current,bg='white',width=10)
btn_last = tk.Button(root,text = 'Last')
btn_next = tk.Button(root,text='Next')
check_mute = tk.Checkbutton(root,text='Mute')


def current_volumne():
    pass

def current_pi():
    return 10

def set_volume(value):
    pass

def pi_to_volume(location):
    if 0 <= location < len(pi)-2: 
        return int(pi[location:location+2])
    elif location == len(pi) - 2:
        return int(pi[location:])
    else:
        return -1

pi_x = current_pi()
current.set(pi_to_volume(pi_x))

def pi_split(location):
    previous = pi[0:location]
    last = pi[location+2:]
    return (previous,last)

def go_last(event):
    global pi_x
    pi_x -= 1
    print(pi_to_volume(pi_x))
    volume = pi_to_volume(pi_x)
    if volume != -1:
        volume = pi_to_volume(pi_x)
        set_volume(volume)
        current.set(volume)
def go_next(event):
    global pi_x
    pi_x += 1
    print(pi_to_volume(pi_x))
    volume = pi_to_volume(pi_x)
    if volume != -1:
        volume = pi_to_volume(pi_x)
        set_volume(volume)
        current.set(volume)
    



label_volume.pack()
label_pi.place(x = pi_x,y = 20)
label_current.pack()
btn_last.pack(side='left',expand = True)
btn_last.bind('<Button-1>',go_last)
check_mute.pack(side='left',expand = True)
btn_next.pack(side='left',expand=True)
btn_next.bind('<Button-1>',go_next)
root.mainloop()
