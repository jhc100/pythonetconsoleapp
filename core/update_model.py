from transformers import AutoTokenizer, AutoModel
from MLpipeline import SentenceEmbeddingPipeline

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
)

model_path = 'model/'
model_name = 'sentence-transformers/all-mpnet-base-v2'

logging.info("Extracting model: " + model_name)

try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    logging.info("The model has been succesfully downloaded")

    embedding_encoder = SentenceEmbeddingPipeline(model=model, tokenizer=tokenizer)

    logging.info("Storing model in " + model_path)
    embedding_encoder.save_pretrained(model_path)

except:
    logging.error("Sorry, the NLP model was not found")

