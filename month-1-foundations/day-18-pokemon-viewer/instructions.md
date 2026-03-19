# Day 18: Pokemon Viewer (JavaScript)

## What You're Building
A Pokemon encyclopedia web app. Search by name, display sprite/stats/types, browse with next/previous, compare two Pokemon side-by-side.

## What You'll Learn
- Complete fetch workflow with complex API responses
- API pagination — navigating datasets
- Dynamic image loading from API URLs
- Error handling UI — user-friendly messages
- Responsive CSS
- Complex state management

## Requirements
1. **Search** — type name or ID, click Search
2. **Display:** name, ID, sprite, type badges (color-coded), stat bars, height/weight, abilities
3. **Navigation** — Previous/Next buttons to browse by ID
4. **Compare mode** — two Pokemon side-by-side with stat comparison
5. **Error handling** — "Pokemon not found", loading states

## API: `https://pokeapi.co/api/v2/pokemon/{name_or_id}` (no key needed)

## Type Colors
```javascript
const typeColors = {
    fire: '#F08030', water: '#6890F0', grass: '#78C850',
    electric: '#F8D030', psychic: '#F85888', ice: '#98D8D8',
    dragon: '#7038F8', dark: '#705848', fairy: '#EE99AC',
    normal: '#A8A878', fighting: '#C03028', flying: '#A890F0',
    poison: '#A040A0', ground: '#E0C068', rock: '#B8A038',
    bug: '#A8B820', ghost: '#705898', steel: '#B8B8D0'
};
```

## Stretch Goals
- Team builder (select 6)
- Evolution chain
- Random Pokemon button
- Cache fetched Pokemon to avoid re-fetching

## When You're Done
```
git add . && git commit -m "Day 18: Pokemon Viewer" && git push
```
