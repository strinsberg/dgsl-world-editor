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

* Items in list should have more identifying information than just their name. Otherwise objects with the same name are hard to find in the list.
* The message and description input boxes should be text boxes instead of just one liners.
* Write the setup script to allow installing the game so that it is easier to use.
* Once things are in a working order consider it an initial version 0.1 and start changelog and branching.

Validation
----------

* A script to check worlds for common errors.
* Should be automatically run before the engine starts a world, but attached and useable with ease for the editor so that people can confirm the working order of a world before trying to play it.
* Should generate very specific and easy to understand error reports so that people know what they need to fix without too much trouble.

Bugs and Annoyances
-------------------

* every event creation should not require a verb.
* The reorganization of the lists is frustrating. I didn't really like using alphabetical order and I don't like that it will be different every time I load because it is in a map. So it needs an index number to sort by. This can work with a move function when I implement one.

* Froze when I tried to access the player right after saving. Program used to freeze once in a while and I am not sure if this is that kind of thing or if it is tied to what I did. Should probably implement an auto save that happens frequently so that people don't lose a lot of hard work.

Features
--------

* some factories that make common objects with less work. Major one is a 2 way door. If there is no 2 way door object yet then it can just create both of the doors and their move events with the verb you want. It woould require both rooms to already exist, but with a minimum amount of work to actually create them fully functional.
* Order room, items, and events how you would like.
* Move an object to another place.
* Clone an object, w/ and option to move it to another place or perhaps just rename it. The need for this is greatly reduced with a few factories for really common objects.
* Really need a change description event. Or to make it possible to make the description itself an event or have an event that plays in addition to the message so that there can be adjustable descriptions. Say if a person is injured, when you help them their description should not say they are injured.
* Even to add some extra settings for certain events and items so that you don't have to edit them after creation, but things you can leave blank if you need to. Like a move event should make it possible to set the destination, but not required. It would actually save on validation if doors required the destination before they were created so that you couldn't forget it. Then the only way it could be without one is if you removed the room, which is a whole other problem.
* possibly a way to change event type when you make a mistake would be cool without having to totally remove it.
