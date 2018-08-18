# NER-for-QA4IE

## Things to Do

- prepare datasets
    - word2vec pre-trained embedding
- train models
    - LSTM-CRF
    - CNN-BiLSTM-CRF => segment fault
- infer on QA4IE benchmark
    - interface
    - without POS and chunk tagging
    - with POS and chunk tagging

## Interface



## Reference

- model: [LSTM-CRF](https://github.com/heshenghuan/LSTM-CRF)
- model: [CNN-BiLSTM-CRF](https://github.com/XuezheMax/NeuroNLP2) ([paper](http://www.cs.cmu.edu/~xuezhem/publications/P16-1101.pdf))
- dataset: [CoNLL-03-eng](https://github.com/glample/tagger/tree/master/dataset)
- pre-trained word vector: [GloVe](https://nlp.stanford.edu/projects/glove/) (6B.100d)