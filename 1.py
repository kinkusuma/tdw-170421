def hitung_kembalian(total, uang):
  pecahan = [50000, 20000, 10000, 5000]
  kembalian = []
  kembalian_sblm = 0
  jmlh_kembalian = 1
  if total > 200000:
    total -= (total * 0.10)
  uang -= total
  for nominal in pecahan:
    while (uang - nominal) > 0:
      uang -= nominal
      kembalian.append(nominal)
  for i in range(len(kembalian)):
    while kembalian_sblm == kembalian[i]:
      jmlh_kembalian += 1
    print(jmlh_kembalian, 'x', kembalian[i])
    jmlh_kembalian = 1
  print('sisa :', uang, 'didonasikan')
