# Getting Started with marimo and Polars

This repository contains the materials for the hands-on workshop on using Polars within a marimo notebook.

## Getting Started

To get started with the hands-on exercises, follow these four steps.

### 1. Get the Project Files

You can either clone the repository using git or download it as a ZIP file.

**Option A: Clone the repository (recommended)**
```bash
git clone https://github.com/wanyek/getting-started-with-marimo-and-polars.git
cd getting-started-with-marimo-and-polars
```

**Option B: Download the ZIP file**
Download the ZIP from the repository page (`Code` -> `Download ZIP`), extract it, and navigate into the main project folder using your terminal.

### 2. Install uv

This project uses `uv`, a fast Python package manager from Astral. To install it as a standalone tool, run the appropriate command for your operating system in your terminal.

**On macOS and Linux (Zsh, Bash, etc.):**
The following command works for most shells, including Zsh.
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows (PowerShell):**
```bash
irm https://astral.sh/uv/install.ps1 | iwr -useb
```
After installation, the script will provide instructions to add `uv` to your system's PATH. For Zsh users, this typically involves adding a line to your `~/.zshrc` file.

### 3. Set Up the Environment and Install Packages

From the root directory of this project, run the following command. `uv` will automatically create a virtual environment and install all the packages listed in `pyproject.toml`.
```bash
uv sync
```

### 4. Run the marimo Notebook

Once the dependencies are installed, you can run the notebook in edit mode.
```bash
uv run marimo edit practice.py 
```

This will start the marimo server and open the notebook in your web browser. You are now ready to begin the workshop.
