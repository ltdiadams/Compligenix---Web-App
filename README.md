Compligenix---Web-App
Django web app featuring SMS messaging capabilities

COMPLIGENIX is a web app created using Python's Web Framework Django, it uses a PGSQL (postgres) database and twilio's api acts as the SMS gateway for the app. The app also has an AI component which was created using tensorflow.

What does the app do?

The app is designed to be a simple interface where people can enter a valid phone number and submit, and then receive an AI generated compliment immediately upon subscribing to the service, and then on a daily basis after that! Currently upon entering your phone number, the app runs the 'create_model' program and creates an AI-generated compliment in the text file 'textgenrnn_texts'. (AI portion from following along with tensorflow interactive demo at: https://colab.research.google.com/drive/1mMKGnVxirJnqDViH7BDJxFqWrsXlPSoK) the contents of the text file become the body of the message for twilio to send to the number you've entered. Finally, the phone number is stored in a postgres database and soon there will be another program which sends a message to the numbers stored in this database on a daily basis!

If you have a twilio account and django installed you can test this on your localhost now, but it will be hosted eventually :)