#renaming of modules
import mymodule as mine
mine.reaction("Santhosh")

#built in modules
import platform
x=platform.system()
print(x)

#Lists all the defined names belonging to the module
print(dir(platform))
print(dir(mine))

import sys
print(sys.path) #prints the list of directories that the interpreter search for the required module

 