#!/usr/bin/python

import os, sys

# Open a file
path = "/Downloads/tf1/tf_files/skripsi/food/1/"
dirs = os.listdir( path )

path1 = "/Downloads/tf1/tf_files/skripsi/dirty/1/"
dirs1 = os.listdir( path1 )

path2 = "/Downloads/tf1/tf_files/skripsi/water/1/"
dirs2 = os.listdir( path2 )


# This would print all the files and directories
for file1 in dirs:
   print file1
   os.rename(file1, file1.replace(" ", "").lower())

# This would print all the files and directories
for file2 in dirs1:
   print file2
   os.rename(file2, file2.replace(" ", "").lower())

# This would print all the files and directories
for file3 in dirs2:
   print file3
   os.rename(file3, file3.replace(" ", "").lower())
