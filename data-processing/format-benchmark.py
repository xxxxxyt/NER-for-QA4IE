import json
import os
import sys

# https://github.com/xxxxxyt/text-classification/blob/master/word-seg.py

if __name__ == "__main__":

    path = ""
    file_name = ""

    comfirm(path + " " + file_name)

    ifs.open(path + file_name, 'r')
    dataset = ifs.read()
    dataset_json = json.loads(dataset)


def comfirm(msg):
    print("input YES to comfirm: " + msg)
    while True:
        s = input()
        if s == "YES":
            return