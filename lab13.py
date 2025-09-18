import csv

# a. Count lines, words, and characters in a file
def a(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)

    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")

def b(filename):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    print("List of lines:", lines)
    return lines

def c(filename):
    with open(filename, "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def d(file1, file2, merged_file):
    with open(file1, "r") as f1, open(file2, "r") as f2, open(merged_file, "w") as out:
        out.write(f1.read())
        out.write("\n")
        out.write(f2.read())
    print(f"Files {file1} and {file2} merged into {merged_file}")

c(r"C:\Users\aumda\OneDrive\Desktop\clg_stuff\sem-3\python\data_sets_for_lab\ict.txt")