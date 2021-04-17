def segitiga(x='dumbwaysidujian'):
  num = len(x) // 2
  spasi = num - 1
  index = 0
  for i in range(num):
      for j in range(spasi):
          print(end=' ')
      spasi -= 1
      for j in range(1, i):
          print(x[index], end=' ')
          index += 1
      print('\r')
