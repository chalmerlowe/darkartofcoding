# Title: demobatch.py
# Revision: 0.8
# Python version: 3.x
# Author: Chalmer Lowe
# Usage: %run demobatch.py <filename.py>
#        * where <filename.py> is the name of the demo file you wish to run
# Description: Launches a demo file enabling interactive demonstrations of python within IPython.

import sys
from IPython.lib.demo import IPythonDemo as demo

n = demo(sys.argv[1])

n()    # immediately run the demo script.
