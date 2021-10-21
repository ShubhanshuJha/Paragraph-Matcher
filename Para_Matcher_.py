import os


class Reader:
    def __init__(self, filename1, filename2):
        self.filename1, self.filename2 = filename1, filename2
        self.Right, self.Wrong, self.Missed, self.Left = [], [], [], []

    def reader(self):
        f1 = open(self.filename1, "r")
        f2 = open(self.filename2, "r")

        # Generating lists from the data
        s1, s2 = f1.read().split(" "), f2.read().split(" ")
        # print(s1)
        i = 0
        while s1.__sizeof__() > 0 and i < len(s2):
            w2 = s2[i]
            if s1.__contains__(w2):
                self.Right.append(w2)
                # s1.remove(w2)
            elif not s1.__contains__(w2):
                self.Wrong.append(w2)
            i += 1
        i, j = len(s2), 0
        # print(i)
        while j < i and j < len(s1):
            if s1[j] not in self.Right:
                self.Missed.append(s1[j])
            j += 1
        for k in range(j, len(s1)):
            self.Left.append(s1[k])
        f1.close()
        f2.close()


class Writer:
    def __init__(self, f_name, lst):
        self.f_name = f_name
        self.lst = lst

    def write(self):
        if os.path.isfile(self.f_name):
            f = open(self.f_name, "w")
        else:
            f = open(self.f_name, "a+")
        content = str(self.lst)
        content = content[1:-1]
        # Added for inserting the words in the next line if it's in next line while comparison
        content = content.replace("\\n", "\n")
        content = content.replace("\'", "").replace(",", "")  # Removing the unnecessary ' signs
        f.write(content)
        f.close()


if __name__ == '__main__':
    # Files name as per the need
    files = ["Right_Words_List.txt", "Wrong_Words_List.txt", "Missed_Words_List.txt", "Left_Words_List.txt"]
    list_content = [[], [], [], []]
    # main_para_file = "Original.txt"   # .txt file is used for the reference of comparison
    # comp_para_file = "InputFile.txt"  # Content of this .txt file is to be compared
    main_para_file = input("Enter the Original File name: ")
    comp_para_file = input("Enter the Input File name: ")

    r = Reader(main_para_file, comp_para_file)  # Opening both the files in reading mode to collect data
    r.reader()  # Collects and generates lists

    # Displaying the generated lists for checking purpose
    # print("Right:\n", r.Right)
    # print("Wrong:\n", r.Wrong)
    # print("Missed:\n", r.Missed)
    # print("Left:\n", r.Left)
    # Stored the lists in a local variable for ease of access
    list_content[0], list_content[1], list_content[2], list_content[3] = r.Right, r.Wrong, r.Missed, r.Left
    idx = 0
    for content_list in list_content:
        file_name = files[idx]
        w = Writer(file_name, content_list)
        w.write()
        idx += 1
    print('Program Completed.')
