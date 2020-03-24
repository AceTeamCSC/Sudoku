# Sudoku
> Short blurb about what your product does.

Add an image
One to two paragraph statement about your product and what it does.

## Installation

work in progress

Windows:

```sh
edit autoexec.bat
```

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially
more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Instructions are tested on Python 3.7.6

### Set Up a Working Environment
1. Download [git](https://git-scm.com/downloads) and optionally [github](https://desktop.github.com/)
2. Install [Python 3.7.6](https://www.python.org/downloads/release/python-376/)
3. [Fork](https://github.com/AceTeamCSC/sudoku/fork) it
4. Clone the fork (`clone https://github.com/<your github id>/sudoku.git`) to your computer
5. Create a virtual environment and activate [it](https://docs.python.org/3.7/library/venv.html#creating-virtual-environments).
This will create a directory that contains a Python installation and tells the interpreter to use it. Now the packages
installed for this project will not create havoc on your system’s default Python installation. Many of this project's
config files assume the virtual environment is named 've'.
    1. On windows:
        1. Right click on the PowerShell application and select Run as Administrator
        2. Run the following command: ```Set-ExecutionPolicy Unrestricted```
        3. ```python -m venv ve```
        4. ```cd .\Scripts\```
        5. `````.\Activate.ps1`````
    2. On Mac:
        1. ```python3 -m venv ve```
        2. ```source ve/bin/activate```
6. Inside the /sudoku directory cloned from Github
```pip install -r requirements.txt``` to install all the packages required for development on this project

## Continuous Integration
This Sudoku project utilizes [continuous integration](https://hackaday.com/2020/01/06/continuous-integration-what-it-is-and-why-you-need-it/)
for collaboration.

   ![continuous integration](https://dan.yeaw.me/images/continuous-integration.svg)

### Before the Pull Request
1. Run ```pytest``` in the /sudoku directory
    1. A unit test is designed to check a single function or unit of code. The code for the unit tests
    is in /tests and the examples will be using [PyTest](https://docs.pytest.org/en/latest/getting-started.html). A standard
    practice that goes with testing is calculating code coverage. Code coverage is the percentage of source code that is
    “covered” by your tests. If the code coverage falls below 70%, the Github check will fail. Before doing a pull request, the
    coverage can be checked by running pytest.

     Example successful run from command line on your local machine:
      ```
    $ coverage run -m pytest --verbose
    ================================================================================ test session starts =================================================================================
    platform darwin -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/paigelo/Desktop/sudoku/ve/bin/python3
    cachedir: .pytest_cache
    rootdir: /Users/paigelo/Desktop/sudoku, inifile: setup.cfg, testpaths: tests
    plugins: mock-2.0.0, black-0.3.8, flake8-1.0.4, xdoctest-0.11.0
    collected 1 item

    tests/test_sudoku.py::test_foo PASSED                                                                                                                                          [100%]

    ================================================================================= 1 passed in 0.03s ==================================================================================
    ```

    Example Unsuccessful Github run as seen in the 'checks' tab:
   ```
     Test with pytest2s
    ##[error]Process completed with exit code 1.
    Run pytest --verbose --cov-branch --cov-fail-under=90 --color=yes --cov=sudoku
    ============================= test session starts =============================
    platform win32 -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- c:\hostedtoolcache\windows\python\3.7.6\x64\python.exe
    cachedir: .pytest_cache
    rootdir: D:\a\sudoku\sudoku, inifile: setup.cfg, testpaths: tests
    plugins: black-0.3.8, cov-2.8.1, flake8-1.0.4, mock-2.0.0, xdoctest-0.11.0
    collecting ... collected 1 item

    tests/test_sudoku.py::test_foo PASSED                                    [100%]

    ----------- coverage: platform win32, python 3.7.6-final-0 -----------
    Name               Stmts   Miss Branch BrPart  Cover   Missing
    --------------------------------------------------------------
    sudoku\sudoku.py       5      1      2      1    71%   45, 44->45

    FAIL Required test coverage of 90% not reached. Total coverage: 71.43%

    ============================== 1 passed in 0.05s ==============================
    ##[error]Process completed with exit code 1.
    ```


2. ```pre-commit run --all-files``` in the /sudoku directory
    1. pre-commit is a Python package that allows you to create a .pre-commit-config.yaml file that maintains a list of
    tools to run before each commit. Note: pre-commit requires git.
    2. The pre-commit config file also has a linter, flake8, to analyze code for potential errors and standard Python
    coding style practices. There are some hooks in .pre-commit-config file, that will make file changes for you. If it makes changes,
    the status will say Failed, but if you run it again it'll show Passed since the violations were corrected in the
    previous run.

    Example unsuccessful run from command line on a local machine:
    ```
    $ pre-commit run --all-files
    seed isort known_third_party.............................................Passed
    black....................................................................Passed
    Flake8...................................................................Passed
    Trim Trailing Whitespace.................................................Failed
    - hook id: trailing-whitespace
    - exit code: 1
    - files were modified by this hook

    Fixing README.md

    Fix End of Files.........................................................Passed
    Debug Statements (Python)................................................Passed
    Check docstring is first.................................................Passed
    Fix requirements.txt.....................................................Passed
    Check Yaml...............................................................Passed
    autopep8.................................................................Passed
    blacken-docs.............................................................Passed

    ```

    Example successful run from command line on your local machine:
    The whitespace issues were fixed when running the initial pre-commit coommand and are therefore no longer showing
    as failed in the second run of pre-commit:
    ```
    $ pre-commit run --all-files
    seed isort known_third_party.............................................Passed
    black....................................................................Passed
    Flake8...................................................................Passed
    Trim Trailing Whitespace.................................................Passed
    Fix End of Files.........................................................Passed
    Debug Statements (Python)................................................Passed
    Check docstring is first.................................................Passed
    Fix requirements.txt.....................................................Passed
    Check Yaml...............................................................Passed
    autopep8.................................................................Passed
    blacken-docs.............................................................Passed
    ```

   Example Unsuccessful Github run as seen in the Github 'checks' tab:
    ```
   pre-commit53s
    [INFO] This may take a few minutes...
    Run pre-commit/action@v1.0.1
    install pre-commit
    C:\hostedtoolcache\windows\Python\3.7.6\x64\Scripts\pre-commit.exe run --all-files --show-diff-on-failure --color=always
    [INFO] Initializing environment for https://github.com/asottile/seed-isort-config.
    [INFO] Initializing environment for https://github.com/ambv/black.
    [INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
    [INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks:darglint,flake8-docstrings.
    [INFO] Initializing environment for https://github.com/pre-commit/mirrors-autopep8.
    [INFO] Initializing environment for https://github.com/asottile/blacken-docs.
    [INFO] Initializing environment for https://github.com/asottile/blacken-docs:black==19.3b0.
    [INFO] Installing environment for https://github.com/asottile/seed-isort-config.
    [INFO] Once installed this environment will be reused.
    [INFO] This may take a few minutes...
    [INFO] Installing environment for https://github.com/ambv/black.
    [INFO] Once installed this environment will be reused.
    [INFO] This may take a few minutes...
    [INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
    [INFO] Once installed this environment will be reused.
    [INFO] This may take a few minutes...
    [INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
    [INFO] Once installed this environment will be reused.
    [INFO] This may take a few minutes...
    [INFO] Installing environment for https://github.com/pre-commit/mirrors-autopep8.
    [INFO] Once installed this environment will be reused.
    [INFO] This may take a few minutes...
    [INFO] Installing environment for https://github.com/asottile/blacken-docs.
    [INFO] Once installed this environment will be reused.
    [INFO] This may take a few minutes...
    ```

## Release History

* 0.1.0
    * CHANGE: coming soon
* 0.1.0
    * CHANGE: coming soon
* 0.0.1
    * Work in progress

## Meta

AceTeam

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/AceTeamCSC/sudoku](https://github.com/AceTeamCSC/sudoku)

## Contributing

If you're unfamiliar with Git, you may find [this](https://realpython.com/python-git-github-intro/) information useful

1. Create your feature branch (`git checkout -b feature/fooBar`)
2. Commit your changes (`git commit -am 'Add some fooBar'`)
3. Push to the branch (`git push origin feature/fooBar`)
4. Create a new [Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
6. Once a Pull Request is initiated, Github Actions will run tests. This is part of continuous integration. To view
the status of the tests:
    1. Go to [actions](https://github.com/AceTeamCSC/sudoku/actions)
    2. then click the first event to see the newest run
    3. Then, in the left corner, click build to get details.

    ![actions](docs/actions.png)



## Documentation
We can take advantage of the [docstrings](https://www.python.org/dev/peps/pep-0257/) we've been writing in the code to
automate the documentation using [Sphinx](https://www.sphinx-doc.org/en/1.5/tutorial.html#running-the-build).
There's also built-in [testing](https://docs.python.org/3.7/library/doctest.html) to make sure the docstrings match the
code. The documentation in our code can be compiled into a PDF by running ```make latexpdf```. Note you need to have latex on
your machine.
## Managing releases
Github [tags](https://help.github.com/en/github/administering-a-repository/managing-releases-in-a-repository)
