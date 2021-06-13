# px-to-rem
Scripts to recursively convert all your css from px to rem values with a single command

The python script can be run directly on a single file with `python ./convert.py PATH/TO/FILE/file.css`

Every file in a directory (found recursively) can be converted at once using `sh ./runScript.sh PATH/TO/FOLDER/folder_name`

Default css file extensions are assumed to be "sass", "less", "css" and "scss". This can be modified in line 7 of convert.py.

Default pixel value of rem is set to 16. This can be modified in line 9 of convert.py.
