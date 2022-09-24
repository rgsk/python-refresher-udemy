import sys
import mymodule
from libs.mylib import add

# path used for importing must exist in sys.path for import to work
print('sys.path')
print(sys.path)

# sys.modules specifies the modules that are loaded in current code
# also note sys.modules keeps track of files imported and ensures
# it doesn't go through the entire file for getting the functions/classes/variables etc defined
# as it is costly to run the entire file and get the items
# so even if it is imported twice the file is ran just once

print('sys.modules')
print(sys.modules)
