from fastapi import FastAPI
import os
os.environ['TRANSFORMERS_CACHE'] = '../../huggingface_cache/model_cache'
os.environ['HF_DATASETS_CACHE'] = '../../huggingface_cache/data_cache'


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/{question}")
def handle_question(question: str):
    return {'answer': "My name is Phuong."}