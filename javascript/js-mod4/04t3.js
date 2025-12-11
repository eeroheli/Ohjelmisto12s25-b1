'use strict';

async function searchtvmaze(searchstring) {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${searchstring}`);
    const results = await response.json();
    return results;
}

const searchform = document.querySelector('#tvmaze');
const inputtext = searchform.querySelector('input');
const resultsDiv = document.querySelector('#results');

searchform.addEventListener('submit', async function (event) {
    event.preventDefault();

    const query = inputtext.value.trim();
    if (query.length < 1) return;

    resultsDiv.innerHTML = '';

    const tvResults = await searchtvmaze(query);

    tvResults.forEach(tvShow => {
        const show = tvShow.show;
        const article = document.createElement('article');
        const h2 = document.createElement('h2');
        h2.textContent = show.name;
        article.appendChild(h2);
        const link = document.createElement('a');
        link.href = show.url;
        link.target = "_blank";
        link.textContent = "Show details";
        article.appendChild(link);
        const img = document.createElement('img');
        img.src = show.image?.medium || "";
        img.alt = show.name;
        article.appendChild(img);
        const summaryDiv = document.createElement('div');
        summaryDiv.innerHTML = show.summary;
        article.appendChild(summaryDiv);
        resultsDiv.appendChild(article);
    });
});
