from fileinput import filename
from math import fabs
import os
import glob
import re

# ALL THE FILES IN THE DIRECTORY
count = 0
for root_dir, cur_dir, files in os.walk(r'./'):
    for file in files:
        count += 1
print('Total files:', count)


# number of files that are not named index.md
counter = 0
for root_dir, cur_dir, files in os.walk(r'./'):
    for file in files:
        if not file.endswith("index.md"):
            counter += 1
print("Files that are not index.md: ", counter)



# files that don't end in .es or .pt (the english ones)

not_es_or_pt_files = 0
for root_dir, cur_dir, files in os.walk(r'./'):
    for file in files:
        if not file.endswith(".es.md") and not file.endswith(".pt") and not file.endswith(".es"):
            not_es_or_pt_files += 1
print("Files that does not end with pt or es: ", not_es_or_pt_files)


not_es_pt_or_index = 0
for root_dir, cur_dir, files in os.walk(r'./'):
    for file in files:
        if not file.endswith(".es.md") and not file.endswith(".pt") and not file.endswith(".es") and not file.endswith("index.md"):
            not_es_pt_or_index += 1
print("Files that are not index, pt or es: ", not_es_pt_or_index)


def search_str(file_path, word):
   with open(file_path, encoding="utf8", errors='ignore') as file:
    for line_number, line in enumerate(file, start=1):  
        if word in line:
          return True
    return False
        

#  files without the metadata have a speaker that can be parsed from the file name
#not index or .es
# does not have name
no_author_files = 0
for root_dir, cur_dir, files in os.walk(r'./'):
    for name in files:
        if not name.endswith("index.md") and not name.endswith(".es.md"):
            file_path = os.path.abspath(os.path.join(root_dir, name))
            if not search_str(file_path, "name"):
                no_author_files += 1

print("Files without author name: ", no_author_files)

with_author_name = 0
for root_dir, cur_dir, files in os.walk(r'./'):
    for name in files:
        if not name.endswith("index.md") and not name.endswith(".es.md"):
            file_path = os.path.abspath(os.path.join(root_dir, name))
            if search_str(file_path, "name"):
                with_author_name += 1

print("Files with author name: ", with_author_name)


# how many have a video link 
video_links = 0
for root_dir, cur_dir, files in os.walk(r'./'):
    for name in files:
        if not name.endswith("index.md") and not name.endswith(".es.md"):
            file_name = os.path.abspath(os.path.join(root_dir, name))
            if not search_str(file_name, "video:"):
                video_links += 1

print("Files with video links: ", video_links)


def find_date(date_file, pattern):
    f = open(date_file, encoding="utf8", errors='ignore')

    content = f.read()

    dates = re.findall(pattern, content)
    if len(dates) > 0:
        return True
    else:
        return False


# Files with a date
files_with_date = no_with_year = 0
pattern = "\d{4}[/-]\d{2}[/-]\d{2}"
year_last_pattern = "\d{2}[/-]\d{2}[/-]\d{4}"
year_pattern = "\d{4}"

for root_dir, cur_dir, files in os.walk(r'./'):
    for name in files:
        if not name.endswith("index.md") or not name.endswith(".es.md"):
            file_name = os.path.abspath(os.path.join(root_dir, name))
            if find_date(file_name, year_pattern):
                no_with_year += 1
            if find_date(file_name, pattern) or find_date(file_name, year_last_pattern):
                files_with_date += 1

print("Files with year date: yyyy ", no_with_year)
print("Files with a date. Format yyyy-mm-mm or dd-mm-yyyy: ", files_with_date)



# Files without a date
without_date = filename_with_year = only_year = 0
for root_dir, cur_dir, files in os.walk(r'./'):
    for name in files:
        if not name.endswith("index.md") and not name.endswith(".es.md"):
            file_name = os.path.abspath(os.path.join(root_dir, name))
            if not find_date(file_name, pattern) and not find_date(file_name, year_last_pattern):
                without_date += 1
                if len(re.findall(pattern, file_name)) > 0:
                    filename_with_year += 1
                if len(re.findall(year_pattern, file_name)) > 0:
                    only_year += 1

print("Files without a date. Format yyyy-mm-mm or dd-mm-yyyy: ", without_date)
print("Files without a date in body but has date [yyyy-mm-dd] in filename ", filename_with_year)
print("Files without a date in body but has year [yyyy] in filename ", only_year)


