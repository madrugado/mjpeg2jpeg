import sys

class imageWriter:
    def __init__(self, filename):
        self.i = 0
        self.baseFilename = filename

    def writeBytes(self, bytes):
        if self.needToWrite is False:
            if bytes[0] == 0xFF & bytes[1] == 0xD8:
                self.needToWrite = True
                self.fileToWrite = open(self.baseFilename + str(self.i), "wb")
                self.fileToWrite.write(bytes)
        else:
            self.fileToWrite.write(bytes)
            if bytes[0] == 0xFF & bytes[1] == 0xD9:
                self.fileToWrite.close()
                self.i += 1
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
    w = imageWriter(sys.argv[1])
    for b in bytesFromFile(sys.argv[1]):
        w.writeBytes(b)

if __name__ == "__main__":
    main()
