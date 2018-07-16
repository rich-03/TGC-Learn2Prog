infile = open("data.txt", "r")
outfile = open("data.txt", "w")

infile.close()
outfile.close()

with open("data.txt", "r") as myfile:
    # Print each line
    print(myfile.readline())

with open("data.txt", "w") as myfile:
    # Write from 1 to 10 each line
    print(myfile.write("1, 2, 3, 4, 5, 6, 7, 8, 9, 10"))

with open("data.txt", "w") as myfile:
    # Find the average of these integers
    print(myfile.write("The average is 5.5."))
