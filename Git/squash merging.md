### when to use:
    1. Feature branches with messy or WIP commits (e.g., “fix typo”, “try again”, “broken”).
    2. You want a clean, readable project history in main.
    3. Your team prefers linear, high-level history over granular development steps.
    4. Common in GitHub/GitLab workflows for small-to-medium features.

### Option 1: Using `git merge --squash` (command line) 
```bash
git checkout main
git pull origin main
git merge --squash feature-branch
git commit -m "feat: add user login"
git push origin main
```
### Option 2: Via GitHub / GitLab UI 
- When merging a Pull Request (GitHub) or Merge Request (GitLab), choose:
    - "Squash and merge" (GitHub)
    - "Squash commits when merge request is accepted" (GitLab)
         
     

- **This does the squashing on the remote side—no local Git commands needed.**