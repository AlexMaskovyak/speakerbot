import os, sys
from os.path import isfile, join

from PIL import Image


def extract_static_frame(gif_path, out_folder):
    frame = Image.open(gif_path)
    try:
        frame.seek(0)
    except EOFError:
        return False

    frame.save( '%s/%s-static.gif' % (out_folder, os.path.basename(gif_path)), 'GIF')

    return True

def generate_static_frames(path):

        files = [ f for f in os.listdir(path) if isfile(join(path,f)) and "-static.gif" not in f]

        for file in files:
                try:
                        print file
                        #extract_static_frame(path + os.sep + file, path)
                except:
                        print "sudo rm %s" % (path + os.sep + file)

if __name__ == "__main__":

    print generate_static_frames(sys.argv[1])