# Workout-Tracker
This program will help you track your workout sessions

For this program to work you will need to use the Nutritionix API and the Sheety API. ( here you will get the App Id, API key and the token from the sheety API)
First, you will have to log in to your google spreadsheet account and make a copy of the My Workouts.xlsx file that I uploaded.
Then you will have to sign in to your sheety API account using the same google account that you have used for the google spreadsheet account.
After that, click on "New Project" icon in the Sheety API to create a new project and select "from Google Sheet", and you will have to paste your url from
the google spreadsheet that you created with the My Workout template. 

Make sure that the "post" request is enabled in the sheety API -> go to API and click on the workouts (it will be named the same if you didn't change the name of the spreadsheet) button and then enable the "post" request

Go to Authentication in the sheety API and select bearer (Token) type and create your own token.
Your token will be something like that: Bearer d1e1wd1ufndufsd8332rmfd!@$@dsa  (you have to copy the "Bearer" word too, otherwise it will not work)




