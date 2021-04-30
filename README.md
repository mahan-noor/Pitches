# Author
* Ismahan Abey

## Description
* This is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application.

## installation
1. cloning the repo https://github.com/mahan-noor/Pitches.git

2. move to the folder and also install whats in the requirements
   * cd pitches
   * pip install -r requirements.txt

3. exporting configuration
  * export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

4. running the app
   * python3.8 manage.py server

5. app in the browser
   * http://127.0.0.1:5000/

## User Story
  * Register to be allowed to log in to the application
  * View pitches from the different categories.
  * Submit a pitch to a specific category of their choice.
  * Comment on the different pitches posted py other uses.
  * See the pitches posted by other uses.
  * Vote on A pitch they have viwed by giving it a upvote or a downvote.


## Technology used
   * Python3.8
   * Flask
   * Heroku

## Known bugs
  * There are no known bugs currently but pull requests are allowed incase you spot a bug
## Contact info
 * if you have any query email me at ismahanabey@gmail.com
 ## Licence
  * MIT LICENCE
  * Copyright (c) 2021 Ismahan Abey
