# The SetlX-Helper for Sublime Text 3
*"Wait, why should I use this?"* Good question! Lets ask the official [SetlX-Tutorial](http://randoom.org/?id=setlXdoc)<sup>as I recall it</sup>:

> 2. Programming [with the] SetlX[-Helper] is the only way to guarantee redemption from the eternal hell fire that awaits those [...] programming in SetlX.
> 3. Programming in SetlX [will then be] fun!

I'm fairly sure you are convinced now ;)



## Installing It
#### Sublime Text 3 / 2
1. [Download](https://www.sublimetext.com/3) and install Sublime Text 3
2. Install Package Control in Sublime Text as described [here](https://packagecontrol.io/installation) and restart Sublime Text
3. Open the Command Palette (by pressing <kbd>Ctrl</kbd>/<kbd>Super</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>), select `Package Control: Install Package`, wait for the list to load and select `SetlX Helper` from the list
4. After the installation is done (the progress is shown in the lower left corner) you are all set. Just open a SetlX-program file and enjoy the new help!
5. *optional* I recommend using the *Monokai Extended* Color Scheme for a nice and colorful syntax-highlighting.



## Using the Features
#### Syntax Definitions
Just type code ;)
![Illustration of the Syntax Definitions](screenshots/readme_syntax.PNG)
*Keep in mind: The colors don't come from the Helper-Plugin. You can choose them as you like by selecting a Color Scheme you like from the* Preferences *Menu of Sublime Text.*


#### Quickly Open the [Quickreference](https://github.com/LucaVazz/SetlXQuickreference/blob/master/SetlX-Quickreference.pdf)
Open the Command Palette (see above) and select `SetlX Helper: Open the SetlX-Quickreference`.
A new browser-window will open to display the Quickreference.


#### Type Common Structures Faster With Snippets
To insert a snippet, just enter its keyword (which is its name, if not noted otherwise below) and press <kbd>Enter</kbd> to insert it. You can then jump through the placeholders by pressing <kbd>Tab</kbd> (and insert a "real" tab by pressing <kbd>Shift</kbd>+<kbd>Tab</kbd>).
![Demonstration of Developing with Snippets](screenshots/readme_snippets.GIF)

**Available snippets:** definition of a `set` / `list` / `closure` / `procedure` / `cached procedure`, `if`-/`else if`-/`else`- / `match` - / `swtich` - statements, `for` - / `while` - loops, try-catch - (keyword: `catch`) / `trace` - blocks, `case` - / `default` - statements.


#### Build System
(For now) you need to install SetlX as described in its manual. This means that you should be able to type `setlx` into a console-window and get the live interpreter fired up.

After that, you can just press <kbd>Ctrl</kbd>/<kbd>Cmd</kbd>+<kbd>B</kbd> to start your SetlX-program and view its results inside Sublie Text own console (at the bottom of your window).

You can switch between running your program inside Sublime Text's own Build-Console (at the bottom of the window) (which doesn't support input) or in an external Command-Line - window by pressing [Ctrl]/[Cmd]+[Shift]+[B] and selecting either "SetlX - in internal Build-Console" or "SetlX - in external Command-Line".

If you just press [Ctrl]/[Cmd]+[B] or just select "SetlX" in the selection-menu mentioned above, the previously selected option will be used.





## Features to Come at Some Point in Time
| Version |             Feature              |                                                                             optional Description                                                                             |
|---------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2.0.0   | [+] build-system - error-parsing | parse all errors from the interpreter's output and get them directly "pinned" to the troubled position in your program                                                       |
| 3.0.0   | real-time basic mistake warning  | marks common (dumb) mistakes (like forgetting a semicolon/a closing bracket, using commas in a vector-definition, etc.) with a warning in real-time in your file as you type |


*Feel free to suggest additional features or to report bugs by using GitHub-Issues.*



### A Note on the Chosen License
This project is licensed under the terms of the *GNU General Public License v3.0*. For further information, please look [here](http://choosealicense.com/licenses/gpl-3.0/) or [here<sup>(DE)</sup>](http://www.gnu.org/licenses/gpl-3.0.de.html).
