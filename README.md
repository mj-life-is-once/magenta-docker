# Magenta Docker Compose

- This is a docker-compose implementation of [Magenta](https://magenta.tensorflow.org/) Based on [xychelsea's repo](https://github.com/xychelsea/magenta-docker).
- Tested with MacOS Ventura 13.5.1(Intel), Docker version 4.22.1

## How to Run

1. Clone this repo

```
git clone git@github.com:mj-life-is-once/magenta-docker.git
```

2. Navigate to the project root directory
3. Run docker-compose

```
docker-compose up -d
```

4. Run generation commands in docker. There are several options to run the command.

- With docker exec

  ```
  sudo docker exec -it magenta /bin/bash

  # Run example command
  melody_rnn_generate \
    --config=lookback_rnn \
    --bundle_file=/home/anaconda/magenta/models/lookback_rnn.mag \
    --output_dir=/home/anaconda/workspace/generated/lookback_rnn\
    --num_outputs=10 \
    --num_steps=128 \
    --primer_melody="[60]"
  ```

- User Portainer

1. Open `localhost:9000`
2. Run bash in magenta container
3. Run the example command

```
  melody_rnn_generate \
    --config=lookback_rnn \
    --bundle_file=/home/anaconda/magenta/models/lookback_rnn.mag \
    --output_dir=/home/anaconda/workspace/generated/lookback_rnn\
    --num_outputs=10 \
    --num_steps=128 \
    --primer_melody="[60]"
```

8. Alternatively, you can directly run command through docker CLI

```
docker exec melody_rnn_generate \
    --config=lookback_rnn \
    --bundle_file=/home/anaconda/magenta/models/lookback_rnn.mag \
    --output_dir=/home/anaconda/workspace/generated/lookback_rnn\
    --num_outputs=10 \
    --num_steps=128 \
    --primer_melody="[60]"

```

# List of example commands

## melodyRNNGenerate

```
melody_rnn_generate \
 --config=lookback_rnn \
 --bundle_file=/home/anaconda/magenta/models/lookback_rnn.mag \
 --output_dir=/home/anaconda/workspace/generated/lookback_rnn\
 --num_outputs=10 \
 --num_steps=128 \
 --primer_melody="[60]"
```

# polyphonyRNN

```
polyphony_rnn_generate \
--bundle_file=/home/anaconda/workspace/models/polyphony_rnn.mag \
--output_dir=/home/anaconda/workspace/generated/polyphony_rnn \
--num_outputs=1 \
--num_steps=128 \
--primer_melody="[60, -2, -2, -2, 60, -2, -2, -2, "\
"67, -2, -2, -2, 67, -2, -2, -2, 69, -2, -2, -2, "\
"69, -2, -2, -2, 67, -2, -2, -2, -2, -2, -2, -2]" \
--condition_on_primer=false \
--inject_primer_during_generation=true
```
