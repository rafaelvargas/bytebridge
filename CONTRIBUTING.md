

# Contribution Guidelines


## Setting up the development environment

The build system used in this project is [Flit](https://flit.pypa.io/en/stable/), thus, you need to have it installed in order to set up the development environment. The steps for setting up the environment are the following:


### Create a virtual environment

```
python -m venv env
```

### Activate the virtual environemnt


#### Linux/Mac OS
```
source ./env/bin/activate
```

#### Windows - Powershell
```
.\env\Scripts\Activate.ps1
```

### Upgrade the pip version
```
pip install --upgrade pip
```

### Install the dev depencencies
```
pip install -e '.[dev]'
```