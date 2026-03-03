# M02 Sprint Project

> [!NOTE]
> You have 60 minutes to clean a catastrophic CSV into tidy format while maintaining granular Git history. Then present your approach and results to the class.
>

## The Challenge

We'll use synthetic datasets in `./data` folder. Your tasks are:

1. Create a figure showing the data in `./data/1d-data.csv`. This dataset consists of the effect of a treatment for 10 subjects. Make sure to label your axes and create a non-misleading data. You can choose any appropriate visualization method (e.g., line plot, bar plot, etc.).
2. Create a figure showing the data in `./data/2d-data.csv`. This dataset consists 2D measurements of samples. You may choose any appropriate visualization method (e.g., heatmap, contour plot, surface plot, etc.). Make sure to label your axes and create a non-misleading data.
3. Create a figure showing the data in `./data/1d-multi-method-data.csv`. This dataset consists of measurements (i.e., "AUC-ROC") of samples using multiple methods. Your goal is to highlight "Proposed" against "Baseline 1" and "Baseline 2", .... "Baseline 9" by using preattentive visual encoding. Make sure to (1) label your axes, (2) create a non-misleading visualizaation, and (3) highlight "Proposed" effectively.
4. Create a figure showing the UCI ML hand-written digits dataset in `./data/digits-data.csv` (also available via `sklearn.datasets.load_digits`). This dataset consists of 8×8 pixel images of handwritten digits (0–9) with 64 features per sample. Visualize the data in 2D (e.g., using t-SNE) to show the clustering structure. Color the data points by digit class to reveal the similarity and dissimilarity of digit distributions. No need to perform clustering — use the provided digit labels as class membership.

Make atomic commits for each step (you can make multiple commits per step, which is encouraged).

## Deliverables: Folder Structure and Filenames

Your repository must follow this folder structure:

```
.
├── data/               # Datasets (provided; do not modify)
│   ├── 1d-data.csv
│   ├── 2d-data.csv
│   ├── 1d-multi-method-data.csv
│   └── digits-data.csv          # UCI ML hand-written digits (generated via gen-digits-data.py)
├── docs/               # Documentation (your notes and write-ups)
│   ├── notes-1d-data.md
│   ├── notes-2d-data.md
│   ├── notes-1d-multi-method.md
│   └── notes-digits.md
├── figs/               # Figures (output from your visualizations)
│   ├── fig-1d-data.png
│   ├── fig-2d-data.png
│   ├── fig-1d-multi-method.png
│   └── fig-digits.png
├── workflow/           # Code (your scripts for data processing and visualization)
│   ├── ...             # Your Python scripts go here
│   └── ...
├── run.sh              # Automated pipeline script (see below)
├── pyproject.toml      # Project dependencies
└── README.md           # This file
```

### Required deliverables

| Deliverable | Location | Filename Convention |
|---|---|---|
| Notes for each dataset | `docs/` | `notes-1d-data.md`, `notes-2d-data.md`, `notes-1d-multi-method.md`, `notes-digits.md` |
| Figures for each dataset | `figs/` | `fig-1d-data.png`, `fig-2d-data.png`, `fig-1d-multi-method.png`, `fig-digits.png` |
| Visualization/processing scripts | `workflow/` | Your choice (e.g., `viz_1d_data.py`, `format_2d_data.py`) |
| Automated pipeline script | project root | `run.sh`, `Makefile`, or `Snakefile` (see [Automated Pipeline](#automated-pipeline)) |

## Use of AI

> [!IMPORTANT]
> Generative AI tools (e.g., ChatGPT, GitHub Copilot, Claude) are **allowed** for this sprint with the following restrictions:
>
> - **Agentic coding is NOT allowed.** You must not simply ask an AI agent to complete the tasks for you (e.g., prompting an agent to generate the entire solution end-to-end). The work must be *yours*.
> - **You may use AI to assist with writing code**, such as generating code snippets, debugging, or understanding library APIs. However, **you must understand all code you submit** and be able to explain it.
> - **Document your AI usage in your notes.** In each `docs/notes-*.md` file, describe the process you followed, including where and how you used AI. For example: "I used ChatGPT to help me choose between a violin plot and a box plot" or "I used Copilot to generate the initial matplotlib boilerplate."
> - **Your documentation must reflect your own understanding.** AI-generated text is acceptable as a starting point, but your notes must demonstrate that *you* understand the data, your design decisions, and the code.

## Automated Pipeline

You must provide a script that reproduces all figures from scratch. This script should:

1. Install dependencies (or document how to install them)
2. Run all data processing and visualization scripts in `workflow/`
3. Save the resulting figures to `figs/`

You may use one of the following formats:

- **`run.sh`** (recommended for simplicity): A shell script at the project root.
  ```bash
  #!/bin/bash
  # Example run.sh
  uv run python workflow/viz_1d_data.py
  uv run python workflow/viz_2d_data.py
  uv run python workflow/viz_1d_multi_method.py
  uv run python workflow/viz_digits.py
  ```
- **`Makefile`**: A Makefile at the project root with a default target that builds all figures.
- **`Snakefile`**: A Snakemake workflow file at the project root.

The evaluator will run your pipeline script on a different machine to test reproducibility. Make sure it works without manual intervention.

## Git Branching Workflow

You must use git branches to organize your work. Each dataset requires three sequential branches:

### Branch Structure

For each dataset (1d-data, 2d-data, 1d-multi-method, digits), create three branches:

**Branch 1: `<dataset>-notes`**
- Document your understanding of the dataset
- Create a notes file in `docs/` (e.g., `docs/notes-1d-data.md`) describing the data structure, key observations, and visualization strategy
- Commit and push the notes file

**Branch 2: `<dataset>-format`**
- Load and inspect the data
- Clean or transform the data if needed
- Save formatted data or create data loading functions in `workflow/`
- Commit each formatting decision separately
- Push your work

**Branch 3: `<dataset>-viz`**
- Create the visualization code in `workflow/`
- Generate the final figure
- Save figure to `figs/` (e.g., `figs/fig-1d-data.png`)
- Commit visualization code and output
- Push your work

You should create and merge these twelve branches:

1. `1d-data-notes`, `1d-data-format`, `1d-data-viz`
2. `2d-data-notes`, `2d-data-format`, `2d-data-viz`
3. `1d-multi-method-notes`, `1d-multi-method-format`, `1d-multi-method-viz`
4. `digits-notes`, `digits-format`, `digits-viz`

## The Rules

- **Time:** 60 minutes of work, followed by presentations.
- **Version Control:** Every change must be committed and pushed. No batch commits. Your commit messages must explain why you made each change.
- **Branching:** You must follow the branching workflow described above. Each dataset requires three branches (notes, format, viz). Merge each branch to master before starting the next.
- **Requirements:** Visualizations must be clear and non-misleading. Notes files must document your thinking. Code must be well-organized.
- **AI:** Generative AI is allowed for assistance but agentic coding is not. You must understand all code you submit. See [Use of AI](#use-of-ai).

## Evaluation

| Criteria | Level 3 (5–6 pt) | Level 2 (1–4 pt) | Level 1 (0 pt) | Score |
|---|---|---|---|---|
| Task Outcome | Fully addresses the task; works as intended | Solve the core task with minor gaps | Solution missing or fundamentally broken | / 6 |
| Documentation | Clear explanation of approach, decisions, and AI usage. Notes files in `docs/` are complete. | Explains approach; some gaps in reasoning or steps. | Absent or unreadable | / 6 |
| Git Log | Regular commits with descriptive messages showing progression | Multiple commits; some evidence of iterative work | Single commit or no meaningful history | / 6 |
| Reproducibility | Provided a pipeline script (`run.sh`, `Makefile`, or `Snakefile`) that reproduces all figures, along with environment setup instructions. The script works on a different machine. | The script is missing/broken or setup instructions are incomplete, but only minor fixes are needed to make it work. | Reproducing results requires manual steps. Instructions are insufficient for reproducibility. | / 6 |
| Submission Format | Deliverables are correctly named and placed in the specified folders (`docs/`, `figs/`, `workflow/`). | Some deliverables are misnamed or misplaced. | Does not follow specified format. | / 6 |

## Submission

Submit the link to your GitHub repository to Brightspace.

## Set up

Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

Open `pyproject.toml` in a text editor and change the project name and add your project dependencies.

If you want to install a Python package, run:

```bash
uv add <package-name>
```

If you need to install non-Python dependencies, you can use conda or mamba as described below.

#### Miniforge

Install miniforge [GitHub - conda-forge/miniforge: A conda-forge distribution.](https://github.com/conda-forge/miniforge).

First create a virtual environment for the project.

    mamba create -n project_env_name python=3.7
    mamba activate project_env_name

Install `ipykernel` for Jupyter.

    mamba install -y -c bioconda -c conda-forge ipykernel numpy pandas scipy matplotlib seaborn tqdm

Create a kernel for the virtual environment that you can use in Jupyter lab/notebook.

    python -m ipykernel install --user --name project_env_kernel_name

## Kickstarter code

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the data
data_table = pd.read_csv('./data/data.csv')

# Your code here
```


