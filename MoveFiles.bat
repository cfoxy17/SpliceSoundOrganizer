@echo off
cd C:\Users\Collin\Documents\Splice
python -c "import MoveFiles;x=MoveFiles.create_folder();MoveFiles.move_to_root_folder(x,'C:\\Users\\Collin\\Documents\\Splice\\Samples');MoveFiles.organize_files(x);MoveFiles.move_to_FL('C:\\Program Files (x86)\\Image-Line\\FL Studio 10\\Data\\Patches\\FL Audio Samples',x)"
pause