# Python instagram_parser
### Logic of app:
    1.Stores total number of followers in a global variable TOTAL
    2.Requests for number of followers in moment on instagram profile
    3.Compares requested number with total number of followers
    4.If requested number is greater than TOTAL, diff = number - TOTAL
    5.Makes request to get usernames of last 'diff' followers 

### How to use:
    1.Install dependencies in 'requirements.txt'
    2.Write your username and password in enviroment variables
    3.Run app, check the result in localhost:5000/. For inital request, app just initializes TOTAL variable
