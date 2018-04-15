import os

for x in range(1, 10):
    m=str(x);
    os.chdir('/home/snewbie/Downloads/skripsi/clean/'+m)
    path =  os.getcwd()
    filenames = os.listdir(path)

    for filename in filenames:
       os.rename(filename, filename.replace(" ", "").lower())

    os.chdir('/home/snewbie/Downloads/skripsi/food/'+m)
    path =  os.getcwd()
    filenames = os.listdir(path)

    for filename in filenames:
       os.rename(filename, filename.replace(" ", "").lower())

    os.chdir('/home/snewbie/Downloads/skripsi/water/'+m)
    path =  os.getcwd()
    filenames = os.listdir(path)

    for filename in filenames:
       os.rename(filename, filename.replace(" ", "").lower())

    os.chdir('/home/snewbie/Downloads/skripsi/dirty/'+m)
    path =  os.getcwd()
    filenames = os.listdir(path)

    for filename in filenames:
       os.rename(filename, filename.replace(" ", "").lower())

