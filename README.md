# uv-init-template
- python project creator
- This is a small wrapper on uv to use a target repo or project as a base
- pass in a git repo link or store it in the `KNOWN_PROJECTS`
- if no template is given it will use the base uv init

use case:
```
./uv-init project_name https://repo.link
```

- feel free to submit a pr for good templates
## extra info
youll need to alias and point it to the correct file

## todo
- [ ] make a file that has a list of good base projects and starter repos
- [x] add support for parsing the uv pyproject.toml 
