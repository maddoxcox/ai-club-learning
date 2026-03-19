// Day 16: Async Data Dashboard

const APIS = {
    quote: 'https://api.quotable.io/random',
    dog: 'https://dog.ceo/api/breeds/image/random',
    joke: 'https://official-joke-api.appspot.com/random_joke'
};

async function fetchQuote() {
    // TODO: fetch, parse JSON, return {content, author}
}

async function fetchDog() {
    // TODO: fetch, parse JSON, return image URL
}

async function fetchJoke() {
    // TODO: fetch, parse JSON, return {setup, punchline}
}

function showLoading(elementId) {
    // TODO: Set element to "Loading..."
}

function showError(elementId, error) {
    // TODO: Show error message in red
}

async function fetchAndDisplay(source) {
    // TODO: Show loading, record start time, fetch, record end time, display result
}

async function refreshAll() {
    // TODO: Promise.all to fetch all 3 in parallel!
}

document.getElementById('refresh-all').addEventListener('click', refreshAll);
// TODO: Add listeners to individual refresh buttons

refreshAll(); // Load on page open
