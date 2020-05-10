from textgenrnn import textgenrnn
textgen = textgenrnn(weights_path='compliments_weights.hdf5',
                       vocab_path='compliments_vocab.json',
                       config_path='compliments_config.json')

textgen.generate_samples(max_gen_length=1000)
textgen.generate_to_file('textgenrnn_texts.txt', max_gen_length=1000)