<!--
* KINOVA (R) KORTEX (TM)
*
* Copyright (c) 2018 Kinova inc. All rights reserved.
*
* This software may be modified and distributed
* under the terms of the BSD 3-Clause license.
*
* Refer to the LICENSE file for details.
*
-->

<a id="markdown-description" name="description"></a>
# Description

Here is some information to help you start with python. This information will help new python users.


<h1>Table of Contents </h1>

<!-- TOC -->
- [Description](#description)
- [Python setup](#python-setup)
    - [Installation of Python & Python modules](#installation-of-basic-python--python-modules)
        - [Required installations](#mandatory-installations)
        - [Optional Python modules](#facultative-usefull-python-modules)
- [Python overview](#python-overview)

<!-- /TOC -->

<a id="markdown-python-setup" name="python-setup"></a>
# Python setup

<a id="markdown-installation-of-basic-python--python-modules" name="installation-of-basic-python--python-modules"></a>
## Installation of Python & Python modules

<a id="markdown-mandatory-installations" name="mandatory-installations"></a>
### Required installations
- python >= 3.9
- pip

 <details open>
 <summary>Linux (Ubuntu)</summary>

 <h4>Install Python 3.9</h4>  

 ```sh
 sudo apt-get install python3.9
 ```


 <h4>Install Pip</h4>  
 ```sh
 sudo apt-get install python3-pip  
 python3.9 -m pip install --upgrade pip --user
 ```

</details>  

<p></p>

<details open>
<summary>Windows</summary>
<h4>Download Python 3.9 (based on 3.9.13)</h4>

- [python-3.9.13](https://www.python.org/downloads/release/python-3913/)  
- alternatively, click this link to download the file directly: [https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe)  

 <h4>Installation using the wizard</h4>  

 - be sure to install pip and to add Python to the environnement variables  
 - you should also consider installing the Python test suite  

</details>  

<a id="markdown-facultative-usefull-python-modules" name="facultative-usefull-python-modules"></a>
### Optional Python modules
- `pipenv`: packages manager
- `pytest`: Python test framework
- `pytest-cov`: pytest coverage tool report
- `pylint`: Python lint (static analyser for editor)

<a id="markdown-python-overview" name="python-overview"></a>
# Python overview

<details open>
<summary>Linux (Ubuntu)</summary>

```sh
# to display the actual version of Python used
python -V
 
# if there are several versions installed you need to specify the version  
python3 -V
python3.9 -V

# use Python pip module to install and manage Python modules
python3.9 -m pip --help

# use Python to run a specific Python script
python3.9 <script>
```

</details>  

<details open>
<summary>Windows</summary>

```sh
# to get the actual version of Python used by Windows
python -V

# to use another version call Python with full path instead of the shortcut alias (see following example)
C:\User\user_name\AppData\Local\Programs\Python\python35-32.exe

# Python pip module
python -m pip --help

# use Python to run a specific Python script
python <script>
```
_________________________
<a id="markdown-back-to-root-topic-readmemdreadmemd" name="back-to-root-topic-readmemdreadmemd"></a>
## Back to root topic: **[readme.md](../readme.md)**  
