'use strict';

const n1 = parseInt(prompt('anna eka luku'))
const n2 = parseInt(prompt('anna toka luku'))
const n3 = parseInt(prompt('anna kolmas luku'))
const sum = n1 + n2 + n3
const product = n1 * n2 * n3
const average = sum / 3
document.querySelector(".output").textContent = 'sum is: ' + sum + ' product is: ' +  product + ' average is: ' + average;