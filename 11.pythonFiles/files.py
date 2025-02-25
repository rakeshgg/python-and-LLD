# location of file to know
# if not in same dirctory knows the path
# always put absolute path

# default mode is read
# directory runing code - /Users/rishikagupta/Documents/Main_LLD_NOTE
# /Users/rishikagupta/Documents/Main_LLD_NOTE - from directory where
# runing the code
# so we can directly use the path as 11.pythonFiles
# total path ->
# /Users/rishikagupta/Documents/Main_LLD_NOTE/11.pythonFiles/files.txt
file = open("11.pythonFiles/files.txt", "r")
# read file
# give all text inside the file as a string
# give one big string
print(file.read())
# always try to close file when its opne
file.close()


# with sytax - Context manager - cleanup when done
# automaticaly close the files
with open("11.pythonFiles/files.txt", "r") as file:
    print(file.read())

# blank lines in files are \n
# give list of readlines files
with open("11.pythonFiles/files.txt", "r") as file:
    print(file.readlines())

# ['hello word!\n', 'add line\n', '\n', '\n', '\n']
# extract word, from file

# line1 want
with open("11.pythonFiles/files.txt", "r") as file:
    line1 = file.readlines()[0]
    print([line1])
    # .strip() removing \n !.e space from last of words
    # removing all leading and traling whitepscae chr in text
    print(line1.strip())

with open("11.pythonFiles/files.txt", "r") as file:
    line1 = file.readlines()[0]
    line1 = line1.replace("\n", "")
    print([line1])

# writing the files
# overirite exiting files if file already exits so very careful
with open("11.pythonFiles/files2.txt", "w") as file:
    file.write("hello word this is a new files\n")
    file.write("hello word this is a new files\n")
    file.write("hello word this is a new files")

# append mode when you want to end of exiting Files
# open the file and put cursor to last of file
with open("11.pythonFiles/files2.txt", "a") as file:
    file.write("hello word this is a new files\n")
    file.write("hello word this is a new files\n")
    file.write("hello word this is a new files")

# r+, mode is opening a file for reading and writing
# going to put file cursor at beging of file
# override the data inside
# r+ mode because you want to preserver some of files
# or because you open the file read inside it and write
# something to it.
with open("11.pythonFiles/files2.txt", "r+") as file:
    file.write("test!\n")

with open("11.pythonFiles/files2.txt", "r+") as file:
    score = file.read()
    # after reading my file cursor is at end of file
    new_score = score + "1"
    print(score)
    # write at the end of files
    file.write(new_score)

with open("11.pythonFiles/files2.txt", "r+") as file:
    score = file.read()
    # after reading my file cursor is at end of file
    # to fix this new method seek is requierd
    new_score = score + "1"
    # chnages the cursor location in the file
    # seek(0) brings begning of the files.
    file.seek(0)
    # 1 is ref points set file cursor where we are
    print(score)
    # write at the end of files
    file.write(new_score)

# reading first 3 lines
with open("11.pythonFiles/files2.txt", "r+") as file:
    # first read the all lines and get till 3rd one
    score = file.readlines()[:3]
    # using indexing loops
    # first 3 lines
    count = 0
    for line in file:
        print(line, end="")
        count += 1
        if count >= 3:
            break
    # easiest way
    for i, line in enumerate(file):
        print(line, end="")
        if i == 2:
            break

    # read first five charachter in files
    file.read(5)
