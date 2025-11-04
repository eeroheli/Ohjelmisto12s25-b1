'use strict';

const name = prompt('whats your name')
const num = Math.ceil(Math.random()*4)
let tupa;
switch (num){
    case 1:
        tupa = 'Gryffindor'
        break
    case 2:
        tupa = 'Slytherin'
        break
    case 3:
        tupa = 'Hufflepuff'
        break
    case 4:
        tupa = 'Ravenclaw'
        break
}
document.querySelector(".output").textContent = `${name}, you are a ${tupa}! `;