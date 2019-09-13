# PyDS
Notebooks, data, and examples supporting the Python for Data Science videos

# Setup
Most of the files should be runnable with the package versions listed in the requirements.txt file. 

I recommend you first create an environment for just your PyDS runs. E.g. in a terminal:

### Using Conda:
```
conda create --name pyds
conda activate pyds
conda install --file requirements.txt
```

More information:
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

### Using virtualenv:
```
py -m venv pyds
.\pyds\Scripts\activate
pip install -r requirements.txt
```

More information:
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/