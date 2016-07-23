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

    image = resize_image(image)
    quality = compression_amount(size(base64_data))

    # create the directory for the file.
    hitwfile.makedir(directory)
    dir_to_save = str(directory) + str(filename) + '.jpg'
    image.save(dir_to_save, optimize=True, quality=quality)
    image.close()



def compression_amount(size):
    if (size > 1500000): # > 1.5 megabytes
        return 20
    elif (size < 1500000): # < 1.5 megabyte
        return 30

def resize_image(image):
    width, height = image.size
    new_height = width / 2
    new_width = height / 2
    return image.resize((new_height, new_width), Image.ANTIALIAS)


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
