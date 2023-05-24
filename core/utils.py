"""
Vectoring Review Support Functions
Author: Luis Esteban Barranco Guida
Company: Softtek
"""

import logging
import numpy as np
import Levenshtein as lev

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
)

def cosine_sim(vector_a, vector_b):
    """
    Implementation of Cosine Similarity using numpy native methods.

    Input:
    - vector_a: First Vector
    - vector_b: Second Vector

    Output:
    - cosine: Cosine Similarity between the two input vectors
    """
    #logging.info("Executing Cosine Similarity between a & b calculation...")
    vector_a = vector_a[0].numpy()
    vector_b = vector_b[0].numpy()
    #logging.info(f"a shape: %s", vector_a.shape)
    #logging.info(f"b shape: %s", vector_b.shape)
    cosine = np.dot(vector_a, vector_b) / \
        (np.linalg.norm(vector_a) * np.linalg.norm(vector_b))
    return cosine

def are_identical(string_a, string_b):
    """
    Function designed to calculate the Levenshtein distance among two strings and
    return a flag with a value of True if the Levenshtein distance is 0, if the 
    reader wants to increase the knowledge about this calculation please refer to:
    https://en.wikipedia.org/wiki/Levenshtein_distance

    Input:
    - string_a
    - string_b

    Output:
    - Flag: True if they are identical, False Otherwise
    """
    #logging.info("Calculating Levenshtein distance between both questions")
    flag = False
    dist = lev.distance(string_a, string_b)
    
    if dist == 0:
        flag = True
        
    return flag


def semantic_sim(input_questions, embedding_encoder):
    """
    Function designed to calculate the Embedding asociated with each question
    and calculate their similarity.

    Input:
    - input_questions: The two questions contained inside the request send to the API

    Output:
    - output: Semantic similarity between the two questions
    """
    questions_dict = input_questions.__dict__
    logging.info("Questions received:")
    logging.info(questions_dict)

    flag = are_identical(questions_dict["question_a"], questions_dict["question_b"])

    if flag == False:
        embedding_a = embedding_encoder(questions_dict["question_a"])
        embedding_b = embedding_encoder(questions_dict["question_b"])

        cosine = cosine_sim(embedding_a, embedding_b)

    else:
        embedding_a = None
        embedding_b = None
        cosine = 1.0

    output = dict()

    output['A'] = {
        'Item': questions_dict["question_a"],
        'embedding': embedding_a}
    output['B'] = {
        'Item': questions_dict["question_b"],
        'embedding': embedding_b}
    output['Similitude'] = cosine

    logging.info("Cosine similarity: %s", output["Similitude"])

    return output
