# Day 13: Git Branching Challenge

## What You're Building
No code today — you're mastering git branching through an interactive tutorial and practice on your real repos.

## What You'll Learn
- `git branch` / `git checkout` / `git switch`
- `git merge` and `git rebase`
- Pull Requests on GitHub
- Merge conflicts — creating and resolving them

## Part 1: Learn Git Branching (45 min)
Go to https://learngitbranching.js.org/ and complete:
- **Introduction Sequence** (all levels)
- **Ramping Up** (all levels)
- **Push & Pull** remote sections

## Part 2: Practice on Your Real Repo (45 min)

### Exercise 1: Feature Branch
```bash
cd ~/ai-club-learning
git checkout -b feature/add-readme-updates
# Make a change to README.md
git add README.md && git commit -m "Update README"
git push -u origin feature/add-readme-updates
# Create a Pull Request on GitHub, merge it
git checkout main && git pull
```

### Exercise 2: Create a Merge Conflict
```bash
git checkout -b conflict-branch-a
# Edit line 5 of README.md, commit
git checkout main
git checkout -b conflict-branch-b
# Edit the SAME line 5 differently, commit
git checkout main
git merge conflict-branch-a   # Works fine
git merge conflict-branch-b   # CONFLICT! Resolve it manually.
```

## Checklist
- [ ] Completed learngitbranching.js.org intro + remote levels
- [ ] Created and merged a feature branch via PR
- [ ] Created and resolved a merge conflict
- [ ] Comfortable with: branch, checkout, merge, push, pull
