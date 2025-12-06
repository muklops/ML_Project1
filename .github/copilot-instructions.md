## Repository Overview

- **Package layout:** source code lives under `src/MLProject/` (packages discovered via `package_dir={"": "src"}` in `setup.py`). Key folders: `config/`, `utils/`, `entity/`, `pipeline/`, `components/`.
- **Artifacts & config:** runtime config is in `configs/config.yaml` and the repo uses an `artifacts` directory (see `configs/config.yaml`) for data, unzip, model and metric outputs.
- **Notebooks & experiments:** research notebooks are under `research/` (e.g., `research/data_ingestion.ipynb`) and show canonical usage patterns for the configuration and ingestion steps.

## What to know up front (big picture)

- The project is organized as a small ML pipeline where configuration drives directory structure and data flow. `configs/config.yaml` declares artifact roots and per-step paths (data_ingestion, data_validation, data_transformation, model_trainer, model_evaluation).
- Utilities in `src/MLProject/utils/` provide common helpers: YAML/JSON readers, binary save/load, directory creation and a module-level `logger` configured in `src/MLProject/utils/__init__.py`.
- Many research examples (including a `ConfigurationManager` and `DataIngestion` flow) exist in `research/data_ingestion.ipynb` — use them as canonical reference when implementing missing code in `src/`.

## Developer workflows & commands

- Install dependencies: `pip install -r requirements.txt` then install package editable: `pip install -e .` (requirements already contains `-e .`).
- Run quick smoke: `python main.py` (this imports `src.MLProject.utils.logger` and emits a log line).
- Run notebooks: open `research/*.ipynb` in Jupyter or VS Code. Notebooks change CWD to repository root early (`%cd "c:/Users/.../ML_Project1"`) — maintain that convention when running cells.
- Packaging: `python setup.py sdist bdist_wheel` will use `src/` as package dir (see `setup.py`).

## Patterns & conventions observed in this repo

- Config-first design: most classes expect dataclasses or ConfigBox objects created from YAMLs. Use `src/MLProject/utils/common.py`'s `read_yaml` (returns `ConfigBox`) when loading config.
- Centralized logger: `src/MLProject/utils/__init__.py` configures logging to `logs/running_logs.log`. Use `from src.MLProject.utils import logger` to access it. Note: some files reference `from mlProject import logger` (case mismatch); prefer the explicit `src.MLProject` import in new code.
- Artifacts layout: tasks write/read from paths under the `artifacts` folder as declared by `configs/config.yaml`. Use `create_directories([...])` from `utils.common` before writing.

## Integration points & external dependencies

- External storage: initial data ingestion downloads a zip from `data_ingestion.source_URL` declared in `configs/config.yaml` (example URL points to a GitHub-hosted zip). Data ingestion extracts to `artifacts/data_ingestion`.
- MLFlow is listed in `requirements.txt` (`mlflow==2.2.2`) — experiments / tracking may be expected; no runner is present in `src/` yet.
- The repo expects standard scientific stack: `pandas`, `scikit-learn`, `numpy`, etc. Tests are not present.

## Typical tasks the agent will be asked to do (and how to approach them)

- Implement missing config code: `src/MLProject/config/configuration.py` is currently empty while research notebooks contain a `ConfigurationManager`. Use the notebook `research/data_ingestion.ipynb` implementation as canonical and port it into `src/MLProject/config/configuration.py`.
- Implement pipeline components: inspect `src/MLProject/components/` and `pipeline/` for placeholders; follow the patterns in `utils.common` for file I/O, logging, and directory creation.
- Maintain YAML-driven behaviour: prefer reading `configs/config.yaml`, `params.yaml`, and `schema.yaml` (when present) rather than hard-coding paths.

## Concrete examples (copy-paste safe)

- Read config and create artifacts directory (pattern used in notebooks):

```py
from src.MLProject.utils.common import read_yaml, create_directories
from box import ConfigBox

config = read_yaml("configs/config.yaml")
create_directories([config.artifacts_root])
```

- Use logger consistently:

```py
from src.MLProject.utils import logger
logger.info("starting data ingestion")
```

- Data ingestion pattern (see `research/data_ingestion.ipynb`): create a `DataIngestionConfig` dataclass and a class `DataIngestion` with `download_file()` and `extract_zip_file()` methods. Use `urllib.request.urlretrieve` and `zipfile.ZipFile`.

## Things to watch / gotchas

- Import casing: package directory is `MLProject` but some files import `mlProject` (lowercase). Normalize to `src.MLProject` imports to avoid runtime ImportError on case-sensitive systems.
- Several files (e.g., `app.py`, `src/MLProject/config/configuration.py`, `params.yaml`, `schema.yaml`) are empty or partially implemented. Prefer referencing `research/*.ipynb` implementations as source of truth when porting.
- Notebooks set the working directory explicitly. When running code from scripts, ensure working directory is repository root or use absolute/Path-based references.

## Where to look when uncertain

- `configs/config.yaml` — canonical paths & artifact layout.
- `research/data_ingestion.ipynb` — working reference implementations for configuration and ingestion flow.
- `src/MLProject/utils/common.py` and `src/MLProject/utils/__init__.py` — logging and I/O helpers.
- `setup.py` — packaging & `src` layout.

## If you need to modify the repo

- Keep edits small and local to the package under `src/MLProject/`.
- When adding runnable scripts, prefer adding CLI entrypoints under `src/MLProject/` or small top-level scripts (`main.py`) that import from `src.MLProject`.

---
If any section is unclear or you want more detail (examples of porting a notebook cell into `src/MLProject/config/configuration.py`, or a ready PR to implement `ConfigurationManager`), tell me which part to expand and I will iterate.
