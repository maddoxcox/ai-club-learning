# Day 15: Dynamic Quiz App

## What You're Building
A timed quiz web app. Questions load from a JS array, a timer counts down, tracks score, and shows results.

## What You'll Learn
- `setInterval` / `setTimeout` / `clearInterval`
- CSS class toggling — `classList.add()`, `classList.remove()`
- State management in vanilla JS
- Dynamic content from data arrays
- Event listeners on dynamically created elements

## Requirements
1. **Start screen** — title + "Start Quiz" button
2. **Quiz screen** — question, 4 answer buttons, 30-second timer, progress bar, score
3. **Answer feedback** — correct=green, wrong=red, 1.5s pause then next
4. **Timer** — counts down, yellow at <10s, red at <5s, auto-advances at 0
5. **Results** — final score, percentage, question review, "Play Again"

## Stretch Goals
- Fetch from Open Trivia DB API: `https://opentdb.com/api.php?amount=10`
- Difficulty levels with different timers
- High score leaderboard (localStorage)
- Animations between questions

## When You're Done
```
git add . && git commit -m "Day 15: Timed quiz app" && git push
```
