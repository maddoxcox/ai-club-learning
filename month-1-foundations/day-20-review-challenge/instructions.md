# Day 20: Review Challenge — Study Buddy CLI

## What You're Building
A "Study Buddy" that combines EVERYTHING from Month 1 into one project.

## ALL Month 1 Concepts Used
- **Exceptions** (Days 1-2): Error handling throughout
- **Libraries** (Days 3-4): requests, rich, sys
- **Testing** (Day 5): pytest tests for core functions
- **File I/O** (Days 6-7): JSON save/load for study data
- **Regex** (Days 8-9): Input validation and text parsing
- **OOP** (Days 10-11): StudyTopic, Flashcard, StudySession classes
- **APIs** (Days 16-19): Fetch from Wikipedia API

## Requirements
Build `study_buddy.py`:
1. **Validates topic** with regex (alphanumeric, 3-50 chars)
2. **Fetches info** from Wikipedia: `https://en.wikipedia.org/api/rest_v1/page/summary/{topic}`
3. **OOP classes:** StudyTopic, Flashcard, StudySession
4. **Generates flashcards** from fetched content
5. **Quiz mode** — show flashcards, track correct/incorrect
6. **Saves progress** to JSON
7. **Loads past sessions**
8. **Error handling** — bad topics, API failures, corrupted files
9. **Rich output** — formatted terminal display
10. **Tests** — at least 5 pytest tests

## Menu
```
=== Study Buddy ===
[1] Study a new topic
[2] Review saved topics
[3] Take a quiz
[4] View progress
[5] Quit
```

## This is your Month 1 final project!
If you can build this, you've mastered the fundamentals and are ready for Month 2 (React + Claude API).

## When You're Done
```
git add . && git commit -m "Day 20: Study Buddy - Month 1 capstone" && git push
```
