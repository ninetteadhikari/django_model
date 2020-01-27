## Available Scripts

In the directory, you can run:

```bash
#Installs pipenv
pip3 install pipenv
```
```bash
#Creates virtual environment
pipenv shell
```
```bash
#Installs all dependencies
pipenv install
```
```bash
#Runs server
python manage.py runserver
```
```bash
#Runs migrations
python manage.py migrate
```

## Create ERD

Remove existing erd.dot and erd.png files and install pyparsing and pydot

```bash
pip3 install pyparsing pydot
```
In the app directory run the following:
```bash
python manage.py graph_models -a > erd.dot
python manage.py graph_models -a > erd.dot && python manage.py graph_models --pydot -a -g -o erd.png
```