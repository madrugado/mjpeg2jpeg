#!/usr/bin/env python

import sys
import os


class imageWriter:
    def __init__(self, filename):
        self.fileCounter = 0
        self.baseFilename = os.path.splitext(filename)[0]
        if not os.path.exists(self.baseFilename):
            os.makedirs(self.baseFilename)
        self.baseFilename += "/" + os.path.basename(self.baseFilename) + "_"
        self.needToWrite = False
        self.fileToWrite = None

    def writeBytes(self, bytesToWrite):
        if self.needToWrite is False:
            if ord(bytesToWrite[0]) == 0xFF and ord(bytesToWrite[1]) == 0xD8:
                self.needToWrite = True
                self.fileToWrite = open(self.baseFilename 
                                        + str(self.fileCounter).zfill(6) 
                                        + ".jpg", "wb+")
                self.fileToWrite.write(bytesToWrite)
        else:
            self.fileToWrite.write(bytesToWrite)
            if ord(bytesToWrite[0]) == 0xFF and ord(bytesToWrite[1]) == 0xD9:
                self.fileToWrite.close()
                self.fileCounter += 1
                self.needToWrite = False



def bytesFromFile(filename, chunksize=2):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                yield chunk
            else:
                break


def main():
    if len(sys.argv) < 2:
        print "Usage: mjpeg2jpeg.py inputFile.mjpeg"
        return 0
    w = imageWriter(sys.argv[1])
    for b in bytesFromFile(sys.argv[1]):
        w.writeBytes(b)

if __name__ == "__main__":
    main()
