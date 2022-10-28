from math import fabs
import os
import glob
import re

# ALL THE FILES IN THE DIRECTORY
count = not_index_no = 0
for root_dir, cur_dir, files in os.walk(r'./'):
    count += len(files)
print('Total files:', count)


# number of files that are not named index.md
counter = 0
for filename in glob.glob("**/*", recursive=True):
    if not filename.endswith("index.md"):
        counter += 1
print("Files that are not index.md: ", counter)



# files that don't end in .es or .pt (the english ones)

not_es_or_pt_files = 0
for filename in glob.glob("**/*", recursive=True):
    if not filename.endswith(".es.md") and not filename.endswith(".pt") and not filename.endswith(".es"):
        not_es_or_pt_files += 1
print("Files that does not end with pt or es: ", not_es_or_pt_files)


def search_str(file_path, word):
   with open(file_path, encoding="utf8", errors='ignore') as file:
    for line_number, line in enumerate(file, start=1):  
        if word in line:
          return True
    return False
        

# files without the metadata have a speaker that can be parsed from the file name
#not index or .es
# does not have name
no_author_files = 0
for root_dir, cur_dir, files in os.walk(r'./'):
    for name in files:
        if not name.endswith("index.md") and not name.endswith(".es.md"):
            file_name = os.path.abspath(os.path.join(root_dir, name))
            if not search_str(file_name, "name") and not search_str(file_name, "author"):
                no_author_files += 1

print("Files without author name: ", no_author_files)


#files without the metadata have a date that can be parsed from the file name
# will need to come back to this

#how many have a video link 
video_links = 0
for root_dir, cur_dir, files in os.walk(r'./'):
    for name in files:
        if not name.endswith("index.md") and not name.endswith(".es.md"):
            file_name = os.path.abspath(os.path.join(root_dir, name))
            if not search_str(file_name, "video"):
                video_links += 1

print("Files with video links: ", video_links)


def find_date(date_file):
    f = open(date_file, encoding="utf8", errors='ignore')

    content = f.read()

    # date pattern
    pattern = "\d{2}[/-]\d{2}[/-]\d{4}"

    dates = re.findall(pattern, content)

    for date in dates:
        return True

    return False


# Files with a date
files_with_date = 0
for root_dir, cur_dir, files in os.walk(r'./'):
    for name in files:
        if not name.endswith("index.md") and not name.endswith(".es.md"):
            file_name = os.path.abspath(os.path.join(root_dir, name))
            if not find_date(file_name):
                files_with_date += 1

print("Files with a date: ", files_with_date)




