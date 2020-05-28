import os

# Count all of the text files in a directory and all
# subdirectories, recursively
# I'm not actually sure if it accounts for idiosyncracies of 
# an operating system that I don't know about but it works in nice
# little test environemnets where
def count_txt(directory, count = 0):
    try:
        files_n_dirs = os.listdir(directory)
        count = 0

        # count all text files in current dir, add those to count
        for thing in files_n_dirs:
            if thing.endswith(".txt"):
                count += 1
            # if theres no "." in thing, let's assume it's a directory
            elif "." not in thing:
                count += count_txt(directory + thing + "/")
        return count
    except (FileNotFoundError, NotADirectoryError):
        return 0

print(count_txt("/home/reilley/projects/practice/recursion/file_count/"))
