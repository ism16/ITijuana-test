from typing import List, Generator
from fastapi import FastAPI

import os, sys

from starlette.requests import Request;
sys.path.append(os.path.split(os.path.dirname(os.path.realpath( __file__ )))[0])

from challenges.math import *  # type: ignore
from challenges.questions import *  # type: ignore
from challenges.games import *  # type: ignore
from challenges.files import *  # type: ignore


app = FastAPI()


# Math questions
@app.post("/Question1")
def read_root(info: Request, number_1: int, number_2: int):
    response: List[int] = question_1(number_1, number_2)
    return {"status": "SUCCESS", "response": response}

@app.post("/Question3")
def read_root(info: Request, number_1: int, number_2: int):
    response: str = question_3(number_1, number_2)
    return {"status": "SUCCESS", "response": response}


# Questions
@app.post("/OOQuestion")
def read_root(info: Request, number: int):
    _generator: Generator = perfect_square_generator(number)
    return {"status": "SUCCESS", "generator": _generator, "numbers": [x for x in perfect_square_generator(30)]}

# Games
@app.post("/Rook")
def read_root(info: Request, sequence: str):
    rook = Rook(sequence)
    return {"status": "SUCCESS", "distance": rook.distance, "steps": rook.steps, "euclidean": rook.euclidean}

# File questions

@app.post("/SearchInText")
def read_root(info: Request, phrase: str, text: str):
    result: bool = search_for_text(phrase, text)
    return {"status": "SUCCESS", "Matches?": result}


@app.post("/CSVFile")
def read_root(info: Request, csv_file: str, column: int):
    csv_file = os.path.join(os.path.split(os.getcwd())[0], csv_file)
    total: int = int(sum_columns_from_csv(csv_file, column))
    return {"status": "SUCCESS", "sum": total}