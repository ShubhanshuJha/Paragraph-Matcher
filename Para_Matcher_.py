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
        while i < len(s2):
            w2 = s2[i]
            w_up, w_low = w2[0:1].upper() + w2[1:], w2[0:1].lower() + w2[1:]
            if s1.__contains__(w_up) or s1.__contains__(w_low):
                self.Right.append(w2)
                # s1.remove(w2)
            elif not s1.__contains__(w_up) and not s1.__contains__(w_low):
                self.Wrong.append(w2)
            i += 1
        i = 0
        # print(s1[1], s2[1])
        # print(s1.index(s2[1]))
        while i < len(s2):
            w1 = s1[i]
            w_up, w_low = w1[0:1].upper() + w1[1:], w1[0:1].lower() + w1[1:]
            # print(w_up, w_low)
            if not s2.__contains__(w_up) and not s2.__contains__(w_low):
                self.Missed.append(w1)
            i += 1
        # print(s2[i - 1])
        i = s1.index(s2[i - 1])  # Fetching index of the last word of InputFile.txt
        # print(s1[i])
        # print(len(s1), len(s2))
        for j in range(i + 1, len(s1)):
            self.Left.append(s1[j])
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
    # main_para_file = "Original.txt"  # .txt file is used for the reference of comparison
    # comp_para_file = "InputFile.txt"  # Content of this .txt file is to be compared
    main_para_file = input("Enter the Original File name: ")
    if ".txt" not in main_para_file:
        main_para_file = main_para_file + ".txt"
    comp_para_file = input("Enter the Input File name: ")
    if ".txt" not in comp_para_file:
        comp_para_file = comp_para_file + ".txt"

    r = Reader(main_para_file, comp_para_file)  # Opening both the files in reading mode to collect data
    r.reader()  # Collects and generates lists

    list_content[0], list_content[1], list_content[2], list_content[3] = r.Right, r.Wrong, r.Missed, r.Left
    idx = 0
    for content_list in list_content:
        file_name = files[idx]
        w = Writer(file_name, content_list)
        w.write()
        idx += 1
    print('Program Completed.')
