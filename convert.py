import re
import sys

# get file path from command line
filePath = sys.argv[1]
# file extensions to use
fileExtensions = ("sass", "less", "css", "scss", "jsx", "js")
# value of rem in pixel
remValue = 16

if(filePath.endswith(fileExtensions)):
    print("processing file ", filePath)

    # pattern to find all pixel values
    pattern = r'([0-9\.]+)px'

    def replacer(match):
        # get the first subgroup which would be the pixel value
        value = match.group(1)
        if value:
            # typecast into a float and divide by 16
            ret = str(float(value)/remValue)
            # convert floats ending with .0 to integer (3.0 -> 3)
            ret = ret.rstrip('0').rstrip('.')
            # add the rem sufffix
            return ret + "rem"
        else:
            # return the original string if there's no value
            return match.group(0)

    # read the file
    readFile = open(filePath, 'r')
    content = readFile.read()
    readFile.close()

    # run the replacement
    modifiedContent = re.sub(pattern, replacer, content)

    # write to file
    writeFile = open(filePath, 'w')
    writeFile.write(modifiedContent)
    writeFile.close()
