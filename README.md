# FAQ Bot

## Description

- The system answers users' questions about content of a website.
- The system contains a database of Questions and Answers about the website.

## Ideas for solution

- The input questions of users will be mapped to the most similarity question existing in the database.
- The system uses sentence embedding model to encode user's questions to compare with existing questions in the database.

## Data for database
csv file: each row corresponding a pair of question and answer

## Data for fine-tuning sentence embedding model
- [Quora Question Pairs](https://paperswithcode.com/dataset/quora-question-pairs)

## Architecture

- 
