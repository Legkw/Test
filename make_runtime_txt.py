import platform
 
with open('runtime.txt', 'w') as file: 
   file.write('python-'+platform.python_version())
   