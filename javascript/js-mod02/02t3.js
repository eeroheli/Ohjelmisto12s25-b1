'use strict';


let list = []
let name
for (let i = 0; i < 6; i++) {
    name = prompt('give dog name')
    list.push(name)
}
list.sort()
list.reverse()
const ul = document.querySelector('.output');

list.forEach(name => {
    const li = document.createElement('li');
    li.textContent = name;
    ul.appendChild(li);
});
