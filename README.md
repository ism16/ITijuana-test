# ITijuana-test
Coding challenge for ITijuana

This repo host the solutions for the coding challenge. Besides the questions, an api has been setup along with a minimal UI using streamlit. 
As in every professional project, unit tests have been included, and also a jenkinsfile (jenkins instance at k0dark.com:8080 runs static analysis and runs all pytests testcases on every commit). 

# Setup

If you want to setup the complete solution, it is strongly recommended to create a python virtual environment:

  ```
  python3 -m venv .venv
  ```
  
Activate your environment and install requirements:

```
source .venv\bin\activate
python3 -m pip install -U pip
pip install - r requirements.txt
```
You can run pytest testcases as:
```
pytest
```

And mypy static analysis as:
 ```
 mypy file1 file2 folder
 ```

# Challenges
Solutions to the questions can be found in challenges folder, they are divided in the same four sections as in the document (math questions, questions, games and files).

You can verify its correctness via pytest, but you can also call every script and give certain arguments.

For math.py there are three different functions that can be run:

```
python challenges\math.py question_1 2 100
python challenges\math.py question_2 2 10 
python challenges\math.py question_3 2 10 
```

For questions.py there are only one option and can be run as:

```
python challenges\questions.py 30  
```

For games.py enter the desired sequence:

```
python challenges\games.py "up1, down 2"
```

For files.py:
```
python challenges\files.py question_1 "test" "this is a simple test for these python scripts" 
python challenges\files.py question_2 "challenges/tests/testfile.csv" 2  
```

# API

An API that interacts with the content at the challenges folders has been setup, and make these modules available for other applications.

```
k0dark.com:8082/docs
```

# UI

Streamlit was used for quickly prototyping a UI, you can run it in your local setup as:

```
streamlit run ui\app.py
```

Or you can access online at:

```
k0dark.com:8501
```


