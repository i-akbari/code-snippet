# 1. Delete remote branch
`git push origin --delete feature-branch-name`
- This does not affect your local branch

# 2. Delete local branch
`git branch -d feature-branch-name`

# 3. (Optional) Prune stale remote-tracking branches
`git remote prune origin`
-     The last command removes outdated references like origin/feature-branch-name from your local Git. 
     