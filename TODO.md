TODO
=====

Priority
--------

1. Make sure all structures from the base game are properly represented by their editors. It should be possible to set all fields.
2. Use the program to create a sample world to identify that everything is working and to find bugs and feature improvements.
3. Clean up the code one last time and try to make sure that the design and the way modules is reasonable.
4. Setup some unit tests. This is not as hard as it seems. Most of the methods for the gui's can be tested without actually making them visible. It is also a good opportunity to try and pull all the logic that can be out of the gui elements. Probably this means making classes of some kind to represent the data that the gui is working with and then making sure all gui elements just call that objects methods or work with it's attributes.
5. Add code documentation.
6. Add a user manual that describes what each game structure is and does and how to go about creating and setting them up using the editor. This is a must for people to use the tool, but I am putting it later in the priority for now because I don't want to write this and then have to change it a whole bunch once I start working on code and tests and discover I have to change something major.
7. Write a validation script to make sure that worlds that are created will actually run with the engine. This is important for public use of the tool as people will not have the knowledge that I do about what might be wrong if a world fails. This way it can be more certain that it is a world design and not an engine bug. It does not have to be too complicated at first, but check for the most common types of errors.

General
-------

* Write the setup script to allow installing the game so that it is easier to use.
* Once things are in a working order consider it an initial version 0.1 and start changelog and branching.

Validation
==========

* A script to check worlds for common errors.
* Should be automatically run before the engine starts a world, but attached and useable with ease for the editor so that people can confirm the working order of a world before trying to play it.
* Should generate very specific and easy to understand error reports so that people know what they need to fix without too much trouble.
