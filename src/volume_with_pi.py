import tkinter as tk
from icecream import ic #debug
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#TODO: 优化代码结构，增加类

root = tk.Tk()
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
window_w = 500
window_h = 120
root.geometry(f'{window_w}x{window_h}+' + 
              f'{int((screen_w-window_w)/2)}+{int((screen_h-window_h)/2)}')
root.resizable(0,0)
label_volume = tk.Label(root,text = 'Volume')
pi_61 = '31415926535897932384626433832795028841971693993751058209749445'
pi = pi_61
pi_current = tk.StringVar()
pi_previous = tk.StringVar()
pi_next = tk.StringVar()
muted = tk.BooleanVar()
pi_x = 0
#TODO：优化按钮布局，当前音量固定显示
frame_pi = tk.Frame(root)
frame_btn = tk.Frame(root)
label_previous = tk.Label(frame_pi,textvariable=pi_previous)
label_current = tk.Label(frame_pi,textvariable=pi_current,bg='white',width=2)
label_next = tk.Label(frame_pi,textvariable = pi_next)
btn_last = tk.Button(frame_btn,text = 'Previous')
btn_next = tk.Button(frame_btn,text='Next')

#TODO: 实现静音功能
#受限于所取圆周率位数，找不到字符串“00”，无法实现静音
def mute():
    ic(str(muted.get()))

check_mute = tk.Checkbutton(frame_btn,text='Mute',var = muted,command=mute)

def volume_system():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current = round(volume.GetMasterVolumeLevelScalar() * 100)
    ic(volume.GetVolumeRange())
    ic(current)
    ic(volume.GetMute())
    if volume.GetMute():
        return 0
    else:
        return current

#TODO 更好的方法？
def volume_to_pi(volume):
    if volume == 100:
        volume = '99'
        return pi.find(volume)
    elif volume == 0:
        return -1
    else:
        return 1

#BUG: 调整音量有时会报错
def set_volume(value):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    ic(value)
    volume.SetMasterVolumeLevelScalar(value / 100,None)

def pi_to_volume(location):
    if 0 <= location < len(pi)-2: 
        return int(pi[location:location+2])
    elif location == len(pi) - 2:
        return int(pi[location:])
    else:
        return -1

def pi_split(location):
    previous = pi[0:location]
    last = pi[location+2:]
    return (previous,last)

def pi_show(previous,current,_next):
    pi_previous.set(previous)
    pi_current.set(current)
    pi_next.set(_next)

def go_last(event):
    global pi_x
    pi_x -= 1
    ic(pi_to_volume(pi_x))
    volume = pi_to_volume(pi_x)
    if volume != -1:
        volume = pi_to_volume(pi_x)
        set_volume(volume)
        previous,_next = pi_split(pi_x)
        pi_show(previous,volume,_next)
def go_next(event):
    global pi_x
    pi_x += 1
    ic(pi_to_volume(pi_x))
    volume = pi_to_volume(pi_x)
    if volume != -1:
        volume = pi_to_volume(pi_x)
        set_volume(volume)
        previous,_next = pi_split(pi_x)
        pi_show(previous,volume,_next)

def display():
    volume = pi_to_volume(pi_x)
    if volume != -1:
        volume = pi_to_volume(pi_x)
        set_volume(volume)
        previous,_next = pi_split(pi_x)
        pi_show(previous,volume,_next)

#BUG: 处理静音时的逻辑和显示BUG
def init():
    global pi_x
    pi_x = volume_to_pi(volume_system())
    if pi_x != -1:
        pi_current.set(pi_to_volume(pi_x))
        display()
    else:
        muted.set(True)
        mute()
    

init()
label_volume.pack()
label_previous.pack(side='left',expand = True)
label_current.pack(side='left',expand = True)
label_next.pack(side='left',expand = True)
btn_last.pack(side='left',expand = True)
btn_last.bind('<Button-1>',go_last)
check_mute.pack(side='left',expand = True)
btn_next.pack(side='left',expand=True)
btn_next.bind('<Button-1>',go_next)
frame_pi.pack()
frame_btn.pack()
root.mainloop()
