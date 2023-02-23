# seek() and tell()

with open('myfile.txt','r') as f:
    print(type(f))

    # Move to 10th byte in the file
    f.seek(10)

    current_position=f.tell()             # It gives the seek number
    print(current_position)

    # Read next 5 bytes
    data=f.read(5)
    print(data)

# f.truncate(5)             # allows only 5 letters in file