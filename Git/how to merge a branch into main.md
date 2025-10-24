### summary:
```bash
git checkout main
git pull origin main

git merge user-authentication

git merge --no-ff user-authentication
# Use if you want to preserve branch history explicitly (creates a merge commit even if fast-forward is possible).

# (resolve conflicts if needed)

git push origin main
git branch -d user-authentication
```

### 1. Switch to the target branch
```bash
git checkout main          # or your target branch (e.g., develop)
```

### 2. Make sure your target branch is up to date
```bash
git pull origin main       # pulls latest changes from remote
```

### 3. Merge the feature branch
```bash
git merge feature-branch-name
```
- Git will attempt to perform a fast-forward merge (if possible) or create a merge commit. 

### 4. Resolve conflicts (if any) 
- resolve confilict:
```text
<<<<<<< HEAD
your code
=======
incoming code
>>>>>>> feature-branch-name
```

- `git add <file>`
- `git commit          # or just git merge --continue`

### 5. Push the merged result
```
git push origin main
```

### 6. Optional: Clean up (delete the merged branch)
```
# Delete locally
git branch -d feature-branch-name

# Delete on remote (if it exists there)
git push origin --delete feature-branch-name
```