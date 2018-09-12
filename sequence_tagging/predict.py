from model.data_utils import CoNLLDataset
from model.ner_model import NERModel
from model.config import Config

import json
import os
import sys


def align_data(data):
    """Given dict with lists, creates aligned strings

    Adapted from Assignment 3 of CS224N

    Args:
        data: (dict) data["x"] = ["I", "love", "you"]
              (dict) data["y"] = ["O", "O", "O"]

    Returns:
        data_aligned: (dict) data_align["x"] = "I love you"
                           data_align["y"] = "O O    O  "

    """
    spacings = [max([len(seq[i]) for seq in data.values()])
                for i in range(len(data[list(data.keys())[0]]))]
    data_aligned = dict()

    # for each entry, create aligned string
    for key, seq in data.items():
        str_aligned = ""
        for token, spacing in zip(seq, spacings):
            str_aligned += token + " " * (spacing - len(token) + 1)

        data_aligned[key] = str_aligned

    return data_aligned

def main():
    # create instance of config
    config = Config()

    # build model
    model = NERModel(config)
    model.build()
    model.restore_session(config.dir_model)

    # predict
    path = "data-sequence-tagging/QA4IE-benchmark/"
    file_name_list = [
        "ie_test/0-400/ie_test.span",
        "seq/0-400/dev.seq",
        "seq/0-400/test.seq",
        "seq/0-400/train.seq",
        "seq/400-700/dev.seq",
        "seq/400-700/test.seq",
        "seq/400-700/train.seq",
        "seq/700-/dev.seq",
        "seq/700-/test.seq",
        "seq/700-/train.seq",
        "span/0-400/dev.span",
        "span/0-400/test.span",
        "span/0-400/train.span",
        "span/400-700/dev.span",
        "span/400-700/test.span",
        "span/400-700/train.span",
        "span/700-/dev.span",
        "span/700-/test.span",
        "span/700-/train.span"
    ]

    for file_name in file_name_list:
        ifs = open(path + file_name + ".json", 'r')
        ofs = open(path + file_name + ".ner", 'w')
        dataset_raw = ifs.read()
        dataset = json.loads(dataset_raw)
        index = 0
        for passage in dataset['data']:
            # start of one passage
            ofs.write('#' + str(index) + "\n\n")
            index = index + 1
            for paragraph in passage['paragraphs']:
                context = paragraph['context']
                word_list = context.split(' ')
                preds = model.predict(word_list)
                ofs.write('\n'.join(preds) + '\n\n')
            ofs.write('\n')
        ifs.close()
        ofs.close()
        print("successfully predict " + file_name + '\n')

if __name__ == "__main__":
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    main()
