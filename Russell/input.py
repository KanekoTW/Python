import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import datetime
import csv
import pandas as pd

#開始秒指定用のGUI
root = tk.Tk()
root.geometry("200x100")
root.title("開始秒指定")

def getTextInput():
    result=textExample.get("1.0","end")#ここに入力された値が代入される
    print(result)
    
    M = (float(result))#GUIで入力された数字を文字列から数値に変換して変数に代入

    list2 = []#経過時間取り出し用のリスト
    listS = []#　用のリスト

    c = 0#指定秒以降でループさせるために使用するカウンター

#開始秒の設定
    N = M#変数に変数を代入しているが、GUIを使用しない場合はここに直接数値を入力することで対応させるため

#CSVファイルの読み込み
    csv_file = open("./0730.csv", "r", encoding="ms932", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    for row in f:
          
        S = row#CSVファイル全データ(X値、Y値、出力時刻、経過時間)
        S2 = S[3]#経過時間のみを代入
        list2.append(S2)#経過時間の要素だけでリストを再編成

    nl = list(map(float, list2))#文字列から数値に変換

    while nl[c] < N:#指定秒以降のデータで処理を行わせるためのwhile文
           c+= 1

    def realtime_graph(x, y):
        line, = plt.plot(x, y, "ro", label="y=x")  # (x,y)のプロット
        plt.title("ラッセルの感情円環モデル", fontname="MS Gothic",fontsize=20)  # グラフタイトル
        plt.xlabel("不快/快", fontname="MS Gothic", fontsize=20)     # x軸ラベル
        plt.ylabel("非覚醒/覚醒", fontname="MS Gothic", fontsize=20)     # y軸ラベル
        plt.gca().set_aspect('equal', adjustable='box') #正方形に固定
        plt.grid()          # グリッド表示
        
        #出用時刻、経過時間描画
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
    
    #グラフ内円描画用
        a,b= [],[]
        for j in np.linspace(0, 2 * np.pi, 1000):
                a.append(math.sin(j)*990)#円の大きさ変更
                b.append(math.cos(j)*990)#円の大きさ変更
        plt.plot(a,b)

    (x, y) = (0, 0)     # 初期値
    plt.ion()           # インタラクティブモードオン

#指定開始秒からCSVファイルで読み込む
    with open('0730.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]

    D = l[c:]#CSVファイルから読み取るデータをカウンターの数から指定

    K = 0#取り出す行指定用変数
    for i in D:#(全行数-指定秒行目-1)
        K += 1
    
        Sx = i[0]
        Sy = i[1]
        z = i[2]
        t = i[3]
        
        #描画用数値
        realtime_graph(x, y)
        x = (float(Sx))#文字列から数値に変換
        y = (float(Sy))#文字列から数値に変換

label = tk.Label(root, text="0~59.9の数字を半角で入力")
label.pack() 

textExample=tk.Text(root, height=1)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Start", 
                    command=getTextInput)

btnRead.pack()

root.mainloop()
