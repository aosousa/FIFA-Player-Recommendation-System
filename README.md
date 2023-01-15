# FIFA Player Recommendation System
Machine learning system to recommend FIFA players based on similar characteristics.

## Tech Stack

* [Python](https://www.python.org/)
    * [Scikit-Learn](https://scikit-learn.org/)
    * [Flask](https://flask.palletsprojects.com/en/2.2.x/)
    * [Psycopg](https://www.psycopg.org/)
    * [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
* [PostgreSQL](https://www.postgresql.org/)

### Package/Module setup fix

Due to the project being set up as a reusable package with its respective modules (e.g. db, server in the modules folder), this can lead to a **ModuleNotFoundError** (No module named 'fifa_player_recommendation_system') when running the ```$ python main.py``` command on a Windows environment. To fix this, run the following command in the terminal before running ```$ python main.py```:

```
$ set PYTHONPATH=%PYTHONPATH%;<path\to\the\project\folder>
```

Example:

```
set PYTHONPATH=%PYTHONPATH%;C:\Users\andre\Documents\Projects\FIFA-Player-Recommendation-System
```