python main.py \
    --model CNNBLSTM \
    --train_data data-LSTM-CRF/CoNLL-03-eng/eng.train.bio.conll \
    --test_data data-LSTM-CRF/CoNLL-03-eng/eng.test.bio.conll \
    --valid_data data-LSTM-CRF/CoNLL-03-eng/eng.dev.bio.conll \
    --emb_file data-LSTM-CRF/GloVe/glove.6B.100d.txt \
    --lr 0.005 \
    --fine_tuning False \
    --eval_test True \
    --l2_reg 0.0002 \
    --log True

    # --log_dir LOG_DIR \
    # --model_dir MODEL_DIR \
    # --output_dir OUTPUT_DIR \

    # --restore_model RESTORE_MODEL \
    # --only_test [ONLY_TEST] \
    
    # --emb_dim EMB_DIM \
    # --dropout DROPOUT_RATE \
    # --max_len MAX_LEN \
    # --nb_classes NB_CLASSES \
    # --hidden_dim HIDDEN_DIM \
    # --batch_size BATCH_SIZE \
    # --train_steps TRAIN_STEPS \
    # --display_step DISPLAY_STEP \
    # --template TEMPLATE \
    # --window WINDOW \
    # --feat_thresh FEAT_THRESH \