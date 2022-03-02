# Daybook📕

Greetings!

Do you want to keep an interesting journal?
You've arrived to the right place.

**Daybook** is a personalised diary writing online software that allows you to keep track of all your favourite experiences.
Simply log in and select Add New Diary to start a new diary for the day.

The goal of the project is to create a basic app that includes an authorisation page, a new user registration page, and a primary content page where users may add, amend, or remove existing entries and you can write the Diary with *Markdown*.
utilised a variety of technologies such as django and python. The project is done by Riya Mary Jude and Shaheem PP

![GIF](https://media0.giphy.com/media/ktEr4Ax4Kci6ESDQkZ/giphy.gif?cid=ecf05e4776vy7e9j929bxqgun2t58dldfbqqmk8x2pjm30ul&rid=giphy.gif&ct=g)

-----

## Team ID Python/312
## Watch [Video Walkthrough of the Project](https://www.loom.com/share/88e35c0cde8a445db9e54f89632b5f21)
## Take a look at our [Website](https://daybook312.azurewebsites.net)
## Team Members

| **Name** | **GitHub ID** |
| --- | ----------- |
| Riya Mary Jude | [Link](https://github.com/Riyajude) |
| Shaheem PP | [Link](https://github.com/shaheem-pp) |

-----

## How it Works?

1. Login and Registration are done by Django Inbuilt Authentication System.
2. When you register your data is save in SQLite3 Data base.
3. When Login you are authenticated by Django Itself.
4. After authenticatiton and logged in you can see the memories you added to your DayBook.
5. Upper Right corner you can see Add New Diary button and Sign Out button.
6. You can Add new Diary by clicking New Diary button and you can use Markdown to add new Diary entry.
7. Date is automatically added.
8. When You submit your New Diary, your data stored in Database with your user id, which automatically made by django itself while you register.
9. In diary home page you can only see memories inserted by you by using the user id, we filter out the diary entries by you to show only your diary entries.
10. Logout to go to login page.
  
---

## How to Run and Configure?

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

-----

## Libraries Used

- Django - Framework(Version 4.0.1)
- Markdown - For Markdown Editor
- Django Auth - For Authentication
- SQLite3 - As Database
- Azure Hosting

-----

**This project is done as part of TinkerHub Co-Coder Event**
