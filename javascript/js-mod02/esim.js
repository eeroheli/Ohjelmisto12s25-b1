

//taulukko array
let item = [1, 2, 3, {name: 'ulla'}, [1,2,3], 'merkkijono']
console.log(item)

//alkioon viitataan indeksillä
console.log(item[3])

//alkion arvoa voidaan muuttaa indeksin sisällä
item[0] = 99

item[9] = 'olen uusi alkio'
console.log(item)

//välissä on nyt määrittelemätön alkio
console.log(item[6])

let fruits = ['banaani', 'mango', 'pear', 'apple']

let elem = document.querySelector('#heading');
console.log(elem);
console.dir(elem)



// taulukon looppaus eri tavoin
//perinteinen for
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i])
}

//läpikäynti for of rakenteella saadaan arvot
for (let fruit of fruits) {
    console.log(fruit)
}
//läpikäynti for in rakenteella saadaan arvot ja index
//harvemmin käytetään taulukoiden kanssa enemmän objektien
for (let index in fruits) {
    console.log(index + fruits[index])
}
