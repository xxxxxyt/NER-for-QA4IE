# Run

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

