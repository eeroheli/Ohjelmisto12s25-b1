'use strict';

let num = parseInt(prompt('how many participants'))
let participants = []
for (let i = 0; i < num; i++) {
    let name = prompt('what is name')
    participants.push(name)
}
participants.sort()

const ol = document.querySelector('.output');

participants.forEach(name => {
    const li = document.createElement('li');
    li.textContent = name;
    ol.appendChild(li);
});
