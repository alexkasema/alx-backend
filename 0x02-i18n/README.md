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
