# Python instagram_parser
### Logic of app:
    1.Stores total number of followers in a text file 'amount.txt'
    2.Requests for number of followers in moment on instagram profile
    3.Compares requested number with total number in amount.txt
    4.If requested number is greater than total, diff = number - total
    5.Makes request to get usernames of last 'diff' followers 

### How to use:
    1.Install dependencies in 'requirements.txt'
    2.Write your username and password in app.py
    3.Run app, check the result in localhost:5000/. For inital request, app just updates the amount.txt file
