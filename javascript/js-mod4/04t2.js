'use strict';

async function searchtvmaze(searchstring) {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${searchstring}`);
    const results = await response.json();
    console.log("tv maze results:", results);
    return results;
}

const searchform = document.querySelector('#tvmaze');
const inputtext = searchform.querySelector('input');

searchform.addEventListener('submit', async function (event){
    event.preventDefault();

    const query = inputtext.value.trim();

    if (query.length > 1) {
        const tvmazeresults = await searchtvmaze(query);
        console.log("event handler hakutulokset:", tvmazeresults);
    }
});