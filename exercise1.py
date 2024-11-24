# Python Program to print success rate for MSG3 (RRC Connection Request)

# input file name with extension
file_name = "bs_log.txt"

# using try catch except to
# handle file not found error along with printing exception

# entering try block
try:

    # opening and reading the file
    file_read = open(file_name, "r")

    # search the content MSG3 & eNB-ID in file
    text = "eNB-ID"
    text2 = "MSG3"

    # reading file content line by line.
    lines = file_read.readlines()

    new_list = []
    idx = 0
    count = 0

    # looping through each line in the file
    for line in lines:

        # if line have the input string, get the index
        # of that line and put the
        # line into newly created list
        if text in line:
            if text2 in line:
                new_list.insert(idx, line)
                idx += 1
                if "MSG3-RRC-C-REQ status success" in line:
                    count += 1

    # closing file after reading
    file_read.close()

    # if length of new list is 0 that means
    # the input string doesn't
    # found in the text file
    if len(new_list) == 0:
        print("\n\"" + text + "\" is not found in \"" + file_name + "\"!")
    else:

        # displaying the lines
        # containing given string
        lineLen = len(new_list)
        print("\n**** Lines containing MSG3 \"" + text + "\" ****\n")
        for i in range(lineLen):
            print(new_list[i])

        # print the success rate
        print("\n**** Success Rate Calculation ****\n")
        print("Success Count = "+str(count))
        print("Total count = "+str(lineLen))
        # calculating the overall success rate
        success_rate = round((count/lineLen) * 100, 2)
        print("Success Rate = "+str(success_rate)+"%")

# entering except block
# if input file doesn't exist
except Exception as e:
    print(e)
    print("\n Check for above exception; issue with opening of file")








