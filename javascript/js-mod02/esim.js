

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
/**
 sort() sorts the array alphabetically
reverse() reverses the items in the array in reverse order
shift() deletes and returns the 1st item in the array
pop() deletes and returns the last item in the array
push(value) adds the value at the end of the array, multiple values separated by commas
includes(value) checks whether the array contains the given value
 */

fruits.sort()
console.log(fruits)
fruits.reverse()
console.log(fruits)

let ages = [2300, 234, 33, 19]
ages.sort()
console.log(ages)
ages.sort((a, b) => a - b)
console.log(ages)
ages.sort((a, b) => b - a)
console.log(ages)


