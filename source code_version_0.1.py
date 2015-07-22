__version__='0.1'
__author__='MYSTIC DAV'
from tkinter import filedialog
import os
import zipfile
file=filedialog.askdirectory()
file_out_dir=filedialog.askdirectory()
file_out_name=input('enter name of output file')
new=os.path.join(file_out_dir,file_out_name)
zf = zipfile.ZipFile(new+".zip", "w")

for dirname, subdirs, files in os.walk(file):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()
