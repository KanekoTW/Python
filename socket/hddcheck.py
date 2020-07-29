import psutil 

dsk = psutil.disk_usage('/')


T = dsk.total
print("トータル",+ T)

U = dsk.used 
print("使用中",+ U)

F = dsk.free
print("空き容量",+ F)

#メガバイトに変換
FM = F/1000000
print("空き容量(mb)", +FM)
