# Day 17: API Explorer

## What You're Building
A web app where you type any REST API URL, fetch it, and display the JSON response in a formatted, readable view with request history.

## What You'll Learn
- `fetch()` complete workflow
- HTTP methods — GET, POST, PUT, DELETE
- Status codes — 200, 201, 301, 400, 401, 403, 404, 500
- Response headers
- `JSON.stringify(data, null, 2)` — pretty-printing JSON
- Request history with localStorage

## Requirements
1. **URL input** + method selector (GET/POST/PUT/DELETE)
2. **Response display:** status code (color-coded), response time, headers, formatted JSON body
3. **Request history** — sidebar of recent requests, click to re-run
4. **Quick buttons** for sample URLs:
   - `https://pokeapi.co/api/v2/pokemon/pikachu`
   - `https://api.github.com/users/octocat`
   - `https://dog.ceo/api/breeds/image/random`
   - `https://jsonplaceholder.typicode.com/posts/1`

## Stretch Goals
- Request body input for POST
- Custom headers
- JSON syntax highlighting
- Export as cURL command

## When You're Done
```
git add . && git commit -m "Day 17: API Explorer" && git push
```
