# Local Repository Skills Index

Entry point for `data/skills/` in `home_work`: lists local skills (`pr_loc`) excluded from shared indexes. Load this index rather than the full directory and use the routing map to open relevant skills. Decision order when norms are absent - `project_standards.md`, Section 07.06.

---

## Mandatory Application

Tagging this file requires applying relevant local skills, not merely reading the index:

1. Identify relevant skills via the routing map
2. Open the matched skill files and follow their instructions
3. Apply relevant skills whenever a matching task arises, even without explicit tagging

---

## Skill Registry

| Skill | Class | Scope | Auto-Apply | Version | Purpose |
|-------|-------|-------|------------|---------|---------|

## Anthropic Agent Skills (SKILL.md)

| Skill (dir) | Class | Scope | Version | Purpose |
|-------------|-------|-------|---------|---------|
| `search-sources` | local | - | 0.1.0 | Задает порядок поиска источников при решении учебных задач: каскад project_standards.md 07.06, context7 для документации библиотек, GitHub MCP для практик и аналогов, веб-поиск для текстов ошибок |
| `textbook` | local | - | 0.1.0 | Оформляет пояснение к задачам сессии в двух форматах - обычный текст и HTML-учебник со схемами-инфографикой по эталонному шаблону |

---

## Routing Map

Maps task topics to skills (`index_nav_standards.md`, Section 04).

| Task Topic | Skill |
|------------|-------|
| Задает порядок поиска источников при решении учебных задач | `search-sources` |
| Оформляет пояснение к задачам сессии в двух форматах - обычный текст и HTML-учебник со схемами-инфографикой по эталонному шаблону | `textbook` |

---

## Index Auto-Update

On any change to `data/skills/` (adding, removing, renaming, or updating skill frontmatter), rebuild this index with `glob-update-indexes`, refine purposes and routing map topics per `index_nav_standards.md` (Sections 03.03, 04), fix `metadata.purpose` and `metadata.topic` where the description yields a weak purpose or topic, and report added, updated, and removed entries.
