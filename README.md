# SpliceSoundOrganizer

Everyone can agree that after a long session on Splice, it can be extremely annoying to try to get all your new files out of the mess of folders in your Documents->Splice->Samples folder. This program will go through all these, organize them by Hi-Hat/808/Kick/Synth/Piano/etc, and then move the organized folder to the directory of your choosing (I have it move them to my FL Studio patches folder)

To configure it, all you have to do is:
-save these two files to your Splice folder in "Documents" (or wherever your splice sounds save to)
-**edit the paths in bold** below so the program is looking at the right paths

To use it:
-double-click on MoveFiles.bat to run program

*(file: MoveFiles.bat)*

@echo off 
cd **C:\Users\Collin\Documents\Splice** python -c "import MoveFiles;x=MoveFiles.create_folder();MoveFiles.move_to_root_folder(x,'**C:\\Users\\Collin\\Documents\\Splice\\Samples'**);MoveFiles.organize_files(x);MoveFiles.move_to_FL('**C:\\Program Files (x86)\\Image-Line\\FL Studio 10\\Data\Patches**',x)" 
pause

