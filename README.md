# px-to-rem

The following scripts can be used to recursively convert all your css files from px to rem values with a single command.

The python script can be run directly on a single file with `python ./convert.py PATH/TO/FILE/file.css`

Every file in a directory (found recursively) can be converted at once using the following scripts:

### For Linux systems

`sh ./runScript.sh PATH/TO/FOLDER/folder_name`

### For Windows systems

`powershell.exe -ExecutionPolicy Bypass -File "./runScript.ps1" "PATH/TO/FOLDER/folder_name"`

> Please note that `convert.py` and `runScript.sh`/`runScript.ps1` need to be available in the same directory for the scripts to work.

Default css file extensions are assumed to be "sass", "less", "css" and "scss". This can be modified in line 7 of convert.py.

Default pixel value of rem is set to 16. This can be modified in line 9 of convert.py.
