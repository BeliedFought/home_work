<!-- START static -->
# AGENTS.md

Standard version: 5.2.1

This file contains instructions for AI agents working with this project.

## Session Entry Points

- `@doc/standards/_index_standards.md` - standards package index (registry, routing map, package version); read it first
- `@doc/skills/_index_skills_repo.md` - repository skills index
- `@doc/specs/_index_specs.md` - specifications index
- `data/memory/memory.md`, `data/memory/decisions.md`, `data/memory/env.md` - agent memory minimum when `data/memory/` exists; update it after significant decisions
- Ignore `.backup/`, `.trash/`, `.arch/`, `.opencode/` unless the user explicitly asks
- Tagging an `@_index_*.md` file without a task runs its index auto-update procedure

## Language & Typography Matrix

| Contour | Artifacts | Language |
| --- | --- | --- |
| Human | Chat responses, `README.md`, user guides, `doc/specs/`, implementation plans, `doc/change_requests/` | Russian |
| User-facing output | Console strings, `report`, `menu`/`rich`, GUI widgets, `--help` through `t()` | English by default; Russian opt-in |
| Agent and code | `AGENTS.md`, `CLAUDE.md`, standards, indexes, skills, code, comments, docstrings, technical logs (`logger.*`), commit messages, subagent communication | English |

Typography applies to all contours: hyphen-minus `-` only (no em dash or en dash), letter `е` without diaeresis, no ellipsis, no emoji, no exclamation marks, no non-breaking or narrow spaces. User-facing output defaults to English; Russian is allowed through `t()`, `[app] language`, `LANGUAGE`, or a project override. Documentation, specifications, change requests, and chat stay Russian. User-facing text follows `doc/standards/human_text_standards.md`; the machine override is `~/.config/opencode/AGENTS.md`; the core rule is `project_standards.md` (04.03). This block is self-sufficient and keeps the rules for sessions where the machine layer is absent. When the machine layer is present, it takes precedence over this block; the two texts must not contradict. Do not remove the rules as duplicates.

The language split in the table above is self-sufficient and applies when the machine layer is absent. When the machine layer is present, its `## Language` section takes precedence on conflict; the two texts must not contradict.

## Development Process

- Use the superpowers skills: `brainstorming` (design exploration and task classification), `writing-plans` (specs and implementation plans), `test-driven-development`, `systematic-debugging`, `subagent-driven-development` or `executing-plans`, `verification-before-completion`, `writing-skills`.
- Classify work as Spike, Bounded, or Architectural before implementation; ratchet up when hidden complexity appears.
- Write specifications and plans in Russian; keep them in `doc/specs/` (`init/` before MVP, `spec_<module>.md` after).
- Delegate isolated search, audit, and verification work to subagents; briefs and answers are English, the user summary is Russian.
- Fact-checking cascade: local code and standards -> `context7` MCP -> `github` MCP -> web search for exact error text -> ask the user when unverifiable.

## Safety, Git & Boundaries

- Mutate code or the system only after the execution trigger `ДЕЛАЙ` or `GO`; design-stage approvals inside `brainstorming` do not replace it.
- Delete repository files only by moving them to `.trash/<slug>_<YYYYMMDDHHMM>/` with `MANIFEST.md`; exceptions: `tmp/` contents, git-native mirror/package synchronization, and `.trash/` purged only on explicit request.
- Run `sudo`, `su`, and `pkexec` only per the privilege levels in `project_standards.md` (05.04); never hardcode secrets.
- Git: one `master` branch; English Conventional Commits `<type>(<scope>): <imperative summary>`; authorship from `whoami` and `hostname`; no AI mention; never bump the package version without an explicit request.
- `CLAUDE.md` mirror: maintained permanently in the hub; deleted by default in derived repositories unless a repo override exists.
<!-- END static -->

<!-- START repo-specific -->
## Специфика репозитория: home_work

## Назначение

Репозиторий-контейнер для решения домашних учебных задач, в основном по программированию (основной язык - Python, встречаются SQL и базы данных). Работа сессионная: одна задача - одна сессия в папке `sessions/`.

Сам контейнер runnable-проектом не является: в корне нет `config/`, `src/`, `.venv`. Каркас и окружение создаются внутри сессии по потребности задачи. Отклонение от `project_standards.md` 07.03 зафиксировано в `doc/specs/overrides.md`.

Источник истины: `README.md` (структура для человека), этот файл (правила агента), `doc/specs/overrides.md` (отклонения от стандарта). Пакет `doc/standards/` - копия хаба `project_standards`, доступна только для чтения (раздел 07.05 стандарта).

<!-- START generated-commands -->
Не runnable-проект: команды установки, запуска, test/lint/typecheck/build на уровне репозитория отсутствуют. Окружение и зависимости создаются внутри сессии по потребности задачи.

Реальные операции:

- Создание сессии: папка `sessions/<YYYY-MM-DD_Русский-слаг>/` с обязательным `SESSION.md` (контракт - раздел 01.01.01 `project_standards.md`)
- Актуализация локальных индексов: навык `glob-update-indexes` (`_index_skills_repo.md`, `doc/specs/_index_specs.md`)
- Деплой навыков в инструменты: навык `glob-skill-deploy`
<!-- END generated-commands -->

## Поиск задания

Задания обычно приходят скриншотами из Telegram. Порядок:

1. Искать свежие изображения в загрузках Telegram: `~/Downloads/Telegram Desktop/` (файлы вида `photo_YYYY-MM-DD_HH-MM-SS.jpg`), при необходимости - `~/Pictures/Screenshots/`
2. Отобрать самые новые по времени изменения; задачи на нескольких скриншотах читать все, собирая единую картину
3. Извлечь условие, пример входа и выхода, язык, ограничения и комментарий учителя
4. Внутри сессии завести задачу `Задача_<NN>_<Русский-слаг>/`; условие записать в `spec.md`, скриншоты и данные - в `input/screenshots/` и `input/data/` задачи (все коммитится)

Методика поиска источников решения при неясностях - в навыке `search-sources`.

## Структура репозитория

Полная таблица - в `README.md`. Поведенческие правила:

- `sessions/` - контейнер сессий; сессия - папка с `SESSION.md`, соответствующая одному заданию (тесту, варианту); внутри - задачи `Задача_<NN>_<Русский-слаг>/`; отдельная сессия на каждую задачу не создается; вложенные сессии и `SESSION.md` в корне репозитория запрещены
- Папка задачи `Задача_<NN>_<Русский-слаг>/` - самодостаточная: `spec.md` (условие и ограничения), `input/screenshots/` (скриншоты задания), `input/data/` (входные данные), `output/code/` (версии решения `<Русский-слаг>_<NN>.py` одной нумерацией, финальный - последний номер); каркас - по потребности, лишние папки не создаются
- Слаги в этом репозитории - русские, без пробелов, слова через дефис, первое слово с заглавной буквы (идентификатор сессии, имя папки задачи, имя файла решения): `2026-09-24_Линейные-алгоритмы`, `Задача_01_Новое-число`, `Новое-число_05.py`. Это проектовый оверрайд к 01.01.01 и `code_standards.md` 02.01 (`doc/specs/overrides.md`)
- Артефакты сессии коммитятся полностью (проектовый оверрайд к 06.01 в `doc/specs/overrides.md`); исключаются только служебные каталоги (`.venv/`, `__pycache__/`, кэши) и `.trash/`
- К каждой сессии создается пояснение к задачам - отдельным документом, в двух форматах: `Объяснение_<идентификатор-сессии>.txt` (обычный текст) и `Объяснение_<идентификатор-сессии>.html` (оформление как учебник: разделы, наглядные схемы-инфографика, без внешних зависимостей). Имя содержит идентификатор сессии - пояснения разных сессий можно собрать в одну папку без перезаписи. Оба файла в корне сессии, содержание совпадает, тон - для начинающего. Эталон оформления - навык `textbook` (`templates/explanation.html`, `templates/explanation.txt`), дизайн не менять
- `HANDOFF.md` - общий разбор работы и уроки для новых агентов (что сделано, как решать задачи, какие ошибки не повторять)
- `doc/standards/` - только чтение; правится только в хабе `project_standards`
- `doc/specs/` - спецификации репозитория и оверрайды (`overrides.md`)
- `doc/skills/` - общие `glob-*` (только чтение, приходят синхронизацией)
- `data/skills/` - локальные навыки репозитория (слаг `pr_loc`, без префикса); индекс - `data/skills/_index_skills_pl.md`
- `doc/change_requests/` - задания на изменение (CR), коммитится с индексом
- `doc/agent_questions/` - транзитная: не коммитится, кроме `.gitkeep`
- `.trash/` - карантин; локальная, не коммитится

## Навыки репозитория

Общие навыки `glob-*` (реестр - `_index_skills_repo.md`) приходят из хаба синхронизацией и здесь не редактируются.

Локальные навыки репозитория (слаг `pr_loc`, без префикса, `data/skills/`; индекс - `data/skills/_index_skills_pl.md`):

- `search-sources` - порядок поиска источников решения: каскад 07.06, context7 для библиотек, GitHub для практик и аналогов, веб-поиск для ошибок
- `textbook` - оформление пояснения к задачам: текст и HTML-учебник с инфографикой по эталонному шаблону

## Типичные scope коммитов

`session` (работа в сессии), `sessions` (инфраструктура контейнера), `docs`, `skills`, `config`; идентификатор сессии или задачи в scope коммита (например `feat(2026-09-24_Линейные-алгоритмы): добавить решение`).

## Особенности

- Задачи проверяются автоматически: программа читает данные со стандартного ввода и печатает ответ в стандартный вывод. Формат вывода должен совпадать с ожидаемым точно; лишние строки, отладочный вывод и пояснения недопустимы (оверрайд в `doc/specs/overrides.md`)
- Ввод без подсказки: `input()` вызывается без аргумента; подсказки и служебный текст в стандартный вывод не печатаются
- Учебные сессии по задачам с автопроверкой не используют логгер, локализацию и конфигурацию; каркас сессии минимален
- Решение укладывается только в конструкции и операции, пройденные в школе (по комментарию учителя в задании и уточнениям пользователя); пользовательские функции, импорты, генераторы, f-строки и непройденные операции (например деление и остаток) не применяются, если это не задано условием. Что разрешено и откуда требование - записывается в спецификацию сессии. Приписывать учителю то, чего он не говорил (домысел агента), запрещено
- Скриншоты задания хранятся постоянными артефактами в `<task>/input/screenshots/`, данные - в `<task>/input/data/`; код решения - в `<task>/output/code/`; спецификация - в `<task>/spec.md`; все коммитится
- Все варианты решения фиксируются и не удаляются: `<task>/output/code/<Русский-слаг>_<NN>.py`, одна нумерация по порядку (`01`, `02`, ...); финальный - последний номер; причины смены вариантов описываются в спецификации задачи
- `doc/specs/spec_ui.html` - универсальный шаблон хаба; собственный UI-эталон создается в сессии, только если задача выводит данные пользователю и требует оформления
- Пакет стандартов обновляется только через хаб `project_standards` (навык `hub-sync-standards`); в этом репозитории `doc/standards/` не правится
<!-- END repo-specific -->

## Ссылки

- doc/standards/_index_standards.md - реестр стандартов и политика версионирования
- doc/standards/index_nav_standards.md - канон навигационных документов (индексы, каркас AGENTS.md - этого файла)
- doc/standards/repo_info_doc_standards.md - канон README и человеческих документов
- doc/standards/project_standards.md - раздел 06.01 (git и коммиты), 07.04 (версия пакета), 07.05 (редактирование стандарта)
- https://agents.md - канонический формат
