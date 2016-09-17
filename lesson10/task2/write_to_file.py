zoo = ['lion', "elephant", 'monkey']

if __name__ == "__main__":
    f = open("output.txt", "w")

    for i in zoo:
        f.write(i+" ")

    f.close()

#If you open a file using "w" (write) as the second argument, a new empty file will be created.
#Note that if another file with the same name exists, it will be deleted.
#If you want to add some content to an existing file, you should use the "a" (append) modifier.
#Add elements from the "zoo" list to "output.txt".