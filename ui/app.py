from typing import List, Generator
import streamlit as st
import requests
import json


url = 'http://localhost:8000'
headers = {'accept': 'application/json'}


st.title('Math Questions')
st.write("1 - Select two different integers (x, y) and get a list of the numbers between x and y that are divisible by 5 but not by 7")
x = st.slider('Select a value for x', value = 0, min_value = 0, max_value = 1000)
y = st.slider('Select a value for y', value = 10, min_value = x, max_value = 1000)

response = requests.post(url+f'/Question1?number_1={x}&number_2={y}', headers=headers)
if response.status_code == 200:
    st.success(','.join([str(x) for x in response.json()['response']]))
else:
    st.warning('Unable to get a succesful response from server')



st.write("3 - Select two different integers (x, b) and x converted into base b")
x2 = st.slider('Select a value for x', value = 7, min_value = 0, max_value = 1000)
y2 = st.slider('Select a value for b', value = 2, min_value = 1, max_value = 9)

response = requests.post(url+f'/Question3?number_1={x2}&number_2={y2}', headers=headers)
if response.status_code == 200:
    st.success(response.json()['response'])
else:
    st.warning('Unable to get a succesful response from server')



st.title('O.O Questions')
st.write("1 - Select a number N and get a list of all the perfect squares less than N")
N = st.slider('Select a value for N', value = 10, min_value = 0, max_value = 1000)

response = requests.post(url+f'/OOQuestion?number={N}', headers=headers)
if response.status_code == 200:
    st.success(','.join([str(x) for x in response.json()['generator']]))
else:
    st.warning('Unable to get a succesful response from server')


st.title('Games')
st.write("""You have a chessboard with only the Rook on it. The Rook can move up, down, left or right from your perspective. 
Write a function (or a class) that takes a series of movements and at the end of the sequence of movements prints two numbers.

Give me a sequence like: up 1, left 3, down 2
And you will get the total distance that the rook was moved, how far is it from the origin (in steps and in euclidean distance).
""")
seq = st.text_input('Enter your sequence for your rook: ', value='up 1, left 3, down 2') 

response = requests.post(url+f'/Rook?sequence={seq}', headers=headers)
if response.status_code == 200:
    st.success('Total Distance:     ' + str(response.json()['distance']))
    st.success('Steps from origin:  ' + str(response.json()['steps']))
    st.success('Euclidean Distance: ' + str(response.json()['euclidean']))
else:
    st.warning('Unable to get a succesful response from server')


st.title('Files')
st.write("""1- Enter a text and a phrase or word in the next textboxes, and you will be able
to know if the phrase is in the text.
""")
text = st.text_input('Enter the text: ', value='''But I particularly remember one wild, snowy afternoon, soon after my return in January: the children had all come up from dinner, loudly declaring that they meant "to be naughty," and they had well kept their resolution, though I had talked myself hoarse, and wearied every muscle in my throat, in the vain attempt to reason them out of it. I had got Tom pinned up in a corner, whence, I told him, he should not escape till he had done his appointed task. Meantime, Fanny had possessed herself of my work-bag, and was rifling its contents—and spitting into it besides. I told her to let it alone, but to no purpose, of course.''') 

phrase = st.text_input('Enter the phrase/word: ', value='''and they had well kept''') 

response = requests.post(url+f'/SearchInText?phrase={phrase}&text={text}', headers=headers)
if response.status_code == 200:
    st.success(response.json()['Matches?'])
else:
    st.warning('Unable to get a succesful response from server')

st.write("""2- Given the file testfile.csv which contains:
1, 2, 3, 4
5, 6, 7, 8
9, 10, 11, 12

Enter a number of column (0-4) and get sum.
""")
column = st.slider('Select your column', value = 0, min_value = 0, max_value = 3)

response = requests.post(url+f'/CSVFile?csv_file=challenges/tests/testfile.csv&column={column}', headers=headers)
if response.status_code == 200:
    st.success(response.json()['sum'])
else:
    st.warning('Unable to get a succesful response from server')