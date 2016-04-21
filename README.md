# Drafts
Quickly draft a new text an do something with the draft afterwards. Inspired by [Drafts](http://agiletortoise.com/drafts/) for iOS.

This is my first Sublime Plugin. I'm not a programmer, but a writer who wants to adjust his writing environment. I've probably did a lot of mistakes in the source code. Feel free to comment and change it, if you know better.


# Installing

**With Package Control plugin**

The easiest way to install Drafts is through [Package Control](https://sublime.wbond.net/installation).

Once Package Control is installed bring up Command Palette (``Command+Shift+P`` on OS X, ``Control+Shift+P`` on Linux/Windows). Select "Package Control: Install Package" and search for Drafts.

**Without Package Control plugin**

Clone or copy the files into the Sublime Text Packages directory. The packages directory is located differently in different platforms. To access the directory use:

* OS X: ```Sublime Text -> Preferences -> Browse Packages...```
* Linux: ```Preferences -> Browse Packages...```
* Windows: ```Preferences -> Browse Packages...```


# Using

**Command Palette**

Bring up Command Palette (``Command+Shift+P`` on OS X, ``Control+Shift+P`` on Linux/Windows) and select Drafts.

**Keyboard Shortcut**

* OS X: ```option+super+d```
* Linux: ```alt+ctrl+d```
* Windows: ```alt+ctrl+d```


# Configuring

You need to set your own configuration file for the plugin. Edit the user configuration file to overwrite default config. To access the file use:

* OS X: ```Sublime Text -> Preferences -> Package Settings - Drafts.
* Linux: ```Preferences -> Package Settings - Drafts.
* Windows: ```Preferences -> Package Settings - Drafts.

Original configuration:

	{   // Configure the user actions for your Drafts 
    "prompt_config": [
        { "name": "New Journal Entry",  // Description in the Prompt
          "action": "prepend", // Possible actions: "prepend" to given file, "append" to file 
          "file": "/Journal/Journal.md", // Path to file to append/prepend the draft
          // The file will be created if it doesn't exists. It opens, so that you can inspect 
          // the changes, but you must save it afterwards.
          "content": "## [[date|%Y-%m-%d %H:%M, %A]]\n[[draft]]\n\n" // Content of the draft
          // [[draft]] will be replaced by the whole text in your current draft
          // [[date]] will be replaced by the date in the default format: %Y-%m-%d %H:%M,
          // You can give another srftime compatible format with [[date|your format]]
        },
        { "name": "New Textidea",
          "action": "prepend",
          "file": "/Texts/Textsideas.md",
          "content": "## [[date|%Y-%m-%d %H:%M]]\n[[draft]]\n\n"
        },
        { "name": "New Book",
          "action": "append",
          "file": "/Todo/Lists/Books.taskpaper",
          "content": "- [[draft]] ([[date]])\n"
        },
        { "name": "New Website",
          "action": "append",
          "file": "/Todo/Lists/Web.taskpaper",
          "content": "- [[draft]] ([[date]])\n"
        },
    ]}


# License
The MIT License (MIT)

Copyright (c) 2016 Ronny Klein (ronny.klein@outlook.de)

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
