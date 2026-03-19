# Day 16: Async Data Dashboard

## What You're Building
A web page that fetches data from 3 free APIs simultaneously and displays a dashboard. Handle loading states and errors independently.

## What You'll Learn
- Promises — what they are and how they work
- `async` / `await` — modern async syntax
- `Promise.all()` — parallel async operations
- `fetch()` — the browser's HTTP client
- `try/catch` with async — error handling
- Loading states — spinners and placeholders

## Requirements
Fetch from 3 APIs simultaneously:
1. **Random Quote** — `https://api.quotable.io/random`
2. **Random Dog** — `https://dog.ceo/api/breeds/image/random`
3. **Random Joke** — `https://official-joke-api.appspot.com/random_joke`

Dashboard features:
- Fetch all 3 with `Promise.all()` (parallel, not sequential!)
- Loading spinner for each section while fetching
- Display data when it arrives
- Handle errors per-section ("Failed to load")
- "Refresh All" button + individual refresh buttons
- Show fetch time in milliseconds

## Key Concept
```javascript
// BAD — sequential (slow):
const data1 = await fetch(url1);
const data2 = await fetch(url2);

// GOOD — parallel (fast):
const [data1, data2] = await Promise.all([fetch(url1), fetch(url2)]);
```

## Stretch Goals
- Auto-refresh every 30 seconds
- Add more API sources
- Error retry with exponential backoff

## When You're Done
```
git add . && git commit -m "Day 16: Async dashboard with Promise.all" && git push
```
