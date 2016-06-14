import os


# Writes a file.
def writefile(location, filename, contents):
    # Attempt to create directory
    createdir(location)
    # Write to file.
    with open(location + filename, 'w') as f:
        f.write(contents)
        f.close()

# Creates a directory if it does not exist already.
def makedir(location):
    if not os.path.exists(location):
        os.makedirs(location)
