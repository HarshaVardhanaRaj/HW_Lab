# Handle IO Error


def write_to_ReadOnly_file(): 
    filename = "/sys/readonly_test.txt" #random file which doesn't exist
    try:
        with open(filename, "w") as f:
            f.write("Trying to write to a read-only file!")
    except IOError:
        print("Caught an IOError. Check file name")
        
write_to_ReadOnly_file()
