## Solubility workshop

### Setup
Prerequisites: Python 3.8.xx - 3.11.xx 


Check python version ```python --version``` or ```python3 --version```

[Install python if needed](https://www.python.org/downloads/) 

Run commands with `python3` or `python` if depending which command above gives satisfactory version output.


Create a new folder

Download files to folder:
[requirements.txt](https://github.com/elonheimo/keminformatiikka/blob/main/solubility_workshop/requirements.txt),
[Solubility model](https://github.com/elonheimo/keminformatiikka/raw/main/solubility_workshop/WaterSoulubility_03_01_2024_model.pkl),
[solubility_predictor](https://github.com/elonheimo/keminformatiikka/blob/main/solubility_workshop/solubility_predictor.ipynb)
[chem_util.py](https://github.com/elonheimo/keminformatiikka/blob/main/solubility_workshop/chem_util.py)

Run all commands under new created folder with the files

Create virtual environment:
```python3 -m venv ./venv```

Enter virtual environment:

Linux/Mac: ```source venv/bin/activate```

Windows cmd: ```venv\Scripts\activate```

Install required packages (will take a few minutes):
```pip install -r requirements.txt```

Open jyputer notebook (command should open jupyter in browser):
```python3 -m notebook```

Open `solubility_predictor.ipynb` in jupyter and follow instructions within notebook