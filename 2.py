def buy_egg(tanggal, uang):
  jumlah_telur = uang // 2500
  bonus = 0
  for i in range(2, tanggal):
    if (tanggal % i) == 0:
      if (tanggal % 2) != 0:
        bonus = (jumlah_telur//12) * 3
    else:
      bonus = (jumlah_telur//12) * 2
  if (tanggal % 5) == 0:
    if (bonus % 2) == 0:
      bonus *= 10
    else:
      bonus *= 5
  print(jumlah_telur + bonus)
