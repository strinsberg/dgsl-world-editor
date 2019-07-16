TODO
====

* Write a test world that uses every structure in everyway it can be used (that you know of right now)
* Write the setup script to allow installing the game so that it is easier to use.
* once the test world has been built and confirmed to work and the setup script is done then start the changelog and the version set to 0.1
* after this like the engine the main areas of work are in testing, documentation, and the like. Because this was written at the beginning of the summer and you are more familiar with python consider fixing up some of the messy code and redesigning bits as you go. May want to do this after some testing is done, or before if it makes things more testable.

* Player needs events and to have its starting position set for sure. Maybe the start could be part of a validation script.
* Try to move as much of the data part of the program out of the gui part so that it can be properly tested. I know lots of the gui will not be automatically testable. But it may be possible to put as much of the logic for doing data operations in places that it can be tested. I will have to look into what I can find about testing gui functions and such. There is certainly no need to create a frame in a window to test some of the supporting functions of a gui, but I am not sure it will be easy. Plus I want to work on the actual game for a while and if the editor is a little rough I am ok with that.

Validation
==========

* validation might just be a script that can be installed along with the programs. Probably it would be best if there were 3 tools packaged together, the engine, editor, and world validator. Though I am not yet sure how to achieve this. Perhaps it would just be best to upload all 3 and make them dependencies?
* There needs to be some validation of the worlds. Ie making sure that every object has at least the required variables for it's type, there are no subject cycles and the like, and that things like player start are not null.
* It might be easier to remember to set all the required variables for an object if its editor was opened automatically on adding a new one.
* might just be better to offer a validation report of somekind that can tell you weather your world is ok. But is not going to stop you from saving it and quitting. Now that the game is in python too the validation script could easily be added to run before a world is loade and make sure it is compatible with the game version and has what it needs.