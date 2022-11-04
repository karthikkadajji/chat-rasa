Add your Token and channel ID 

Run the command:

pip install -r requirements.txt

rasa train
rasa run actions
rasa run -m models --enable-api --cors "*" --debug --endpoints endpoints.yml

when we enter word "world" in slack, the bot will automatically give thumbsup