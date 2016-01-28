# <demo> silent
# Title: Data Analysis Tools Overview (anaconda, ipython, numpy, and pandas)
# Filename: da_tools_overview.py
# Usage: da_tools_overview.py
# Description: 
#     A short overview of anaconda, ipython, numpy and pandas
# Author: Chalmer Lowe, Dark Lord of Python
# Version: 0.5
# Python Revision: 3.x
# IPython Revision: 3.0+
# TO DO:
# 
#---------------------------------------------------------

# <demo> stop
# Today, we will discuss a high level overview of several data analysis tools.
# Each of these tools will be used in our upcoming Data Analysis Series.
# 
# Anaconda
# IPython
# numpy
# pandas

# and if we have time... we'll solve a puzzle from one of my 
# favorite puzzle sites: 
#     checkio.org


# <demo> stop
# Our demo scripts will be available on github at:
#     https://github.com/chalmerlowe/darkartofcoding/tree/master/data_analysis

#     https://goo.gl/MzSJoL


# <demo> stop
# Let's start with Anaconda
# From Continuum Analytic's webpage:

#     "Anaconda is a completely free Python distribution (including for commercial
#      use and redistribution). It includes more than 300 of the most popular Python
#      packages for science, math, engineering, and data analysis."

# Anaconda solves some tricky problems:
#     * resolves interdependencies between multiple libraries
#     * installs as a single bundle or you can pick and choose libraries
#     * takes a lot of the headache out of setting up a computing environment

# Download here:  https://www.continuum.io/downloads


# <demo> stop
# Anaconda includes many libraries, including:
#     * IPython     A powerful interactive shell & more
#     * numpy       The fundamental package for scientific computing with Python.
#     * scipy       A scientific computing package for Python
#     * astropy     Astronomy tools
#     * googlecl    Tool to use some Google APIs
#     * lxml        XML library
#     * nltk        Natural Language Toolkit
#     * pandas      Data analysis library
#     * beautifulsoup4  Screen scraping library


# <demo> stop
# One of my favorite programs included in Anaconda is IPython.

# IPython includes:
#     * A powerful interactive shell.

#     * A kernel for Jupyter - A Jupyter Notebook is a web application that allows you
#       to create and share documents that contain live code, equations, visualizations
#       and explanatory text. 

#     * Support for interactive data visualization and GUI toolkits:
#           * wxPython
#           * PyQt4/PySide
#           * PyGTK
#           * Tk

#     * Easy to use, high performance tools for parallel computing:
#           * Single program, multiple data (SPMD) parallelism.
#           * Multiple program, multiple data (MPMD) parallelism.
#           * Message passing using MPI.
#           * Task farming.
#           * Data parallel.
#           * Combinations of these approaches.


# <demo> stop
# Let's talk about some of the ways that IPython can help you:
# Getting help is a breeze:

# In regular python, if you want help on a function like print, you need to
# use the help() function like this:
# help(print).

# With IPython, this is greatly simplified to just a ? OR ??

# print?          # note we are not including the parens

# To see the source code for the item you are interested in, sometimes 
# the double question marks will work. To see this in action, I will import
# the datetime module and we will look at the timedelta class.

import datetime as dt
 
# dt.timedelta??


# <demo> stop
# Help can be used on modules, classes/objects, functions, methods, etc
# Let's take a look at several examples:

import math

# math?
# math.sqrt?

def doubler(int):
    '''doubler(int) -> int

doubler is a world-class function that takes in an integer
and returns a number that is:
yep, you guessed it...
twice as large'''
    return int * 2

# doubler?
# doubler??



# <demo> stop
# Another excellent feature of IPython is the tab-complete feature
# which is common to command line interfaces.
# IPython includes tab completion against
#     * operating system/file system objects, like files/paths
#     * functions and methods
#     * variable names
#     * and more

# For example:
# fin = open('events.1a.csv')        # open a file
# math.log10()                       # calc the logarithm (base 10) of a num
# zvar                               # a variable we will set up...

zvar = 1
zvariant = 20
zvariation = 300

# <demo> stop
# Another great feature of IPython is that it gives you access to the 
# underlying operating system commands with very little fuss.
# Let's demo a few:

# ls -al
# !chmod 777 events.1.csv
# !less events.csv
# cd
# cd -<tab key>      # use tab key completion after the hyphen


# <demo> stop
# The next great feature of IPython is the builtin 'magic' commands:
# These commands are built into IPython and expose many useful features
# that speed up analysis, increase productivity and simplify workflows.
# Here are some of my favorites:

# %hist -n
# %hist -g chmod
# %hist -o -p        # OR hist -op

# %save ex_save.py 1-5 8 10
# %save -a ex_save.py 12 13-16


# <demo> stop
# More of my faves!

# %recall 12 13-16
# %rerun

# %timeit [x * x for x in range(10)]
# VS
# timeit [x ** 2 for x in range(10)]


# <demo> stop
# I like these too... 

# %cpaste
# %run 

# How do you know what magics exist:
# %quickref


# <demo> stop
# Let's shift gears and take a look at numpy

# numpy is widely used in the background by other scientific and data analysis programs AND used outright for its efficient numerical handling.
# From a high level perspective, it provides:

#     * a powerful N-dimensional array object
#     * sophisticated (broadcasting) functions
#     * useful linear algebra, Fourier transform, and random number capabilities
#     * tools for integrating C/C++ and Fortran code


# <demo> stop
#

import numpy as np
a = np.arange(15)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

# <demo> stop
#

for item in a:
    print(item)

# <demo> stop
#

f = a.astype('float16')
print(f.dtype, '\n', f)
print('What is f?:', type(f))

# <demo> stop
# 

r = a.reshape(3, 5)


# <demo> stop
#
b = np.array([5, 6, 7, 8])
c = np.array([[1.5, 3, 6], [7, 8, 9]])

# <demo> stop
#

inc = np.arange(42, 82, 10)
lin = np.linspace(13, 42, 100)

# <demo> stop
#

neglin = np.linspace(-50, 50, 101)
absolute = np.abs(neglin)


# <demo> stop
#

r = a.reshape(3, 5)
# r.sum()
# r.std()
# r.<tab key>

# <demo> stop
# np functions
sums = np.apply_along_axis(sum, 1, r)

def max_sq(numbers):
    maximum = max(numbers)
    return maximum ** 2

biggest_square = np.apply_along_axis(max_sq, 1, r)



# <demo> stop
# vector mathematics...
# r = array([[ 0,  1,  2,  3,  4],
#            [ 5,  6,  7,  8,  9],
#            [10, 11, 12, 13, 14]])

additive = r + 5
additive

# <demo> stop
# saving data...
np.savetxt('np.out', r, delimiter=',')

# !less np.out

# <demo> stop
#
import pandas as pd
from pandas import DataFrame, Series

# df = pd.read_csv?
df = pd.read_csv('events.csv', header=None)


# <demo> stop
#
df.columns = ['name', 'email', 'fmip', 'toip', 'datetime', 'lat', 'long', 'payload_size']
df


# <demo> stop
#
# df.datetime
# df.lat
# df[df['lat'] > 49]


# <demo> stop
#
# df.payload_size.<tab key>
# df.payload_size.max()
# df.payload_size.min()
# df.payload_size.std()
# df.payload_size.mean()
# df.payload_size.median()
# df.payload_size.apply...

# <demo> stop
#
# round?
df.payload_size.apply(round, args=(-3,))


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


# <demo> stop
#


