'use strict';

let num;
let list = []
let runnin = true
while (runnin == true){
    num =parseInt(prompt('give number'))
    if (list.includes(num) !== true){
        list.push(num)
    }
    else if (list.includes(num) == true){
        runnin = false
    }
}
list.sort((a, b) => a - b)
console.log(list)