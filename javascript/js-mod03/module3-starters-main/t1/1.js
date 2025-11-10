'use strict';

const ulElement = document.querySelector('#target');
const newLi1 = document.createElement('li');
ulElement.appendChild(newLi1);
const newLi2 = document.createElement('li');
ulElement.appendChild(newLi2);
const newLi3 = document.createElement('li');
ulElement.appendChild(newLi3);
newLi1.textContent = 'first item';
newLi2.textContent = 'second item';
newLi3.textContent = 'third item';