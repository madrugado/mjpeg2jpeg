import sys

def bytes_from_file(filename, chunksize=2):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
  			   yield chunk 
            else:
                break
               
def bytes_to_file(filename, bytes):
	i = 0
	while True:
		break

def main():
	for b in bytes_from_file(sys.argv[1]):
		

	
	out_file = open("out-file", "wb") # open for [w]riting as [b]inary
	out_file.write(data)
	out_file.close()

if __name__ == "__main__":
    main()
