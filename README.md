# Structorex

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Structorex** is a command-line tool that generates a detailed report of your project's file structure, including file contents. It provides a visual representation of your directory hierarchy and allows you to inspect file contents directly in the generated report.

## Features

- 🌳 Visual representation of directory structure
- 📄 File content inspection in the report
- 🔍 Automatic file type detection (images, audio, video, documents)
- 🗑️ Exclude specific directories (`.git`, `__pycache__`, etc.)
- 📏 File size limitation (skips large files)
- 🧪 Comprehensive test suite

## Installation

```bash
pip install structorex
```

Or install from source:

```bash
git clone https://github.com/structorex/structorex.git
cd structorex
pip install -e .
```

## Usage

### Command Line Interface

```bash
structorex
```

The tool will prompt you for:
1. Directory path to analyze
2. Output filename (default: `project_report.txt`)

### Example Output

```
PROJECT STRUCTURE:
└── my_project/
    ├── src/
    │   ├── __init__.py
    │   ├── main.py
    │   └── utils.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_utils.py
    ├── .gitignore
    └── README.md

FILE CONTENTS:
==================================================
File: /path/to/my_project/src/main.py
==================================================
def main():
    print("Hello, Structorex!")

if __name__ == "__main__":
    main()
```

## Advanced Configuration

You can customize which directories to exclude by modifying the `excluded` set in the code:

```python
excluded = {
    '.git', '__pycache__', '.idea', 'venv', '.venv',
    'node_modules', '.vscode'
}
```

## Running Tests

```bash
pip install -e .[dev]
pytest -v
```

## Project Structure

```
structorex/
├── app/
│   ├── __init__.py
│   ├── app.py          # CLI entry point
│   ├── builder.py      # Builds file system tree
│   ├── components.py   # File system components
│   ├── console.py      # Handles user input
│   ├── file_utils.py   # File operations utilities
│   └── visitors.py     # Report generation
├── tests/              # Test suite
├── pyproject.toml      # Project configuration
└── .gitignore
```

## Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.