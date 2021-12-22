# Scripting & environments

## Python
```bash
python3 -m venv <venv_name>
source venv/bin/activate
```


## conda
### Search and find packages
```bash
conda search <package_name>
```
All packages are listed [here](https://docs.anaconda.com/anaconda/packages/pkg-docs/)


### Installing and removing packages
Install packages with
```bash
conda install <package_name>
```
or from a specific channel with:
```bash
conda install --channel <channel_name> <package_name>
```
Install package in a specific environment:
```bash
conda install --name <env_name> <package_name>
```

#### Installed packages in current environment
```bash
conda list
```

#### Install directly from PyPI
In an active conda environment you can install PyPI packages using pip as normal
```bash
pip install <package_name>
```


### Create and delete environment
See available environments with:
```bash
conda env list
```
or
```bash
conda info --envs
```
and activate with
```bash
conda activate <env_name>
```

Creating a new environment with:
```bash
conda create --name <env_name>
```
or with a specific python version:
```bash
conda create --name <env_name> python=3.8
```

Delete environment with:
```bash
conda env remove --name <env_name>
```

### Save and share environments
Save the current environment to a text file with
```bash
conda list --explicit > env_name.txt
```
and rebuild the exact environment with 
```bash
conda env create --file env_name.txt
```






