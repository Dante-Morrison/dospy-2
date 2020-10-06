# DosPY2
the succsessor to the original dospy

# All of this is still in development so not everything has been implemented yet

rest assured, it still features the same serverside technology that makes it technically impossible to block

# Features
DosPY2 features a new emulation subsystem kniwn as v86. this means it will be able to emulate much more complicated games like half life. it will also be capable of emulating operating systems like windows 95 or 98, or even lightweight linux distros for use of modern software. it is now more modular than ever and on release will feature all the documentation to get started adding your own games or hosting your own cloud emulator.

# Add more games
to add more games to your own branch, you must first upload the zip file for your dos game. i recommend that you
modify it with whatever needed changes you want (controlls, wads, ect). then make a new html file in the templates
file. copy the code from one of the templates and paste it to the new one. then modify the code and point it twords your
zip file and change the built in directory to the corresponding one of the zip file. in short, point it to the zip, and then the exe location within the zip file.

after that it needs to be initialized in the flask container too. this is optional if you dont really care about the flask layer. to do this, add another directory in the main.py script. its okay to copy one of the other existing directories, just be sure to rename it for it to work. also be sure to point it in the direction of your new page rather than the old page.

#DosPY DB
we are working on adding an official dospy database so you can add your own file and contribute games. it will also be a place to add isos and bios drivers so you can add your favorites with full support. the database will aslo be open so if youd like you couls make your own dospy and add support for any of the available games

# additional info
this project was made with repl.it and therefore works best with that. to run it in repl, create a new project from this repo and set the language to python. also make it run the main.py script in the file.

alternatively you can find the repl project and simply fork it there. although im not too sure about things like the whole github commit feature working.
