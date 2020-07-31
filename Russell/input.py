import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import datetime
import csv
import pandas as pd


root = tk.Tk()
root.geometry("200x100")
root.title("開始秒指定")

def getTextInput():
    result=textExample.get("1.0","end")#ここに入力された値が
    print(result)
    
    M = (float(result))


    list2 = []
    listS = []

    c = 0

#開始秒の設定
    N = M


    csv_file = open("./0730.csv", "r", encoding="ms932", errors="", newline="" )

    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    for row in f:
          
        S = row
        S2 = S[3]
        #print(S2[3])
        list2.append(S2)    

    nl = list(map(float, list2))

    while nl[c] < N:
           c+= 1#c = 設定した開始秒の行数


    def realtime_graph(x, y):
        line, = plt.plot(x, y, "ro", label="y=x")  # (x,y)のプロット
        plt.title("ラッセルの感情円環モデル", fontname="MS Gothic",fontsize=20)  # グラフタイトル
        plt.xlabel("不快/快", fontname="MS Gothic", fontsize=20)     # x軸ラベル
        plt.ylabel("非覚醒/覚醒", fontname="MS Gothic", fontsize=20)     # y軸ラベル
        plt.gca().set_aspect('equal', adjustable='box') #正方形に固定
        plt.grid()          # グリッド表示
        z = Sz
        t = St
    
        boxdic = {
            "facecolor" : "lightgreen",
            "edgecolor" : "darkred",
            "boxstyle" : "Round",
            "linewidth" : 2
        }
        plt.text(1050, 600,z,size = 10, bbox = boxdic)#出力時刻
        plt.text(1050, 400,t,size = 10, bbox = boxdic)#経過時間
        
        plt.xlim([-1000, 1000])    # x軸範囲
        plt.ylim([-1000, 1000])    # y軸範囲
        plt.draw()          # グラフの描画
        plt.pause(0.01)     #処理時間
        plt.clf()  # 画面初期化
    
        a,b= [],[]
        for j in np.linspace(0, 2 * np.pi, 1000):
                a.append(math.sin(j)*990)#円の大きさ変更
                b.append(math.cos(j)*990)#円の大きさ変更
        plt.plot(a,b)

    (x, y) = (0, 0)     # 初期値
    plt.ion()           # インタラクティブモードオン



    with open('0730.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]

    D = l[c:]

    youso = sum([1 for _ in open('0730.csv')])

    K = 0

    for i in range(youso - c -1):
        K += 1
    
        Sx = D[K][0]
        Sy = D[K][1]
        Sz = D[K][2]
        St = D[K][3]

        realtime_graph(x, y)
        x = (float(Sx))
        y = (float(Sy))


label = tk.Label(root, text="0~59.9の数字を半角で入力")
label.pack() 

textExample=tk.Text(root, height=1)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read", 
                    command=getTextInput)

btnRead.pack()

root.mainloop()
