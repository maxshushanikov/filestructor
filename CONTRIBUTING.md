# Contributing to Filestructor

Thank you for your interest in contributing to Filestructor! We welcome contributions from the community to help improve the project. This guide will help you get started with contributing code, documentation, and bug reports.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Coding Guidelines](#coding-guidelines)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Feature Requests](#feature-requests)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs
This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find a solution.

### Suggesting Enhancements
This section guides you through submitting an enhancement suggestion, including the process for proposing new features.

### Your First Code Contribution
Unsure where to begin contributing? You can start with these beginner-friendly issues:
- [First Issues](https://github.com/yourusername/filestructor/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)

### Pull Requests
The process for submitting code changes is outlined below.

## Development Setup

1. **Fork the repository** on GitHub
   
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/filestructor.git
   cd filestructor
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -e .[dev]
   ```

5. **Verify installation**:
   ```bash
   filestructor --help
   ```

## Project Structure

```
filestructor/
├── app/
│   ├── __init__.py
│   ├── app.py          # CLI entry point
│   ├── builder.py      # Builds file system tree
│   ├── components.py   # File system components
│   ├── console.py      # Handles user input
│   ├── file_utils.py   # File operations utilities
│   └── visitors.py     # Report generation
├── tests/              # Test suite
├── .github/            # GitHub workflows and templates
├── docs/               # Documentation
├── pyproject.toml      # Project configuration
├── mkdocs.yml          # Documentation configuration
└── CONTRIBUTING.md     # This file
```

## Coding Guidelines

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use type hints for all function signatures
- Write docstrings in Google format
- Keep functions and methods focused and small
- Avoid global variables
- Write tests for all new functionality
- Add comments for complex logic

## Testing

Filestructor uses pytest for testing. Before submitting a pull request, ensure all tests pass:

```bash
pytest -v
```

To run tests with coverage:

```bash
pytest -v --cov=app --cov-report=html
```

Then open `htmlcov/index.html` in your browser to view the coverage report.

### Writing Tests

When adding new functionality, please include tests in the appropriate file in the `tests/` directory. Follow these guidelines:

- Use descriptive test names
- Keep tests isolated and independent
- Use pytest fixtures where appropriate
- Test edge cases and error conditions
- Ensure tests are deterministic

## Submitting Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes

3. Run tests to ensure everything works:
   ```bash
   pytest -v
   ```

4. Format your code using black:
   ```bash
   black .
   ```

5. Add and commit your changes:
   ```bash
   git add .
   git commit -m "Add your descriptive commit message"
   ```

6. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a build.
2. Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent.
4. You may merge the Pull Request in once you have the sign-off of at least one other developer, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

## Reporting Bugs

When reporting bugs, please include:

- Filestructor version
- Python version
- Operating system
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Any relevant error messages or stack traces

## Feature Requests

Before submitting a feature request, please check if the feature has already been requested. When creating a new feature request, please provide:

- A clear and descriptive title
- A detailed description of the feature
- The problem it solves
- Any alternatives you've considered
- Any additional context or screenshots

---

Thank you for contributing to Filestructor!