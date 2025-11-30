'use strict';
const names = ['John', 'Paul', 'Jones'];
let nameslist = '';

for (let i = 0; i < names.length; i++) {
  nameslist += `<li>${names[i]}</li>`;
}

document.getElementById("target").innerHTML = nameslist;
