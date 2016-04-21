# Insert Filepath
Quickly insert relative filepath from current folder into file.


# Installing

**With Package Control plugin**

The easiest way to install Inert Filepath is through [Package Control](https://sublime.wbond.net/installation).

Once Package Control is installed bring up Command Palette (``Command+Shift+P`` on OS X, ``Control+Shift+P`` on Linux/Windows). Select "Package Control: Install Package" and search for "Insert Filepath". When the plugin is installed, Package Control will automatically keep it up to date.

**Without Package Control plugin**

Clone or copy the files into the Sublime Text Packages directory. The packages directory is located differently in different platforms. To access the directory use:

* OS X: ```Sublime Text -> Preferences -> Browse Packages...```
* Linux: ```Preferences -> Browse Packages...```
* Windows: ```Preferences -> Browse Packages...```


# Using

**Command Palette**

Bring up Command Palette (``Command+Shift+P`` on OS X, ``Control+Shift+P`` on Linux/Windows) and select "Insert Filepath". This will bring up a quick select dialog with all the files located in the open folder. Search for and select your file to insert it.

**Keyboard Shortcut**

* OS X: ```option+super+1```
* Linux: ```alt+super+i```
* Windows: ```alt+super+i```


# Configuring

You can set your own configuration file for the plugin. Edit the user configuration file to overwrite default config. To access the file use:

* OS X: ```Sublime Text -> Preferences -> Package Settings -> Insert Filepath -> Settings - User```
* Linux: ```Preferences -> Package Settings -> Insert Filepath -> Settings - User```
* Windows: ```Preferences -> Package Settings -> Insert Filepath -> Settings - User```

Original configuration:

	{
		"exclude_git_folder": true,
		"exclude_hidden_files": true,
		"exclude_hidden_folders": true
	}


# License

The MIT License (MIT)

Copyright (c) 2014 Magnus Hauge Bakke (mhbakke@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.