"""
Vectoring Review Support Functions
Author: Luis Esteban Barranco Guida
Company: Softtek
"""

import numpy as np

from transformers import AutoTokenizer, AutoModel
from MLpipeline import SentenceEmbeddingPipeline


def cosine_sim(vector_a, vector_b):
    """
    Implementation of Cosine Similarity using numpy native methods.

    Input:
    - vector_a: First Vector
    - vector_b: Second Vector

    Output:
    - cosine: Cosine Similarity between the two input vectors
    """
    vector_a = vector_a[0].numpy()
    vector_b = vector_b[0].numpy()

    cosine = np.dot(vector_a, vector_b) / \
        (np.linalg.norm(vector_a) * np.linalg.norm(vector_b))
    return cosine


def semantic_sim(question_A, question_B):
    """
    Function designed to calculate the Embedding asociated with each question
    and calculate their similarity.

    Input:
    - input_questions: The two questions contained inside the request send to the API

    Output:
    - output: Semantic similarity between the two questions
    """
    try:
        model = AutoModel.from_pretrained('model/', local_files_only=True)
        tokenizer = AutoTokenizer.from_pretrained('model/', local_diles_only=True)
        embedding_encoder = SentenceEmbeddingPipeline(model=model, tokenizer=tokenizer)
        print("The model has been succesfully loaded")

    except:
        embedding_encoder = None
        print("Sorry, the model was not found in model/")

    embedding_a = embedding_encoder(question_A)
    embedding_b = embedding_encoder(question_B)

    cosine = cosine_sim(embedding_a, embedding_b)

    output = dict()

    output['A'] = {
        'Item': question_A,
        'embedding': embedding_a}
    output['B'] = {
        'Item': question_B,
        'embedding': embedding_b}
    output['Similitude'] = cosine

    print("Cosine similarity: %s", output["Similitude"])

    return output
