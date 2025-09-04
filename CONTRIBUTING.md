[简体中文](./Document/CONTRIBUTING/zh_cn.md)
[繁体中文](./Document/CONTRIBUTING/zh_tw.md)
[日本語](./Document/CONTRIBUTING/jp.md)

# CONTRIBUTING

Thank you for your interest in contributing to Snake! This document provides guidelines and instructions to help you set up your development environment and start contributing.

## Development Setup

Before you start contributing to the project, you need to set up your development environment. Here are the steps you need to follow:

### Prerequisites


**Install Python**: Our project requires Python. Please follow the instructions provided [here](https://www.python.org/downloads/) to install it on your system.

### Setup for All Users



*   Make sure to add Python to your system's PATH. This option is usually available during the installation process, but you can verify and manually add it if necessary.

*   Ensure that pip (Python package installer) is installed, which typically comes bundled with Python.

### Clone the Repository

First, clone the project repository to your local machine:



```
git clone https://github.com/Personalizations/Snake.git

cd snake
```

### Install Dependencies

Install the required Python package using pip:



```
pip install -r requirements.txt
```

### Run the Application

To start the development version of the application, use the following command:



```
python main.py
```

## Contributing Your Changes

#### Before committing your changes

It's recommended to check code style and quality before committing:

### Code style formatting (if using tools like black):

```
black .
```

Once you have made your changes:



1.  Fork the repository.

2.  Create a new branch for your feature or bug fix.

3.  Commit your changes with clear and concise commit messages.

4.  Push your branch to your fork and submit a pull request to our repository.

We appreciate your contributions and look forward to your active participation in our project!