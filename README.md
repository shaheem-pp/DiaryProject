# DiaryProject  <img src="https://media3.giphy.com/media/3oKGzvg3gGxSS3O38A/giphy.gif?cid=ecf05e471mbq13b45htuitku9ca5rk6k9d94sarxaadpcl3z&rid=giphy.gif&ct=g" width="30px"/>


<h1>
  Hey there! Looking for a cool diary app? Well, you've come to the right place.
  Introducing My_Daybook, a personalised diary app to record all your favourite memories.
 </h1>
<div align="center">
  <img src="https://media0.giphy.com/media/ktEr4Ax4Kci6ESDQkZ/giphy.gif?cid=ecf05e4776vy7e9j929bxqgun2t58dldfbqqmk8x2pjm30ul&rid=giphy.gif&ct=g" width="600" height="300"/>
</div>

  
---

### :man_technologist: About The Diary App :
- :book: The project is to make a simple app with an authorisation page, a new user registeration page and a main content page where one can add,edit or delete existing entries.

- :seedling: used various technologies like django and python.

- :zap: Done by Shaheem PP and Riya Mary Jude.
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
