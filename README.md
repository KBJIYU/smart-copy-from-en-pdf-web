# smart-copy-from-en-pdf

## Activation Information

- **Create** Virtual Environment (Needed First time)
  - (WITH full anaconda pre-install packages) `conda create -n smartcopy python=3.6.6 anaconda`
    - In this case, we prefer to install all anaconda-pre-install-packages.
  - (WITHOUT full anaconda pre-install packages)`conda create -n smartcopy python=3.6.6`
- **Activate** Virtual Environment (Everytime)
  - `activate smartcopy`
- **Install** Packages Into Environment (Needed First Time, or some changes happened)
  - `(smartcopy) pip install -r requirements.txt`
- **export** Packages Into Environment (some packages changed)
  - `(smartcopy) pip freeze > requirements.txt`

---

## Packages Control

- In this case, we use **pip** to control packages.
  - `(smartcopy) pip freeze > requirements.txt`
  - `(smartcopy) pip install -r requirements.txt`
  - (do **NOT** use conda in this case)`conda list --export > condarequirements.txt`
  - (do **NOT** use conda in this case)`(smartcopy) conda install --yes --file condarequirements.txt`


---

## Naming System

- Files Naming
  - filename: all lowercase, can named with underscore.
  - foldername: all lowercase, without underscore.
- Coding Style(python)
  - refer to [PEP8](https://www.python.org/dev/peps/pep-0008/
  - single_trailing_underscore_
    - use `foo_` to prevent misleading built-in variables.
  - _single_leading_underscore
    - use `_foo` as class' hidden methods.
  - __double_leading_underscore
    - use `__foo` as class' name mangling.

---

## Git Commit Messages

- `[feat](file.py) add new func to avoid bra bra bra`
  - **Add** functions or useful codes.
- `[refactor](file.py) move func to bra bra bra`
  - **refactor**, but no new functions.
    - such as variables/functions/classes renaming.
- `[hotfix](file.py) fix func bug to avoid bra bra bra`
  - **fix** bug.
- `[env] add env requirement`
  - **change** or **modify** working environment settings.
- `[misc](file.py) add bra bra bra`
  - NOThing import use.
- `[data] add bra bra bra`
  - **change** static files.
