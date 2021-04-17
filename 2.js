function buyEgg(tanggal, uang){
  const jumlahTelur = uang / 2500;
  let bonusTelur = 0;
  for (let i=2; i<=tanggal; i++){
    if ((tanggal % i) === 0){
      if ((tanggal % 2) === 0){
        bonusTelur = Math.floor(jumlahTelur/12) * 3;
      }
    } else {
      bonusTelur = Math.floor(jumlahTelur/12) * 2;
    }
  } 
  if ((tanggal % 5) === 0){
    if ((tanggal % 2) === 0){
      bonusTelur *= 10;
    } else {
      bonusTelur *= 5;
    }
  }
  console.log(bonusTelur+jumlahTelur);
}
