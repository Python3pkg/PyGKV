# PyGKV

Python library for Git as a Key-Value store  

## 1. Dependencies
  * None  

## 2. Support  
Currently the package supports the following python versions:
  * Python 2.7.10
  * Python 3.4.3
  * PyPy3
  * Pyston
  * Jython
  * IronPython  

## 3. Usage
  * The current API is quiet simple, clone this repo with  
  
  ```bash
    $ git clone git@github.com:ishankhare07/PyGKV.git
  ```
  
  * Run python  
  ```bash
    $ cd PyGKV/
    $ python3
  ```
  ```python
    >>> import GitDatabase
    >>> db = GitDatabase.Database()
    >>> db["name"] = "Guido Van Rossum"
    >>> db["name"]
    "Guido Van Rossum"
  ```
