# FAQ Bot
python 3.8
conda install pytorch==1.11.0 -c pytorch
pip install transformers
pip install -U sentence-transformers
pip install pandas

## TODO:
- [x] Handle the case below 0.8 (Phuong)
- [ ] Create API for server side (Dang)
- [ ] Front end? 

## Description

- The system answers users' questions about content of a website.
- The system contains a database of Questions and Answers about the website.

## Ideas for solution

- The input questions of users will be mapped to the most similarity question existing in the database.
- The system uses sentence embedding model to encode user's questions to compare with existing questions in the database.
- Set threshole 0.8 to pick answer. if score < 0.8, pass question to general LM to generate answer.

## Data for database
csv file: each row corresponding a pair of question and answer

## Data for fine-tuning sentence embedding model
- [Quora Question Pairs](https://paperswithcode.com/dataset/quora-question-pairs)

## Architecture

- 
