# Internationalization and localization
* In computing, internationalization and localization (American) or internationalisation and localisation (British), often abbreviated i18n and l10n respectively, are means of adapting computer software to different languages, regional peculiarities and technical requirements of a target locale.

* Internationalization is the process of designing a software application so that it can be adapted to various languages and regions without engineering changes.
* Localization is the process of adapting internationalized software for a specific region or language by translating text and adding locale-specific components.
## 0-app.py, templates/0-index.html
Basic Flask app
First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title and “Hello world” as header.
## 1-app.py, templates/1-index.html
Install the Babel Flask extension:

$ pip3 install flask_babel==2.0.0
Then instantiate the Babel object in your app. Store it in a module-level variable named babel.

In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and timezone ("UTC").

Use that class as config for your Flask app.
## 2-app.py, templates/2-index.html
Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.
## 4-app.py, templates/4-index.html
In this task, you will implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs.

In your get_locale function, detect if the incoming request contains locale argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting http://127.0.0.1:5000?locale=[fr|en].
## 5-app.py, templates/5-index.html
Mock logging in
Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in 5-app.py.

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
This will mock a database user table. Logging in will be mocked by passing login_as URL parameter containing the user ID to log in as.

Define a get_user function that returns a user dictionary or None if the ID cannot be found or if login_as was not passed.

Define a before_request function and use the app.before_request decorator to make it be executed before all other functions. before_request should use get_user to find a user if any, and set it as a global on flask.g.user.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

msgid	English	French
logged_in_as	"You are logged in as %(username)s."	"Vous êtes connecté en tant que %(username)s."
not_logged_in	"You are not logged in."	"Vous n'êtes pas connecté."
