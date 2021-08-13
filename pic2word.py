import PySimpleGUI as sg
from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np
import time
sg.theme("DarkAmber") # Add a touch of color
# All the stuff inside your window.
'''
在图片中隐藏文字
'''

layout = [
    [sg.Text('欢迎来到情人节必杀器：图片文本转换器')],
    [sg.Text('选择要转换的图片', size=(35, 5), auto_size_text=True), sg.InputText( key='PATH')
              ,sg.FileBrowse()],
    [sg.Text('请输入要转换的内容'), sg.InputText('我喜欢你', key='TEXT')],
    [sg.Text('请输入字体大小'), sg.InputText('15', key='FONT')],
    [sg.Button('开始转换'), sg.Button('退出')]
]

# Create the Window
window = sg.Window('picture to word', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print(values)
    if event == '开始转换':
        print("=====================================")
        print("开始转换！！！请耐心等待！！！")
        print("=====================================")
        start = time.time()

        path, text, font_size = values['PATH'], values['TEXT'], int(values['FONT'])
        # path_reverse = path.reverse()
        path_reverse = ''.join(reversed(path))
        idx0 = path_reverse.index('.')
        idx1 = path_reverse.index('/')
        img_name = path[len(path)-idx1:len(path)-idx0-1]
        print(img_name)
        path_save = path[0:len(path)-idx1]
        print(path_save)
        file_type = path[len(path)-idx0:]
        img_raw = Image.open(path)
        img_array = img_raw.load()
        # img_new = Image.new("RGB", img_raw.size, (255, 255, 255))
        img_new = Image.fromarray(np.asarray(img_raw))
        # img_new = img_array
        draw = ImageDraw.Draw(img_new)
        font = ImageFont.truetype('C:/Windows/fonts/Dengl.ttf', font_size) 
        print(img_array[0,9])
        def character_gen():
            while True:
                for i in range(len(text)):
                    yield text[i]
        
        ch_gen =character_gen()
        for x in range(0, img_raw.size[0], font_size):
            for y in range(0, img_raw.size[1], font_size):
                color = img_array[x, y]
                color = color[0]+50, color[1]+50, color[2]+50
                draw.text((x, y), next(ch_gen), font=font, fill=color, direction=None)
        path_abs = path_save + img_name +'_new' + '.' + file_type
        print(path_abs)
        img_new.convert('RGB').save(path_abs)

        end = time.time()
        print("=====================================")
        print("转换完成！！！用时 {:.2f} s！！！您可以继续进行转换操作！！！".format(end-start))
        print("=====================================")
        
window.close()
