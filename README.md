# NER-for-QA4IE

## Things to Do

- ~~prepare datasets~~
- train models
    - sequence-tagging
    - LSTM-CRF => wrong data format for word2vec
    - CNN-BiLSTM-CRF => segment fault
- infer on QA4IE benchmark
    - data processing
    - without POS and chunk tagging
    - with POS and chunk tagging

## Interface



## Reference

- model: [sequence-tagging](https://github.com/guillaumegenthial/sequence_tagging)
- model: [LSTM-CRF](https://github.com/heshenghuan/LSTM-CRF)
- model: [CNN-BiLSTM-CRF](https://github.com/XuezheMax/NeuroNLP2) ([paper](http://www.cs.cmu.edu/~xuezhem/publications/P16-1101.pdf))
- dataset: [CoNLL-03-eng](https://github.com/glample/tagger/tree/master/dataset)
- pre-trained word vector: [GloVe](https://nlp.stanford.edu/projects/glove/) (6B.100d)