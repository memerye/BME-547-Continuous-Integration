# Unit Testing and Continuous Integration

## Background
With the transition towards electronic medical records, many paper records are being scanned into a digital format.  [Optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition)
(OCR) is used so that the scanned text is searchable.  Depending on the quality of the paper records (often derived from faxes), the quality of the OCR result may not be perfect.  Therefore, any code that is looking to interpret the scanned results needs to be flexible enough to read results that may be slightly off.   

Tachycardia is a heart rate that exceeds the normal resting heart rate. In this assignment, you will be writing a function that could be used to interpret whether a string obtained from OCR of medical records contains the word **"tachycardic"**. 

## Function Specifications
* The function is named as `is_tachycardic` and located in a module called `tachycardia.py`.
* It takes a single word string argument as input, and recgnize if it contains the word **"tachycardic"**. For example, **"ooooops tachycardic"** contains the word.
* The word in the string can be upper case, lower case, mixed case, or have leading / trailing spaces or punctuation. For example, **" TACHYCARDIC", "tachy, cardic", "tachycardic  ."** should all be considered as the word **"tachycardic"**.
* The function is tolerant to close representations of the word **"tachycardic"**. It can tolerate at most 2 mistakes inside the word, including missing letters, inserting letters, and mistaking letters. The cases above like space or punctuation will not considered as mistakes. For example, **",tachcadic"** (missing two letters), **"tachy cord1c"** (mistaking two letters) and **"tarchyQcardic"** (inserting two letters) are all considered as the word **"tachycardic"**.
* The function should return a value of `True` if the string meets the standard above. Otherwise, the function should return a value of `False`.
* Function follows the PEP-8 style guide.

## How to use
* Install the required functions in the `requitements.txt` with the following command: 
`pip install -r requirements.txt`
* Ensure the existence of the files named `tachycardia.py` and `test_tachycardia.py`. Run the command `pytest -v` in your bash window. It will automatically test the function `is_tachycardic` in `tachycardia.py`. If all pass, we are expected to see the following output.
```
====================================== test session starts =======================================
platform darwin -- Python 3.6.8, pytest-5.1.3, py-1.8.0, pluggy-0.13.0 -- /Users/liangyu/Documents/BME/BME547/Homework/unit-testing-ci-memerye/myvenv/bin/python
cachedir: .pytest_cache
rootdir: /Users/liangyu/Documents/BME/BME547/Homework/unit-testing-ci-memerye
plugins: pep8-1.0.6
collected 8 items                                                                                

test_tachycardia.py::test_is_tachycardic[tachycardic-True] PASSED                          [ 12%]
test_tachycardia.py::test_is_tachycardic[ taCHyca. rdic-True] PASSED                       [ 25%]
test_tachycardia.py::test_is_tachycardic[Tach?ycardic ...-True] PASSED                     [ 37%]
test_tachycardia.py::test_is_tachycardic[tchycardic-True] PASSED                           [ 50%]
test_tachycardia.py::test_is_tachycardic[tachyQcardic-True] PASSED                         [ 62%]
test_tachycardia.py::test_is_tachycardic[t0chycard1c-True] PASSED                          [ 75%]
test_tachycardia.py::test_is_tachycardic[t0chycrd1c-False] PASSED                          [ 87%]
test_tachycardia.py::test_is_tachycardic[ooooops Tachycardic,-True] PASSED                 [100%]

======================================= 8 passed in 0.06s ========================================
```
* You can also change the testing strings in the `test_tachycardia.py` and re-run the pytest command.

### Reference
https://github.com/dward2/BME547/blob/master/Assignments/UnitTestingCIAssignment.md






