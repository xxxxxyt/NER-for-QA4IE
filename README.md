# NER-for-QA4IE

## Run the Experiments

> In the root of the repository, first make the `tmp` directory:

```
mkdir tmp
```

> To train a NER model,

```
./example/run_ner_crf.sh
```

> Note: If you want to apply the sequence labeling model to other tasks or different datasets, please be sure to remove the corresponding folders storing the vocabularies located in `data/alphabets/`. Otherwise, the old vocabularies will be loaded from disk.



## Data Format

Data format is the same as in [NeuroNLP2](https://github.com/XuezheMax/NeuroNLP2/issues/9).

> For the data used for NER, our data format is similar to that used in CoNLL 2003 shared task, with a little bit difference. An example is in following:

```
1 EU NNP I-NP I-ORG
2 rejects VBZ I-VP O
3 German JJ I-NP I-MISC
4 call NN I-NP O
5 to TO I-VP O
6 boycott VB I-VP O
7 British JJ I-NP I-MISC
8 lamb NN I-NP O
9 . . O O

1 Peter NNP I-NP I-PER
2 Blackburn NNP I-NP I-PER
3 BRUSSELS NNP I-NP I-LOC
4 1996-08-22 CD I-NP O
...
```

> where we add an column at the beginning to store the index of each word. The original CoNLL-03 data can be downloaded [here](https://github.com/glample/tagger/tree/master/dataset). Make sure to convert the original tagging schema to the standard BIO (or more advanced BIOES). Here is the code I used to convert it to BIO:

```python
def transform(ifile, ofile):
	with open(ifile, 'r') as reader, open(ofile, 'w') as writer:
		prev = 'O'
		for line in reader:
			line = line.strip()
			if len(line) == 0:
				prev = 'O'
				writer.write('\n')
				continue

			tokens = line.split()
			# print tokens
			label = tokens[-1]
			if label != 'O' and label != prev:
				if prev == 'O':
					label = 'B-' + label[2:]
				elif label[2:] != prev[2:]:
					label = 'B-' + label[2:]
				else:
					label = label
			writer.write(" ".join(tokens[:-1]) + " " + label)
			writer.write('\n')
			prev = tokens[-1]
```



## Reference

- model: [CNN-BiLSTM-CRF](https://github.com/XuezheMax/NeuroNLP2) ([paper](http://www.cs.cmu.edu/~xuezhem/publications/P16-1101.pdf))
- dataset: [CoNLL-03](https://github.com/glample/tagger/tree/master/dataset)
- pre-trained word vector: [GloVe](https://nlp.stanford.edu/projects/glove/) (6B)