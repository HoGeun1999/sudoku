from distutils import command
from re import T
from tabnanny import check
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
check = True
num_button_dic = {}
realtime_board = [[0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0]]

make_board = [    [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0]]

def input_num(x,y):
    def input_num2():
        if realtime_board[x-1][y-1] == 0:
            for i in range(9):
                num_button = num_button_dic[i+1]
                num_button["state"] = 'normal'
                num_button.configure(command = draw(x,y,i+1))
        else:
            for i in range(9):
                num_button = num_button_dic[i+1]
                num_button["state"] = 'normal'
                num_button.configure(command = change_text(x,y,i+1))
        del_button.configure(command=del_text(x,y))

    return input_num2

def draw(x,y,num):
    def draw2():
        check = True
        canvas.create_text(50+100*(y-1),50+100*(x-1),text =num,font=("Purisa",50))
        realtime_board[x-1][y-1] = num
        for i in range(9):
            num_button = num_button_dic[i+1]
            num_button["state"] = 'disable'

        for i in range(9):
            for j in range(9):
                if realtime_board[i][j] == 0:
                    check = False
        if check == True:
            if realtime_board in sudoku_board_list:
                text_bnt = tkinter.Button(window,text='정답',font=("Purisa",30))
                text_bnt.place(x=100,y=500)
            else:
                text_bnt = tkinter.Button(window,text='오답',font=("Purisa",30))
                text_bnt.place(x=100,y=500)
            
    return draw2

def del_text(a,b):
    def del_text2():
        realtime_board[a-1][b-1] = 0
        for x in range(9):
            for y in range(9):
                point = [0+100*y,0+100*x,0+100*y,100+100*x,100+100*y,100+100*x,100+100*y,0+100*x]
                canvas.create_polygon(point,outline="black",fill="white",width=1)
        for x in range(1,4):
            canvas.create_line(0,x*300,900,x*300,fill="red",width=2)
        for y in range(1,4):
            canvas.create_line(y*300,0,y*300,900,fill="red",width=2)
        for x in range(9):
            for y in range(9):
                button1 = tkinter.Button(window,command = input_num(x+1,y+1),text ="%d,%d"%(x+1,y+1),width='2')
                dic[(x,y)] = button1
                button1_window = canvas.create_window(20+100*y,20+100*x,window=button1)
        for i in range(9):
            for j in range(9):
                if make_board[i][j] != 0:
                    canvas.create_text(50+100*j,50+100*i,text = make_board[i][j],font=("Purisa",50))
                    button = dic[(i,j)]
                    button["state"] = 'disable'
        for i in range(9):
            for j in range(9):
                if make_board[i][j] != realtime_board[i][j]:
                    canvas.create_text(50+100*j,50+100*i,text = realtime_board[i][j],font=("Purisa",50))
        
    return del_text2


def change_text(a,b,num):
    def change_text2():
        del_text(a,b)()
        draw(a,b,num)()

    return change_text2

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
        button1 = tkinter.Button(window,command = input_num(x+1,y+1),text ="%d,%d"%(x+1,y+1),width='2')
        dic[(x,y)] = button1
        button1_window = canvas.create_window(20+100*y,20+100*x,window=button1)

#랜덤 스도쿠 보드 생성
sudoku_board_num = random.choice(sudoku_board_list)
for i in range(9):
    for j in range(9):
        board_text = sudoku_board_num[i][j]
        random_num = random.randrange(1,11)
        if random_num >= 2:
            canvas.create_text(50+100*j,50+100*i,text = board_text,font=("Purisa",50))
            button = dic[(i,j)]
            button["state"] = 'disable'
            realtime_board[i][j] = board_text
            make_board[i][j] = board_text

#우측 버튼 생성
for i in range(9):
    num_button = tkinter.Button(window,text='%d'%(i+1),font=("Purisa",30),state=tkinter.DISABLED)
    num_button_dic[i+1] = num_button
    num_button.place(x=1300,y=100*i)

del_button = tkinter.Button(window,text='지우기',font=("Purisa",30))
del_button.place(x=100,y=100)

window.mainloop()
