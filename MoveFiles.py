import os, shutil, sys, datetime, shutil

def create_folder():
	done=False
	while not done:
		date=datetime.datetime.today().strftime('%Y-%m-%d')
		directory=os.getcwd()+'Splice Samples '+date
		if not os.path.exists(directory):
			os.makedirs(directory)
			print('directory ' + directory + ' was successfully created.')
			done=True
			return directory
		else:
			done=True
			print('requested path already exists.')

def move_to_root_folder(root_path, cur_path):
    for filename in os.listdir(cur_path):
        if os.path.isfile(os.path.join(cur_path, filename)):
            shutil.move(os.path.join(cur_path, filename), os.path.join(root_path, filename)) 
        elif os.path.isdir(os.path.join(cur_path, filename)):
            move_to_root_folder(root_path, os.path.join(cur_path, filename))
        else:
            sys.exit("Should never reach here.")

def move_to_FL(destination, cur_dir):
	done=False
	while not done:
		date=datetime.datetime.today().strftime('%Y-%m-%d')
		newDir=destination+'\\Splice Samples '+date
		if not os.path.exists(newDir):
			os.makedirs(newDir)
			print('directory ' + newDir + ' was successfully created.')
			done=True
		else:
			done=True
			print('requested path already exists.')
			
	list_dir = os.listdir(cur_dir)
	
	
	for sub_dir in list_dir:
		if sub_dir is not None:
			dest = os.path.join(cur_dir,newDir) 
			dir_to_move = os.path.join(cur_dir, sub_dir)
			shutil.move(dir_to_move, dest)
		else:
			shutil.move(cur_dir,newDir)
			
def organize_files(directory):
	print('----------------------------------------------------------')
	for filename in os.listdir(directory):
		filenameORIG = filename
		filename = filename.lower()
		print('looking at: '+filenameORIG)
		claps=filename.find("claps")
		clap=filename.find("clap")
		
		kick=filename.find("kick")
		
		atmosphere=filename.find("atmosphere")
		ambiance=filename.find("ambiance")
		ambience=filename.find("ambience")
		
		snare=filename.find("snare")
		snares=filename.find("snares")
		
		vocal=filename.find("vocal")
		vocals=filename.find("vocals")
		
		horn=filename.find("horn")
		horns=filename.find("horns")
		brass=filename.find("brass")
		
		hat=filename.find("hat")
		hats=filename.find("hats")
		
		string=filename.find("string")
		strings=filename.find("strings")
		orchestra=filename.find("orchestra")
		toms=filename.find("toms")
		tom=filename.find("tom")
		
		sub=filename.find("sub")
		bass=filename.find("bass")
		slide=filename.find("slide")
		EightOEight=filename.find("808")
		
		piano=filename.find("piano")
		
		stomp=filename.find("stomp")
		stop=filename.find("stop")
		
		FX=filename.find("fx")
		
		fill=filename.find("fill")
		
		perc=filename.find("perc")
		percs=filename.find("percs")
		
		if FX != -1:
			if not os.path.exists(directory+"\\FX"):
				os.makedirs(directory+"\\FX")
			shutil.move(directory+"\\"+filename, directory+"\\"+"FX")
			continue
			
		elif toms != -1 or tom != -1:
			if not os.path.exists(directory+"\\Toms"):
				os.makedirs(directory+"\\Toms")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Toms")
			continue
			
		elif stomp != -1 or stop != -1:
			if not os.path.exists(directory+"\\Stomps"):
				os.makedirs(directory+"\\Stomps")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Stomps")
			continue
		
		elif string != -1 or strings != -1:
			if not os.path.exists(directory+"\\Strings"):
				os.makedirs(directory+"\\Strings")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Strings")
			continue
		
		elif piano != -1:
			if not os.path.exists(directory+"\\Piano"):
				os.makedirs(directory+"\\Piano")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Piano")
			continue
		
		elif EightOEight != -1:
			if not os.path.exists(directory+"\\808"):
				os.makedirs(directory+"\\808")
			shutil.move(directory+"\\"+filename, directory+"\\"+"808")
			continue
		
		elif sub != -1 or bass != -1:
			if filename.find("drop") != -1 or slide != -1 or filename.find("wobble") != -1:
				if not os.path.exists(directory+"\\Bass Slides"):
					os.makedirs(directory+"\\Bass Slides")
				shutil.move(directory+"\\"+filename, directory+"\\"+"Bass Slides")
				continue
			elif filename.find("synth") != -1:
				if not os.path.exists(directory+"\\Trap Synths"):
					os.makedirs(directory+"\\Trap Synths")
				shutil.move(directory+"\\"+filename, directory+"\\"+"Trap Synths")
				continue
		
		elif filename.find("synth") != -1:
			if filename.find("stab") != -1 or filename.find("shot") != -1:
				if not os.path.exists(directory+"\\Trap Synths"):
					os.makedirs(directory+"\\Trap Synths")
				shutil.move(directory+"\\"+filename, directory+"\\"+"Trap Synths")
				continue
			elif filename.find("loop") != -1:
				if not os.path.exists(directory+"\\Synths"):
					os.makedirs(directory+"\\Synths")
				shutil.move(directory+"\\"+filename, directory+"\\"+"Synths")
				continue
			else:
				if not os.path.exists(directory+"\\Synths"):
					os.makedirs(directory+"\\Synths")
				shutil.move(directory+"\\"+filename, directory+"\\"+"Synths")
				continue
		
		elif orchestra != -1:
			if not os.path.exists(directory+"\\Orchestra"):
				os.makedirs(directory+"\\Orchestra")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Orchestra")
			continue
		
		elif claps != -1 or clap != -1:
			if not os.path.exists(directory+"\\Claps"):
				os.makedirs(directory+"\\Claps")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Claps")
			continue
			
		elif kick != -1:
			if not os.path.exists(directory+"\\Kicks"):
				os.makedirs(directory+"\\Kicks")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Kicks")
			continue
			
		elif ambiance != -1 or ambience != -1 or atmosphere != -1:
			if not os.path.exists(directory+"\\Atmospheres"):
				os.makedirs(directory+"\\Atmospheres")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Atmospheres")
			continue
			
		elif snare != -1 or snares != -1:
			if not os.path.exists(directory+"\\Snares"):
				os.makedirs(directory+"\\Snares")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Snares")
			continue
			
		elif vocal != -1 or vocals != -1:
			if not os.path.exists(directory+"\\Vocals"):
				os.makedirs(directory+"\\Vocals")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Vocals")
			continue
			
		elif horn != -1 or horns != -1 or brass != -1:
			if not os.path.exists(directory+"\\Brass"):
				os.makedirs(directory+"\\Brass")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Brass")
			continue
			
		elif fill != -1:
			if not os.path.exists(directory+"\\Fills"):
				os.makedirs(directory+"\\Fills")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Fills")
			continue
			
		elif hat != -1 or hats != -1:
			open=filename.find("open")
			closed=filename.find("closed")
			if open != -1:
				if not os.path.exists(directory+"\\Open Hats"):
					os.makedirs(directory+"\\Open Hats")
				shutil.move(directory+"\\"+filename, directory+"\\"+"Open Hats")
				continue
			
			elif closed != -1:
				if not os.path.exists(directory+"\\Closed Hats"):
					os.makedirs(directory+"\\Closed Hats")
				shutil.move(directory+"\\"+filename, directory+"\\"+"Closed Hats")
				continue
			else:
				if not os.path.exists(directory+"\\Hats"):
					os.makedirs(directory+"\\Hats")
				shutil.move(directory+"\\"+filename, directory+"\\"+"Hats")
				continue
		
		elif perc != -1 or percs != -1 or filename.find("snap") != -1 or filename.find("shaker") != -1:
			if not os.path.exists(directory+"\\Percs"):
				os.makedirs(directory+"\\Percs")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Percs")
			continue
			
		elif filename.find("stab") != -1:
			if not os.path.exists(directory+"\\Misc. Stabs"):
				os.makedirs(directory+"\\Misc. Stabs")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Misc. Stabs")
			continue
			
		elif filename.find("guitar") != -1:
			if not os.path.exists(directory+"\\Guitar"):
				os.makedirs(directory+"\\Guitar")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Guitar")
			continue
			
		elif filename.find("breakbeat") != -1 or filename.find("break-beat") != -1 or filename.find("break") != -1:
			if not os.path.exists(directory+"\\Breakbeat"):
				os.makedirs(directory+"\\Breakbeat")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Breakbeat")
			continue
			
		elif filename.find("melody") != -1:
			if not os.path.exists(directory+"\\Melody"):
				os.makedirs(directory+"\\Melody")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Melody")
			continue
		
		down=filename.find("down")	
		build=filename.find("build")
		buildup=filename.find("build-up")
		buildup2=filename.find("buildup")
		sweep=filename.find("sweep")
		riser=filename.find("riser")
		rise=filename.find("rise")
		
		if down != -1:
			if sweep != -1:
				if not os.path.exists(directory+"\\Downsweeps"):
					os.makedirs(directory+"\\Downsweeps")
				shutil.move(directory+"\\"+filename, directory+"\\"+"Downsweeps")
				continue
				
		elif sweep != -1 or build != -1 or buildup != -1 or buildup2 != -1 or riser != -1 or rise != -1:
			if not os.path.exists(directory+"\\Build-up"):
				os.makedirs(directory+"\\Build-up")
			shutil.move(directory+"\\"+filename, directory+"\\"+"Build-up")
			continue
			
	print('----------------------------------------------------------')
