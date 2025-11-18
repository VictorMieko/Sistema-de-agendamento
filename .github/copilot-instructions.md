<!-- .github/copilot-instructions.md - guidance for AI coding agents -->
# Copilot / AI Agent Instructions — Ted project

Purpose: Help an AI coding agent be immediately productive in this repository by describing the project's layout, expected conventions, and safe change patterns.

1) Big picture
- **Layout:** tiny MVC-like layout with a single entry point `main.py` and three folders: `controllers/`, `models/`, `view/`.
- **Runtime:** `main.py` is the canonical entrypoint. At present it is empty — contributors usually add CLI or app startup logic here.

2) Key files and directories
- **`main.py`**: app entry. Any runnable behaviour should be callable from here (e.g., `if __name__ == '__main__':`).
- **`controllers/`**: place request/command handlers. Files should be named `snake_case_controller.py` and contain a single controller class, e.g. `class UserController:`.
- **`models/`**: data classes or ORM models. Keep one model class per file named `snake_case.py` (e.g., `user.py` → `class User`).
- **`view/`**: UI or presentation helpers (templates, CLI printers). Keep simple functions like `render_<thing>()`.

3) Conventions & patterns (discoverable from current repo)
- Use `snake_case` filenames and `CamelCase` classes. Example: create `controllers/user_controller.py` with `class UserController:`.
- Keep modules small: one public class or related functions per file.
- No dependency manifest is present. If adding third-party packages, add `requirements.txt` at repo root and keep the list minimal.

4) Development workflows (project-specific)
- Run locally by invoking the entrypoint:
  ```powershell
  python main.py
  ```
- If you add dependencies:
  ```powershell
  python -m pip install -r requirements.txt
  ```
- Debug with VS Code by launching `main.py` (standard Python debug configuration). Use the integrated terminal (PowerShell) on Windows.

5) Safe editing rules for an AI agent
- Do not add large structural changes without a short PR-style note and asking the user first.
- Prefer adding small, self-contained files under the existing folders rather than moving them.
- When creating runnable code, include a minimal interaction example and mention how to run it in `README.md` or a short docstring.
- If you add external dependencies, update `requirements.txt` and include a one-line rationale in the commit message.

6) Examples (what to add and where)
- Controller example file: `controllers/user_controller.py`
  ```py
  class UserController:
      def list(self):
          # return a list of user-like dicts
          return []
  ```
- Model example file: `models/user.py`
  ```py
  from dataclasses import dataclass

  @dataclass
  class User:
      id: int
      name: str
  ```

7) What not to assume
- There are no tests, CI, or packaging files present — do not add CI configuration without asking.
- No database or external services are configured. If introducing one, include setup and teardown instructions.

8) If you need clarification
- Ask the user before implementing any behavior that requires external services, significant design choices, or large refactors.

---
If you want, I can: (a) initialize a minimal `README.md` and `requirements.txt`, (b) scaffold a sample controller/model and wire it into `main.py`, or (c) add a starter test harness. Which should I do next?
