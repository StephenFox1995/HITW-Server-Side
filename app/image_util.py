import base64
import io, hitwfile
from PIL import Image

def base64_decode(encoded_string):
    return base64.b64decode(encoded_string)

def base64_encode(data):
    return base64.encode(data)


# Decodes a base64 image and writes it to a file location
def jpeg_and_write_image(directory, filename, base64_data):
    raw_data = base64_decode(base64_data)
    image = Image.open(io.BytesIO(raw_data))

    # create the directory for the file.
    hitwfile.makedir(directory)
    dir_to_save = str(directory) + str(filename) + '.jpg'
    image.save(dir_to_save, 'JPEG')
    

def write_image(base64_data):
    raw_data = base64_decode(base64_data)
    image = Image.open(io.BytesIO(raw_data))

    # create the directory for the file.
    hitwfile.makedir(directory)
    image.save(str(directory) + str(filename))
