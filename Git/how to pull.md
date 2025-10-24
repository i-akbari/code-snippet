```bash
git branch

git checkout <branch-name> 
# or 
git switch <branch-name>

git pull # By default, git pull pulls from the remote branch that your current branch is tracking (usually origin/<current-branch>). 
# or
git pull <remote> <branch> # If you want to be explicit (or pull from a different remote/branch): 
git pull origin main
```

### Uncommitted changes: 
**If you have uncommitted local changes, Git may refuse to pull to avoid overwriting your work.**
Either:
1. Commit your change
```
git add .
git commit -m "Your message"
```

2. stash them temporarily
```
git stash
git pull
git stash pop
```

### Conflicts: 
If there are merge conflicts, Git will pause and ask you to resolve them manually. 