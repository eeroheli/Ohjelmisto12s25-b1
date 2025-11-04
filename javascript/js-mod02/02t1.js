'use strict';

let num;
let list = []
for (let i = 0; i < 5; i++) {
    num = parseInt(prompt('give number'))
    list.push(num)
}
for (let i = list.length; i >= 0; i--) {
    console.log(list[i])
}
