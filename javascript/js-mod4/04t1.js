'use strict';
async function searchtvmaze(searchstring){
    const response=  fetch('https://api.tvmaze.com/search/shows?q=' + searchstring)
    const results = await response.json()
    console.log('tv maze results: ' + results)
    return results;
}
const searchform = document.querySelector('form#tvmaze')
const inputtext = searchform.querySelector('input')
searchform.addEventListener('submit', async function (event){
    event.preventDefault();
    if (inputtext.value.length > 1) {
        const tvmazeresults = await searchtvmaze(inputtext.value)
        console.log('event handler hakutulokset' + tvmazeresults)
    }
})