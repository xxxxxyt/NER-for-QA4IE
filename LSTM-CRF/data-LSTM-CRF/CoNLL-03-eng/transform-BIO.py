import os

def transform(ifile, ofile):
	counter = 0
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
			writer.write(tokens[0] + ' ' + label)
			writer.write('\n')
			prev = tokens[-1]

# eng.train => eng.train.bio.conll
ifs = "eng.train"
ofs = "eng.train.bio.conll"
transform(ifs, ofs)
# eng.testa => eng.dev.bio.conll
ifs = "eng.testa"
ofs = "eng.dev.bio.conll"
transform(ifs, ofs)
# eng.testb => eng.test.bio.conll
ifs = "eng.testb"
ofs = "eng.test.bio.conll"
transform(ifs, ofs)