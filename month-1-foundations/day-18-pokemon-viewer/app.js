// Day 18: Pokemon Viewer

const typeColors = {
    fire: '#F08030', water: '#6890F0', grass: '#78C850', electric: '#F8D030',
    psychic: '#F85888', ice: '#98D8D8', dragon: '#7038F8', dark: '#705848',
    fairy: '#EE99AC', normal: '#A8A878', fighting: '#C03028', flying: '#A890F0',
    poison: '#A040A0', ground: '#E0C068', rock: '#B8A038', bug: '#A8B820',
    ghost: '#705898', steel: '#B8B8D0'
};

let currentId = null;
const display = document.getElementById('display');
const searchInput = document.getElementById('search-input');
const searchBtn = document.getElementById('search-btn');

async function fetchPokemon(nameOrId) {
    // TODO: Show loading state
    // TODO: fetch from https://pokeapi.co/api/v2/pokemon/{nameOrId}
    // TODO: Handle 404 (not found)
    // TODO: Handle network errors
    // TODO: Parse and display
}

function displayPokemon(data) {
    // TODO: Extract name, id, sprites, types, stats, abilities, height, weight
    // TODO: Build HTML card with:
    //   - Image (data.sprites.front_default)
    //   - Name and ID
    //   - Type badges with colors
    //   - Stat bars (HP, Attack, Defense, Sp.Atk, Sp.Def, Speed)
    //   - Nav buttons (Previous / Next)
    // TODO: Set currentId for navigation
}

function showError(message) {
    display.innerHTML = `<div class="error">${message}</div>`;
}

// Event listeners
searchBtn.addEventListener('click', () => {
    const query = searchInput.value.trim().toLowerCase();
    if (query) fetchPokemon(query);
});
searchInput.addEventListener('keypress', e => {
    if (e.key === 'Enter') searchBtn.click();
});

// Load Pikachu by default
fetchPokemon('pikachu');
