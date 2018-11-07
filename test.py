import os 
files = os.listdir('./casas')
for file in files:
    if '.html' in file:
      print(file)