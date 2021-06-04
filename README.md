This work is based on Visual Genome dataset. The webpage of the project can be found here: https://visualgenome.org/ 

You can get the objects.json data in .csv by first running parse_objects.py. The following notebooks (notebooks example folder) are based on this format.

Our goal is to represent images based on their region descriptions in natural languages and apply this approach on a variety of tasks. 
Region descriptions per image are encoded in vector space using state of the art pre-trained NLP models such as BERT sentence embeddings. 
Sentence embeddings are extracted using SentenceTransformers Python framework for state-of-the-art sentence, text and image embeddings.
5 different techniques were attempted, based on the provided documentation of sentence transformers:  
- bert-base-nli-mean-tokens
- paraphrase-mpnet-base-v2
- paraphrase-distilroberta-base-v2
- stsb-mpnet-base-v2
- stsb-roberta-large

For more information please check: https://www.sbert.net/ and https://www.sbert.net/docs/pretrained_models.html.
The calculated embeddings per sentence are averaged in order to represent each image as a whole.

K-means clustering algorithm is used to group together similar images based on their averaged sentence embedding representations. 
A 2D visualization of the clusters produced reveals the embeddings placement, revealing images containing some semantic similarity, when placed in the same cluster or
closely, while semantically different images are found to be far from one another. 

This semantic similarity is proved useful in the task of image retrieval. The first approach is to provide an image id and retrieve the k most similar images
based on the embedding proximity, which is calculated in the multi-dimensional space using Euclidean distance. 
Another approach receives a user defined input sentence in natural language, which aims to describe an image present in the dataset.
This sentence is encoded similar to the region sentences, and the k most relevant images comparing to the given description are returned.

The images returned from both approaches are visually similar to the given image id or user sentence respectively. Our approach is able to successfully capture
relevant semantic features on images even when ambiguous or non well-defined input sentences are provided, as far as relevant images indeed exist in the dataset.

