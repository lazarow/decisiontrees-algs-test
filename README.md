# Decision Trees Algorithms Test

## Introduction

## How to run the code?

### Step 0
_(Optional)_ Installation of the `virtualenv` if you don't have it already. Install it globally.
```
pip install virtualenv
```

### Step 1
Clone this repository and step into a created folder.
```
git clone https://github.com/lazarow/decisiontrees-algs-test.git
cd decisiontrees-algs-test
```

### Step 2
Create an virtual environment with `virtualenv`.
```
virtualenv .
```
Some folders and files will be created. Now, activate the virtual environment.
```
source bin/activate     # for linux
Scripts\activate.bat    # for windows
```

### Step 3
Install required libraries. It has to be done once only, the environment will store downloaded libraries.
```
pip install -r requirements.txt
```

### Step 4
Run the tests.
```
python run.py
```
The generated models will be saved into the `models` folder. Beware, re-run of the scripts will use saved models an test them against test sets only.
In order to re-do all experiments, please clear the `models` folder.

On the standard output you will find the results output. See the example below.
```
-------------------------
Experiment ID: tic-tac-toe
-------------------------
Algorithm: ID3
ID3  tree is going to be built...
-------------------------
finished in  4.0019001960754395  seconds
-------------------------
Evaluate  train set
-------------------------
Accuracy:  100.0 % on  383  instances
Labels:  ['negative' 'positive']
Confusion matrix:  [[139, 0], [0, 244]]
Precision:  100.0 %, Recall:  100.0 %, F1:  100.0 %
-------------------------
Evaluate  validation set
-------------------------
Accuracy:  84.02777777777777 % on  288  instances
Labels:  ['positive' 'negative']
Confusion matrix:  [[174, 26], [20, 68]]
Precision:  87.0 %, Recall:  89.6907 %, F1:  88.3249 %
-------------------------
Evaluate  test set
-------------------------
Accuracy:  82.92682926829268 % on  287  instances
Labels:  ['negative' 'positive']
Confusion matrix:  [[74, 24], [25, 164]]
Precision:  75.5102 %, Recall:  74.7475 %, F1:  75.1269 %
{"positive", "positive"} => 164,
{"negative", "negative"} => 74,
{"negative", "positive"} => 25,
{"positive", "negative"} => 24

...
```

### Pre-generated results

You will find all generated results in two files: `output_full.txt` and `output_test_only.txt`. The former consist a complete procedure, whereas the latter consists validation of test sets only.

### Clean up
Deactivate the virtual environment or just close the terminal.
```
source bin/deactivate     # for linux
Scripts\deactivate.bat    # for windows
```
