# The SetlX-Helper for Sublime Text 3
*"Wait, why should I use this?"* Good question! Lets ask the official [SetlX-Tutorial](http://randoom.org/?id=setlXdoc)<sup>as I recall it</sup>:

> 2. Programming [with the SetlX-Helper] is the only way to guarantee redemption from the eternal hell fire that awaits those [...] programming in SetlX.
> 3. Programming in SetlX [will then be] fun!



## Installing It
1. [Download](https://www.sublimetext.com/3) and install Sublime Text 3
2. Install Package Control in Sublime Text as described [here](https://packagecontrol.io/installation) and restart Sublime Text
3. Open the Command Palette by pressing <kbd>Ctrl</kbd>/<kbd>Super</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>, type in `install`, select `Package Control: Install Package` with <kbd>Enter</kbd>, wait for the list to load, type in `setlx` and select `SetlX Helper` from the list with <kbd>Enter</kbd>
4. You are all set, just open a SetlX-programm file and enjoy the new help!



## Using the Features
#### Syntax Definitions
Just type code ;)
![Syntax Definitions](screenshots/readme_syntax.PNG)
*Keep in mind: The colors don't come from the Helper-Plugin. You can choose your own in the* Preferences *- menu under the* Color Scheme *- sub-entry.*



## Features to Come Soon / ToDo
| Version |                      Feature                      |                                                                             optional Description                                                                             |
|---------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0.2.0   | command to open the Quickreference in the browser |                                                                                                                                                                              |
| 0.3.0   | snippets                                          | for faster developing by automatically completing standard-structures like for-loops/set-definitions/etc.                                                                    |
| 0.4.0   | build-system + error-parsing                      | start your program right from within Sublime Text, see the successful output and get the parsed errors directly pinned to the troubled position in your program              |
| 0.5.0   | real-time basic mistake warning                   | marks common (dumb) mistakes (like forgetting a semicolon/a closing bracket, using commas in a vector-definition, etc.) with a warning in real-time in your file as you type |


*Feel free to suggest additional features with a new GitHub-Issue.*