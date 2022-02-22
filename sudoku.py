import tkinter
import random
from tkinter.font import NORMAL
from sudoku_board import *

window = tkinter.Tk()
window.title("sudoku")
window.geometry("1500x900+200+100")

canvas = tkinter.Canvas(width=900,height=900,bg="white")
canvas.pack()
dic = {}
num_button_dic = {}
click_xy_buttom = []
click_num_button = []

def input_num(x,y):
    def input_num2():
        click_xy_buttom.append([x,y])
        print(x,y)
        for i in range(9):
            num_button = num_button_dic[i+1]
            num_button["state"] = 'normal'

    return input_num2


def draw_input(num):
    def draw_input2():
        click_num_button.append(num)
        for i in range(9):
            num_button = num_button_dic[i+1]
            num_button["state"] = 'disable'
        print(click_num_button)
    
    

    return draw_input2




for x in range(9):
    for y in range(9):
        point = [0+100*y,0+100*x,0+100*y,100+100*x,100+100*y,100+100*x,100+100*y,0+100*x]
        
        canvas.create_polygon(point,outline="black",fill="white",width=1)

for x in range(1,4):
    canvas.create_line(0,x*300,900,x*300,fill="red",width=2)
for y in range(1,4):
    canvas.create_line(y*300,0,y*300,900,fill="red",width=2)

#스도쿠판 버튼 생성
for x in range(9):
    for y in range(9):
        button1 = tkinter.Button(window,command = input_num(x+1,y+1),text = "%d,%d"%(x+1,y+1),width='2')
        dic[(x,y)] = button1
        button1_window = canvas.create_window(20+100*y,20+100*x,window=button1)

#랜덤 스도쿠 보드 생성
board_num = random.randrange(1,7)
for i in range(9):
    for j in range(9):
        board_text = sudoku_board_1[i][j]
        random_num = random.randrange(1,11)
        if random_num >= 6:
            canvas.create_text(50+100*j,50+100*i,text = board_text,font=("Purisa",50))

#우측 버튼 생성
for i in range(9):
    num_button = tkinter.Button(window,command = draw_input(i+1),text='%d'%(i+1),font=("Purisa",30),state=tkinter.DISABLED)
    num_button_dic[i+1] = num_button
    num_button.place(x=1300,y=100*i)








window.mainloop()
