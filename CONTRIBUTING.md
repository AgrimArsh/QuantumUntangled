# Contributing 
All contributions to this project should be made through pull requests, these will be evaluated and further changes will be required if necessary. If you want to report a bug, suggest changes or propose features, start an issue detailing the situation with as much detail as you can, and please include if you want/can work on that.

For commit messages, please follow this format: `fix typos`, `add 'Title Example' article`, etc. This format being:

- Write in all lowercases
- Titles, authors, etc. should go in uppercase and within single quotes
- File names should be written exactly the same as found on the repository
- Use present tense
- Give a good and short description of changes

## Virtual environment
To keep the python version and packages used in this project without interfering with other versions of the same packages or programs, using a virtual environment is advised. To set up a virtual environment with python, read [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html).

## Database
To run the project in your local machine, you will probably need to set up a local database (which will be independent of that used for production). To do this, run the following commands inside the `website` folder.

```
python manage.py makemigrations
python manage.py migrate
```

After running this, the website should work without any problems.

Since the project is built using Django, some knowledge of python and Django is required. If you are comfortable with python but not with Django, it is recommended that you watch [this series](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p). If you are not comfortable with python yet, there are a lot of online resources to learn this language that it is hard to choose the best one, but one good resource is [learnpython.org](https://www.learnpython.org).
