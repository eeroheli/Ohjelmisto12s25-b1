'use strict';

let num;
let list = []
while (num !== 0){
    num =parseInt(prompt('give number (0 stops)'))
    list.push(num)
}
list.sort((a, b) => b - a)
console.log(list)