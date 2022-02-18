# diaryProject
-----
## How to Use?

1. `fork` the project
2. clone using command line(make sure git is installed)
```
git clone url
```
3. In `Command line` or `Terminal` run `python` and copy paste the below code and `run`
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
4. You will get a random digits as output. `Copy` the output
5. create file name `secret.py inside diaryProject folder`
6. `paste` the output in `THE-OUPUT-HERE` and copy paste the below code inside `secret.py`
```python
SECRET_KEY = 'THE-OUTPUT-HERE'
```
7. Run migrations in `CMD` from `To Do` Folder
```
python manage.py makemigrations
python manage.py migrate
```
For Mac and Linux
```
python3 manage.py makemigrations
python3 manage.py migrate
```
8. `Run the project`
```
python manage.py runserver
```
for Mac and Linux
```
python3 manage.py runserver
```
