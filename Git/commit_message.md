# commit message best practics:
 - ## This is a very good project:
    - ### https://www.conventionalcommits.org/en/v1.0.0/
# 1. format
```
<type>[optional scope]: <subject>

[optional body]

[optional footer]
```

### example:

```
perf(scroll)!: improve performance by 30%

Use passive event listeners for scroll handling.

JIRA-3463
BREAKING CHANGE: Requires modern browser support for passive events
```

### type:
- officail:
    - **feat**: A new feature
    - **fix**: A bug fix
    - **chore**: Maintenance task (e.g., updating dependencies)
        - database schema changes
        - Reorganizing file structures or renaming files for better organization
        - Adding missing semicolons, fixing indentation, or other style fixes
        - Cleaning up unused imports, variables, or dead code
        - Modifying environment configuration files (.env templates, config files)
        - Updating IDE settings or editor configurations
        - Changing logging configurations or debugging settings
        - Adjusting database migration scripts or seed data
        - Refactoring code structure without changing functionality
        - Updating license files or legal documentation
        - Updating build scripts, webpack configs, or bundler settings
        - Modifying package.json dependencies (adding/removing/updating)
        - Configuring linters, formatters, or code quality tools
        - Setting up CI/CD pipeline files (.github/workflows, .gitlab-ci.yml)
        - Updating Docker files or container configurations

    - **docs**: Documentation only changes
    - **style**: Code style changes (no logic change)
    - **‍refactor**: Code refactoring (no feature/bug change)
        - replacing a hardcoded integer constant with a class-level variable
    - **perf**: Performance improvements
    - **test**: Adding or modifying tests
    - **build**: Build system or dependency changes
    - **ci**: Changes to CI/CD configuration files (e.g., GitHub Actions, Travis, CircleCI)
    - **revert**: Reverts a previous commit
- others:
    - **wip:** Work in progress (not officially part of spec but often used locally)
        - alternative:
            - **DRAFT:** Similar to WIP, often used in place of WIP for clarity.
            - **IN PROGRESS:** More descriptive version of WIP.
            - **NOT READY:** Clear indication that changes are incomplete.
    - **config**: Change configuration files (e.g., .eslintrc,.babelrc)
    - **deploy**: Deployment-related changes
    - **init**: Initial commit/project setup
    - **merge**: Merge branch into another
    - **release**: Version bump or release tag 	
    - **script**: Add or modify helper scripts
    - **security**: Security-related fix or enhancement
    - **sync**: Sync two branches or external sources
    - **translation**: Translation updates
    - **typo**: Fix typos
    - **vendor**: Update third-party libraries or binaries

### scope: 
**Describes what part of the code was affected (e.g., component, module, file name).**
- **project**
- **auth**
- **router** 
- **auth**: Authentication logic  
- **api**: API-related changes (endpoints, clients, etc.)  
- **ui**: User interface components  
- **utils**: Utility/helper functions  
- **config**: Configuration files (e.g., webpack.config.js)  
- **db**: Database schema, queries, or connections  
- **deps**: Dependencies (e.g., package.json updates)  
- **build**: Build system or scripts  
- **ci**: Continuous integration pipelines (e.g., GitHub Actions, Travis)  
- **docs**: Documentation (even though it's also a type)  
- **style**: Styling/CSS/Sass/etc  
- **perf**: Performance-related areas  
- **test**: Testing framework or tests  
- **types**: TypeScript types/interfaces  
- **logging**: Logging infrastructure  
- **cache**: Caching logic  
- **routing**: Routing logic (especially in frontend apps)  
- **store**: State management (Redux, Vuex, etc.)  
- **state**: Also used for state management  
- **i18n**: Internationalization/localization  
- **network**: Network or HTTP handling  
- **security**: Security-related changes  
- **scripts**: Custom dev scripts  
- **server**: Backend server logic  
- **client**: Frontend/client-side logic  
- **mobile**: Mobile-specific code (React Native, Flutter, etc.)  
- **cli**: Command-line interface tools  
- **docker**: Dockerfiles or container config  
- **deploy**: Deployment scripts/configs  
- **lint**: Linting rules or fixes
     

### footer:
- **#123**
- **JIRA-123**
- **BREAKING CHANGE**


# 2. Write in the Imperative Mood:
Use commands like **"Add"**, **"Fix"**, **"Update"**, **"Remove"** instead of *"Added"*, *"Fixed"*, or *"Adding"*.

# 3. Clearly state **what was changed and why** (if not obvious).




