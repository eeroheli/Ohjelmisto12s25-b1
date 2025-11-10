'use strict';

// hae viittaus kaikkiin output class elementteihin taulukkona
const outputElement =
    document.getElementsByClassName('output');
console.log(outputElement);

// viittaus yhteen elementtiin id:n perusteella
const outputElement2 =
    document.getElementById('output');
console.log(outputElement2);

// viittaus kaikkiin p-elementteihin tagin perusteella
const outputElement3 =
    document.querySelectorAll('p');
console.log(outputElement3)

// viittaus koko body-elementtiin
const body = document.querySelector('body');
body.querySelector('#output');

// Listan (ul) käsittely
const ulElement = document.querySelector('ul');
const newLi = document.createElement('li');
ulElement.appendChild(newLi);
newLi.textContent = 'Uusi itemi';

// innerHTML-esimerkki
//ulElement.innerHTML = '<li>uusi itemi</li><li>Toinen uusi</li>';

// haetaan viittaus kaikkiin li-elementteihin listan sisällä
const liElems = ulElement.querySelectorAll('li');
for (let i= 0; i<liElems.length; i++) {
    // muutetaan jokaisen li-elementin sisältöä perustuen taulukon indeksin arvoon
    liElems[i].textContent = `${i+1}. itemi`;
}

// luodaan html-lista, jossa sisältö js-taulukosta
const inventory = ['kynä', 'kumi', 'läppäri', 'reppu'];
const inventoryOlElem = document.createElement('ol');
for (const item of inventory) {
    // luodaan html li-elementit ja sijoitetaa ol-elementi lapsiksi
    const liElem = document.createElement('li');
    liElem.textContent = item;
    inventoryOlElem.appendChild(liElem);
}
// lisätään luotu lista DOMiin käyttäen aiemmin haettu viittausta body-elementtiin
const inventoryHeader = document.createElement('h2');
inventoryHeader.textContent = 'Inventaario';
body.appendChild(inventoryHeader);
body.appendChild(inventoryOlElem);
inventoryHeader.classList.add('red')

const button = document.querySelector('button')
//sidotaan tapahtuma ja tapahtumakäsittelijöitä yhteen
button.addEventListener('click', buttonClick());
//erillinen tapahtuman käsittelyfunkitio
function buttonClick() {
    console.log('nappulaa klikattu')
}
//käsitellään sisällä eli nimetön funktio
inventoryHeader,addEventListener('click',function (){
    console.log('otsikkoa klikattu')
    inventoryHeader.classList.toggle('red')
})

//näppäimistö tapahtumat
let inputstring = ''
document.addEventListener('keypress', function (event:){
    console.log('näppäintä painettu')
    inputstring += event.key
    if (event.key === 'Enter') {
        outputElement2.classList.remove('blue')
        outputElement2.classList.add('red')
    }
    //outputElement2.classList.add('blue')
    outputElement2.textContent = 'nappia painettu: ' + inputstring
})

//hiiiri tapahtumat
document.addEventListener('mousemove', function (event){
    console.log('hiiri liikkuu', event)
    outputElement[0].textContent = `hiiren sijainti: ${event.screenX},${event.screenY}`
})