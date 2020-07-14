import tkinter
import webbrowser
from tkinter import ttk


analy = {
        '思古解析': 'http://api.bbbbbb.me/jx/?url=',
        '视频解析': 'http://jx.598110.com/?url=',
        'vip视频解析': 'http://api.sumingys.com/index.php?url=',
        '那片云解析': 'http://api.nepian.com/ckparse/?url=',
        '石头云': 'http://jiexi.071811.cc/jx.php?url=',
        '人人解析': 'https://vip.mpos.ren/v/?url=',
        'wlzhan解析': 'http://api.wlzhan.com/sudu/?url=',
        '金桥解析': 'http://jqaaa.com/jx.php?url=',
        'Lequgirl': 'http://api.lequgirl.com/?url=',
        '通用视频': 'http://jx.598110.com/index.php?url=',
        '爱看TV': 'http://aikan-tv.com/?url=',
        '百域阁': 'http://app.baiyug.cn:2019/vip/index.php?url=',
        '会员K云': 'http://17kyun.com/api.php?url=',
        '高端解析': 'http://api.hlglwl.com/jx.php?url=',
        '鑫梦解析': 'http://api.52xmw.com/?url=',
        '618G解析': 'https://jx.618g.com/?url=',
        'OK视频': 'http://okjx.cc/?url='
    }


def go():
    for i in range(len(list(analy.keys()))):
        if com.get() == list(analy.keys())[i] and m_str_var.get() != '':
            webbrowser.open(list(analy.values())[i] + m_str_var.get())


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('VIP解析')
    root.wm_attributes('-topmost', 1)
    width = 550
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, 100, (screenwidth - width) / 2, 0)
    root.geometry(alignstr)
    root.resizable(0, 0)

    com = ttk.Combobox(root, textvariable=tkinter.StringVar(), state="readonly")
    com["value"] = tuple(analy)
    com.current(0)
    com.pack(expand='yes', fill='both')

    m_str_var = tkinter.StringVar()
    m_entry = tkinter.Entry(root, textvariable=m_str_var, width=100)
    m_entry.pack(padx=10, pady=10)

    button = tkinter.Button(root, text="Go", command=go, width=20)
    button.pack(expand='yes', fill='both')

    root.mainloop()
