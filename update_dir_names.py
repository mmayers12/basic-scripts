#!/bin/python3

import os
import shutil

# Fix these two functions to change how things are named
def determine_if_needs_fix(d):
    return len(d) == 8 and '-' not in d and '.' not in d
def convert_to_new_name(old_dir):
    return old_dir[:4] + '-' + old_dir[4:6] + '-' + old_dir[6:8]


def move_to_new_dir(old_dir):
    new_dir = convert_to_new_name(old_dir)

    to_dir = os.path.join(os.getcwd(), new_dir)
    from_dir = os.path.join(os.getcwd(), old_dir)

    os.mkdir(to_dir)

    for file in os.listdir(from_dir):
        print(from_dir+'/'+file, '->', to_dir+'/'+file)
        shutil.move(os.path.join(from_dir, file), to_dir)


if __name__ == "__main__":
    for d in os.listdir():
        if determine_if_needs_fix(d):
            if os.path.isdir(d):
                move_to_new_dir(d)
                shutil.rmtree(d)

