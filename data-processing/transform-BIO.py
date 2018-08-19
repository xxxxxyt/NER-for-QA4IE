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
				counter = 0
				continue
			else:
				counter = counter + 1

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
			writer.write(str(counter) + " " + " ".join(tokens[:-1]) + " " + label)
			writer.write('\n')
			prev = tokens[-1]

# eng.train => eng.train.bioes.conll
ifs = "english/eng.train"
ofs = "english/eng.train.bioes.conll"
transform(ifs, ofs)
# eng.testa => eng.dev.bioes.conll
ifs = "english/eng.testa"
ofs = "english/eng.dev.bioes.conll"
transform(ifs, ofs)
# eng.testb => eng.test.bioes.conll
ifs = "english/eng.testb"
ofs = "english/eng.test.bioes.conll"
transform(ifs, ofs)