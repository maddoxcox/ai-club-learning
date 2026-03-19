// Day 17: API Explorer

const urlInput = document.getElementById('url-input');
const methodSelect = document.getElementById('method');
const sendBtn = document.getElementById('send-btn');
const statusEl = document.getElementById('status');
const timeEl = document.getElementById('time');
const bodyEl = document.getElementById('body');
const historyList = document.getElementById('history-list');

let history = JSON.parse(localStorage.getItem('api-history') || '[]');

async function sendRequest() {
    // TODO: Get URL and method
    // TODO: Record start time
    // TODO: fetch() with the selected method
    // TODO: Record end time
    // TODO: Display status code (color: green 2xx, yellow 3xx, red 4xx/5xx)
    // TODO: Display response time
    // TODO: Display formatted JSON (JSON.stringify with indent)
    // TODO: Add to history
    // TODO: Handle errors
}

function addToHistory(method, url, status) {
    // TODO: Add to history array
    // TODO: Save to localStorage
    // TODO: Render history list
}

function renderHistory() {
    // TODO: Display history items, click to re-run
}

// Sample URL buttons
document.querySelectorAll('.sample-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        urlInput.value = btn.dataset.url;
        sendRequest();
    });
});

sendBtn.addEventListener('click', sendRequest);
urlInput.addEventListener('keypress', e => { if (e.key === 'Enter') sendRequest(); });

renderHistory();
