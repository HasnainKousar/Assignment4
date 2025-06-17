# Professional-grade calculator with Advance Testing
## Project Overview

Welcome to the Module 4 assignment, where we create a modular, extensible calculator application written in Python.  
This project demonstrates object-oriented design, test-driven development, and robust error handling for basic arithmetic operations.

## Object-Oriented Programming and Advanced Testing

For this project we used Object-Oriented Programming (OOP) principles to first create the Operation class, then we used the factory method to create the Calculation module using OOP.

We also used automated testing to ensure our code's correctness and reliability. 

- **Abstraction:** 
  Created an abstract base class `Calculation` which defines the interface for all calculation types and requires subclasses to implement the `excute` method.

- **Encapsulation:**  
  Each calculation type (addition, subtraction, multiply and divide) was represented as a class that encapsulates its operands and logic.

- **Inheritance:**  
  Concrete classes like `AddCalculator` and `SubtractCalculator` inherit from `Calculation`, and shares a common interface and structure

- **Polymorphism:**  
  The `CalculatorFactory` creates calculation objects based on the operation type. We can call `excute` on any calculation object, and the correct logic is executed.

- **Extensibility:**  
  We can makes changes to the app without modifying the existing code/structure. New operations can be added by creating new subclasses and registering them with the factory.


- **Unit Testing:**
  Each function and class method is tested in isolation to verify that it behaves as expected for various inputs, including edge cases and error conditions

- **Test Framework:**
  We used the [pytest](https://pytest.org/) framework to write and run tests.

- **Mocking:**
  Used `unittest.mock.patch` decorator to mock dependencies

- **Parameterized Testing:**  
  Pytest’s `@pytest.mark.parametrize` was used to run the same test logic with multiple sets of inputs and expected outputs, improving coverage and reducing code duplication.

- **Error Handling Tests:**  
  Tests were written to ensure that the application correctly handles invalid input, division by zero, unsupported operations, and other error scenarios.

## Features

- Supports addition, subtraction, multiplication, and division
- Easily extensible to support more operations (e.g., power)
- Command-line interface for user interaction
- Calculation history display
- Comprehensive unit tests with pytest

## Project Structure

```
module4/assingment4/
├── .github/
│   └── workflows/
│       └── tests.yml
├── app/
│   ├── calculation/
│   │   └── __init__.py
│   ├── operations/
│   │   └── __init__.py
│   ├── calculator.py
│   └── __init__.py
├── tests/
│   ├── test_calculation.py
│   ├── test_calculator.py
│   └── test_operations.py
├── main.py
├── README.md
```
## Extending the Calculator

To add a new operation:
1. Implement the operation in `app/operations/__init__.py`.
2. Create a new Calculator class in `app/calculation/__init__.py` and register it with `CalculatorFactory`.

## License

This project is licensed under the MIT License.

---

*Created for educational purposes.*

## Setup
- WSL (Windows Subsystem for Linux): developed by Microsoft to enable users to run a Linux enviroment directly on Windows machine. 
- Git: open-source distributed version control system that enables developers to track changes in the source code. 
- VSCode (Visual Studio Code): use to set up python virtual enviroment, and isolating project dependencies
- Python: main programming language for the calculator and tests
- pytest: for advanced testing of the code
- Homebrew(for mac users): for installing packages on macOS

## Setup Instruction

# 🧩 1. Install Homebrew (Mac Only)

> Skip this step if you're on Windows.

Homebrew is a package manager for macOS.  
You’ll use it to easily install Git, Python, Docker, etc.

**Install Homebrew:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Verify Homebrew:**

```bash
brew --version
```

If you see a version number, you're good to go.

---

## WSL:
On powershell and type the following command to see a list of valid distributions that can be installed.

```bash
wsl --list --online
```
From the list install Ubuntu using the following command:

```bash
wsl --install -d Ubuntu-24.04
```
After it's installed, create a new UNIX username and set password (make sure you remember the password, as there is no way to get it back)

# 🧩 2. Install and Configure Git

## Install Git

- **MacOS (using Homebrew)**

```bash
brew install git
```

- **Windows**

Download and install [Git for Windows](https://git-scm.com/download/win).  
Accept the default options during installation.

**Verify Git:**

```bash
git --version
```

---

## Configure Git Globals

Set your name and email so Git tracks your commits properly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Confirm the settings:

```bash
git config --list
```

---

## Generate SSH Keys and Connect to GitHub

> Only do this once per machine.

1. Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

(Press Enter at all prompts.)

2. Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

3. Add the SSH private key to the agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

4. Copy your SSH public key:

- **Mac/Linux:**

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

- **Windows (Git Bash):**

```bash
cat ~/.ssh/id_ed25519.pub | clip
```

5. Add the key to your GitHub account:
   - Go to [GitHub SSH Settings](https://github.com/settings/keys)
   - Click **New SSH Key**, paste the key, save.

6. Test the connection:

```bash
ssh -T git@github.com
```

You should see a success message.

---

# 🧩 3. Clone the Repository

Now you can safely clone the course project:

```bash
git clone <repository-url>
cd <repository-directory>
```

---

# 🛠️ 4. Install Python 3.10+

## Install Python

- **MacOS (Homebrew)**

```bash
brew install python
```

- **Windows**

Download and install [Python for Windows](https://www.python.org/downloads/).  
✅ Make sure you **check the box** `Add Python to PATH` during setup.

**Verify Python:**

```bash
python3 --version
```
or
```bash
python --version
```

---

## Create and Activate a Virtual Environment

(Optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🐳 5. (Optional) Docker Setup

> Skip if Docker isn't used in this module.

## Install Docker

- [Install Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
- [Install Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)

## Build Docker Image

```bash
docker build -t <image-name> .
```

## Run Docker Container

```bash
docker run -it --rm <image-name>
```

---

# 🚀 6. Running the Project

- **Without Docker**:

```bash
python main.py
```

(or update this if the main script is different.)

- **With Docker**:

```bash
docker run -it --rm <image-name>
```

---

# 📝 7. Submission Instructions

After finishing your work:

```bash
git add .
git commit -m "Complete Module X"
git push origin main
```

Then submit the GitHub repository link as instructed.

---

# 🔥 Useful Commands Cheat Sheet

| Action                         | Command                                          |
| ------------------------------- | ------------------------------------------------ |
| Install Homebrew (Mac)          | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| Install Git                     | `brew install git` or Git for Windows installer |
| Configure Git Global Username  | `git config --global user.name "Your Name"`      |
| Configure Git Global Email     | `git config --global user.email "you@example.com"` |
| Clone Repository                | `git clone <repo-url>`                          |
| Create Virtual Environment     | `python3 -m venv venv`                           |
| Activate Virtual Environment   | `source venv/bin/activate` / `venv\Scripts\activate.bat` |
| Install Python Packages        | `pip install -r requirements.txt`               |
| Build Docker Image              | `docker build -t <image-name> .`                |
| Run Docker Container            | `docker run -it --rm <image-name>`               |
| Push Code to GitHub             | `git add . && git commit -m "message" && git push` |

---

# 📋 Notes

- Install **Homebrew** first on Mac.
- Install and configure **Git** and **SSH** before cloning.
- Use **Python 3.10+** and **virtual environments** for Python projects.
- **Docker** is optional depending on the project.

---

# 📎 Quick Links

- [Homebrew](https://brew.sh/)
- [Git Downloads](https://git-scm.com/downloads)
- [Python Downloads](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [GitHub SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)



