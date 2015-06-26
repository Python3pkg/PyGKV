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
  * The current API is quiet simple, install using pip  
  
  ```bash
  $ pip install pygkv
  ```
  
  * Run python  
  ```bash
 $ python3
  ```
  * Import the Library

  ``` python
  >>> from pygkv import GitDatabase
  >>> db = GitDatabase.Database()
  >>> db["name"] = "Guido Van Rossum"
  >>> db["name"]
  Guido Van Rossum
  ```
