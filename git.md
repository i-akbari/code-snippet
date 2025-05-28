# commit message best practics:
 1. Use a Clear Structure:

    **Subject Line:** Start with a short (50–72 characters) summary of the change in the imperative mood (e.g., "Add", "Fix", "Update"). This is the first line of the commit message.

    **Body (Optional):** Provide additional context or details in a separate paragraph, wrapping lines at 72 characters for readability.

    **Example:**

 ```
Add user authentication endpoint

Implement the /login endpoint with JWT-based authentication.
Include validation for email and password fields.
Update user model to support new auth fields.
```

2. Write in the Imperative Mood:

    Use commands like **"Add"**, **"Fix"**, **"Update"**, **"Remove"** instead of *"Added"*, *"Fixed"*, or *"Adding"*.

3. Clearly state **what was changed and why** (if not obvious).

4. Format: **type (scope): description**

    **Types:** **feat (new feature), fix (bug fix), docs (documentation), style (formatting), refactor, test, chore (maintenance), etc.**

    **Scope:** Optional; specifies the module or area (e.g., auth, ui, api).

**Example:** "Update README with installation instructions" (clear and concise).

 - ## This is a very good project:
    - ### https://www.conventionalcommits.org/en/v1.0.0/

# git commands
### git log --oneline