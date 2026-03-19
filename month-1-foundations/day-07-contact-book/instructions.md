# Day 7: Contact Book

## What You're Building
A CLI contact manager where you can add, search, edit, and delete contacts. Everything persists in a JSON file so your contacts survive between runs.

## What You'll Learn
- `json.load()` / `json.dump()` — reading and writing JSON
- JSON structure — how data is organized
- File read/write — persistent data storage
- CRUD operations — Create, Read, Update, Delete
- Menu-driven CLI programs

## Requirements
Build `contact_book.py` that:

1. **Stores contacts as JSON** in `contacts.json`:
   ```json
   [
     {
       "id": 1,
       "name": "Alice Johnson",
       "phone": "555-0101",
       "email": "alice@email.com",
       "category": "friend"
     }
   ]
   ```

2. **Menu options:**
   - `[1] Add contact` — prompt for name, phone, email, category
   - `[2] Search contacts` — search by name (partial match)
   - `[3] List all contacts` — show all contacts formatted
   - `[4] Edit contact` — find by name, then edit any field
   - `[5] Delete contact` — find by name, confirm before deleting
   - `[6] Export to CSV` — save contacts as a CSV file
   - `[7] Quit`

3. **Data persistence:**
   - Load contacts from JSON on startup
   - Save to JSON after every change
   - Handle missing file (first run)
   - Handle corrupted JSON file gracefully

4. **Search features:**
   - Case-insensitive search
   - Partial name matching ("ali" finds "Alice")
   - Search by category

## How to Work
- Start with the JSON read/write functions
- Build the add and list features first
- Then add search, edit, delete
- Add export to CSV last

## Stretch Goals
- Add contact groups/tags
- Add a "favorites" feature
- Import contacts from a CSV file
- Add phone number formatting validation

## When You're Done
```
git add .
git commit -m "Day 7: Contact Book with JSON persistence"
git push
```
