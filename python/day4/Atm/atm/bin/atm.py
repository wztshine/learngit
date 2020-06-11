import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,base_dir)
# print(list(sys.path)[0])
from atm.core import main

if __name__ == '__main__':
    main.run()






