TODO
====

* Player needs events and to have its starting position set for sure. Maybe the start could be part of a validation script.
* Change the way this works with things like decorators. To decorate with a message is just adding a 'message' field to the object. It should just be possible to add more decorators to an object. as long as it is not too messy.
* Make sure that things here fit with the engine as it is changing some with the rewrite in python.
* Try to move as much of the data part of the program out of the gui part so that it can be properly tested. I know lots of the gui will not be automatically testable. But it may be possible to put as much of the logic for doing data operations in places that it can be tested. I will have to look into what I can find about testing gui functions and such. There is certainly no need to create a frame in a window to test some of the supporting functions of a gui, but I am not sure it will be easy. Plus I want to work on the actual game for a while and if the editor is a little rough I am ok with that.

Validation
==========

* There needs to be some validation of the worlds. Ie making sure that every object has at least the required variables for it's type, there are no subject cycles and the like, and that things like player start are not null.