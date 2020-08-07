from flask import Flask, render_template, make_response
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random
import numpy as np


app = Flask(__name__)

fig = plt.figure()#　クラスのインスタンス化
ax = fig.add_subplot()#　オブジェクト作成

#  x、yの値を設定
x = np.arange(0,100,0.1)
y = x**2

@app.route('/')
#グラフを作成
def index():
  plt.cla()

  plt.title('Graph')
  plt.legend()
  plt.grid()
  plt.xlabel('x')
  plt.ylabel('y')
  plt.plot(x, y)
  

  canvas = FigureCanvasAgg(fig)#　画像を出力
  png_output = BytesIO()#　仮想的にメモリに書き出し
  canvas.print_png(png_output)
  data = png_output.getvalue()#　Date＝画像データ

  response = make_response(data)#　Dateをレスポンス(response)で生成
  response.headers['Content-Type'] = 'image/png'
 

  return response


if __name__ == "__main__":
  app.run()
