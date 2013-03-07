#!/usr/bin/env python

import sys


class imageWriter:
    def __init__(self, filename):
        self.fileCounter = 0
        self.baseFilename = str(filename).split('.')[0]

    def writeBytes(self, bytesToWrite):
        if self.needToWrite is False:
            if bytesToWrite[0] == 0xFF & bytesToWrite[1] == 0xD8:
                self.needToWrite = True
                self.fileToWrite = open(self.baseFilename + str(self.fileCounter) + ".jpg", "wb")
                self.fileToWrite.write(bytesToWrite)
        else:
            self.fileToWrite.write(bytesToWrite)
            if bytesToWrite[0] == 0xFF & bytesToWrite[1] == 0xD9:
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


def main(self):
    if len(sys.argv) < 2:
        print "Usage: mjpeg2jpeg.py inputFile.mjpeg"
        return 0
    w = imageWriter(sys.argv[1])
    for b in bytesFromFile(sys.argv[1]):
        w.writeBytes(b)

if __name__ == "__main__":
    main()
