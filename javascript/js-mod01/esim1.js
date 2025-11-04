'use strict'; // muista käyttää aina js alussa

// käytä const avainsanaa esittelyyn ja let jos arvoa muutetaan myöhemmin
const teksti = 'moi'
console.log('haha');
console.log(teksti);

//selaimen oma popup
alert('kukkuu')

//kirjoitetaan muuttujan avulla
document.querySelector('.output').textContent = teksti

let name = 'matti';
const greeting = `moi ${name}!`;

console.log(greeting);


//syötteen lukeminen
name = prompt('anna nimesi');
let age = parseInt(prompt('anna ikäsi'))
console.log('käyttäjän syöte ', name, age)
//if (age > 10) {
//else if () {

//math luokka
// noppaesim
const result = Math.ceil(Math.random()*6)
console.log(result)

switch (result) {
    case 1:
        console.log('Tuli ykköne');
        break;
    case 2:
        console.log('kakkone');
        break;
    case 3:
        console.log('kolmone');
        break;
}

//while käytetään kun ei tiedä tarkasti monta kertaa haluaa tehdä ja tekee niin pitkään ennen kuin toteutuu

let count = 0;
while (count <5){
    console.log('laskuri:',count)
    count++
}

//do while
//looppi suoritetaan ainakin kerran ennen ehtoa
let result2;

do {
    result2 = Math.floor(Math.random()*6)+1
    console.log(result)
} while (result2<6)


//tilsnteisiin jossa haluaa toistaa x määrä kertoja
//esim käydään taulukin indeksin läpi
for (let i = 0; i < 10; i++) {
    console.log('Luku on:', i)
}