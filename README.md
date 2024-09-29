# Text Based Adventure Game

## Before getting started we need to do some setup
This python application will be run in a virtual environment (venv) in the terminal. A venv is a mini virtual computer within your own creating an isolated environment where regardless of your computers confirgurations, downloads or settings it will run the same on all machines producing the same result.   
When installing libraries like we are today ti will also isolate it to our current working directory, to not affect the other projects on your machine by installing them globally.

## Creating the virtual environment
First we need to create the virtual environment, then we need to activate it.

1. Create your project folder and open it in your code editor of choice.

2. Open the terminal in your current directory.

3. Enter the following command, where 'python3' represents your current version of python:

```
python3 -m venv ./venv
```

4. Once created you will have new folders created in your project folder, now we need to activate it with the following command:

```
source venv/bin/activate
```

## package download 
Now that we have our virtual environment created let's download pickle.

1. If your on python 3.8 or newer pickle is preinstalled. To check your version enter the following into your terminal:

```
python --version
```

2. If you're currently on version 3.8 or higher simply enter the following command into your file:

```python
import pickle
```

3. If you're on an older version of python (3.5, 3.6, 3.7) enter the following into your terminal:

```
pip install pickle5
```

4. Once package has downloaded successfully enter the following into your file:  
 - (pickle5 is to utilise the newest version of pickle. Not neccessery for 3.8 or newer)

```python
import pickle5 as pickle
```


## Legal and ethical impacts of pickle 

Pickle is an open source data serilisation and deserilisation software library of python.

### license
- GNU Lesser General Public License v3 or later (LGPLv3+)  
This is a free open source software license. This means any work created under it also holds its license, both original and modified versions. This allows there to transprancy and freedom of use while still being open source and accessable to everyone.