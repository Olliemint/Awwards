# Awwards
  Site link https://netawwards.herokuapp.com/



### By: Oliver Maiyo

## APIs Endpoints
[Projects](https://netawwards.herokuapp.com/api/project/)<br>
[Users](https://netawwards.herokuapp.com/api/user/)<br> 
[Profiles](https://netawwards.herokuapp.com/api/profile/)<br> 



### Screenshot of the App

<img src="https://raw.githubusercontent.com/Olliemint/Awwards/main/media/awwwardslanding.png">

## Table of Content

- [Description](#description)
- [User Stories](#user-stories)
- [Installation Requirement](#usage)
- [Technology Used](#technologies)
- [Licence](#licence)
- [Authors Info](#author-info)

## Description
This an website that shows users site, allow users to create account and submit their sites , it also allow users to review and rate other users site

## User Stories

The user is able to;

- Sign in or register to submit or rate a project

- Post a project to be rated/reviewed

- Rate/ review other users' projects

- Search for projects 

- View projects overall score
- View my profile page

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

These are the things you need to install the software and how to install them

```
virtual enviroment:

$ clonenv

or

$ python3 -m venv virtual ( or your selected virtual enviroment name )
```

### 1. Local Repository

- Make sure you have a stable internet to have the ability to clone the repository.
- Type the following command in your terminal to clone this repository

```
git clone https://github.com/Olliemint/Awwards.git

```



When you run the commands successfully, you should have a local version of this repository.

### 2. Online Repository

- Make sure you have a stable internet for forking this repository.
- According to the license, you can fork this project. You need to click on the forking icon and it will be added as one of your repositories

Feel free to fork the project and have fun with it. Happy coding!

### Installing

To get a development env running, you simply need the install all the packages reguired from either a requirements.txt file or a pipfile. First you need to activate your virtual environment

```
$clonenv

of

$ source virtualenvname/bin/activate
```

after that, install all the required depencencies

```
$ pipenv install //pretty much takes care of installing all depencies for you
```

After this, you can run the application using the commands that come in the make file. for this case, it is either of the following:

```
$ make

or

$ make run

or

$ python manage.py runserver

```

## Running the tests

If you want to run tests for the entire project, you need only run this command:

```
$ make test

or

$ python manage.py test
```

## Technologies


- JavaScript
- Django

## Licence

Copyright (c) Olliemint - [MIT Licence](LICENSE)

## Author Info

- Twitter - [@K-720](@Furymint)
