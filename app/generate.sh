#!/bin/bash

sudo docker exec magenta polyphony_rnn_generate \
--bundle_file=/home/anaconda/workspace/models/polyphony_rnn.mag \
--output_dir=/home/anaconda/workspace/generated/polyphony_rnn \
--num_outputs=1 \
--num_steps=128 \
--primer_melody="[60, -2, -2, -2, 60, -2, -2, -2, "\
"67, -2, -2, -2, 67, -2, -2, -2, 69, -2, -2, -2, "\
"69, -2, -2, -2, 67, -2, -2, -2, -2, -2, -2, -2]" \
--condition_on_primer=false \
--inject_primer_during_generation=true