import base64
import io, hitwfile
from PIL import Image

def base64_decode(encoded_string):
    return base64.b64decode(encoded_string)

def base64_encode(data):
    return base64.b64encode(data)


# Decodes a base64 image and writes it to a file location
def jpeg_and_write_image(directory, filename, base64_data):
    raw_data = base64_decode(base64_data)
    image = Image.open(io.BytesIO(raw_data))

    # create the directory for the file.
    hitwfile.makedir(directory)
    dir_to_save = str(directory) + str(filename) + '.jpg'
    image.save(dir_to_save, optimize=True, quality=50)



def write_image(base64_data):
    raw_data = base64_decode(base64_data)
    image = Image.open(io.BytesIO(raw_data))

    # create the directory for the file.
    hitwfile.makedir(directory)
    image.save(str(directory) + str(filename))


def get_image(file):
    image = Image.open(file)
    return image

def get_image_base64(file, encoding):
    import cStringIO
    image = Image.open(file)
    image_buffer = cStringIO.StringIO()
    image.save(image_buffer, encoding)
    image_base64 = base64.b64encode(image_buffer.getvalue())
    return image_base64

def size(b64string):
    return (len(b64string) * 3) / 4 - b64string.count('=', -2)


def enconding_extensions(encoding):
    if encoding == 'JPEG':
        return '.jpg'
    elif encoding == 'PNG':
        return '.png'
