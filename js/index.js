function sorteio(params) {
  const lista = ["pirulito", "bala", "chiclete", "paçoca"];
  const escolhido= lista[Math.floor(Math.random() * lista.length)];

  alert(`parabens voce ganhou: ${escolhido} 
  `);
}
