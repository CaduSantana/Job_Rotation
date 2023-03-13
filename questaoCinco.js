// 5) Escreva um programa que inverta os caracteres de um string.
const stringTeste = "Hello World!";
// Primeiro, quebra-se a string em um array de caracteres. Depois, inverte-se o array, pegando do final da sequência e colocando no início, iterativamente. Por fim, junta-se o array em uma string novamente.
const stringTesteSeparada = stringTeste.split("");
const stringTesteSeparadaInvertida = [];
for (let i = stringTesteSeparada.length - 1; i >= 0; i--) stringTesteSeparadaInvertida.push(stringTesteSeparada[i]); // Itera do final para o início do array
const stringTesteInvertida = stringTesteSeparadaInvertida.join("");

console.log(stringTesteInvertida);