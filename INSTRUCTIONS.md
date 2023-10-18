## Interacting with Spotify's API

Spotify can be used as a data source for various data science projects. In this exercise, we will learn how to interact with the API of this social network. `Spotipy` is an open source and Python library that allows high-level use of the Spotify API.

### Step 1: Create a Spotify Developer Account
The first step is to create an application to be able to access Spotify's API services. You can find all the information [here](https://developer.spotify.com/documentation/web-api).

Once you have logged in using your Spotify account, you will be able to create the application to access the credentials needed to consume the API. You will need to fill in the following fields:

![Spotify create app](https://github.com/4GeeksAcademy/interacting-with-api-python-project-tutorial/blob/main/assets/spotify_1.PNG?raw=true)

> NOTE: As we are not going to use this API from any other web application, leave the `Redirect URI` field as `http://localhost/`.

Once you complete the form, you will have your application created. Next, in the `settings` section you can find your `Client ID` and `Client Secret`.

### Step 2: Initial configuration

- Create an app.py file inside the `./src/` folder.
- Make sure you have installed the Python library we are going to use, and if not, install it: `pip install spotipy`.

### Step 3: Environment variables

You must provide the Spotify key and token in order to use the API and access its functionality. As we saw in the previous project, you can easily do this by creating a `.env` file in the root directory of your project.

The third step is to create an `.env` file in your project and add your secret keys or passwords:

```py
CLIENT_ID="insert your client key"
CLIENT_SECRET="insert your client secret"
```

> NOTE: Be sure to add the .env inside your .gitignore file, which is not saved in source control, so that you are not putting potentially sensitive information at risk.

Now, you must install python-dotenvpackage. python-dotenvpackage is a Python package that allows your Python application to read an .env file. This package will look for an .env and, if found, expose the variables it contains to the application.

Example:

```py
º
```

### Step 4: Initialize Spotipy library

- Import Spotipy.
- Make the connection to the API. To do this, you can use the `spotipy.Spotify()` function.

> NOTE: Use the following documentation as a guide on parameters: https://spotipy.readthedocs.io/en/2.22.1

### Step 5: Make API requests

- Start interacting with the Spotify API: Get the top 10 of your favorite artist's songs. To do this, you will have to find the `ID` of the artist to use in the library. This identifier is the web address that the artist has in Spotify:

![Spotify search for artist ID](https://github.com/4GeeksAcademy/interacting-with-api-python-project-tutorial/blob/main/assets/spotify_2.png?raw=true)

- Once you have the API response, keep the `tracks` element, which will contain the most played songs of the artist, keep the name of the song, the popularity and the duration (in minutes).

### Step 6: Transform to Pandas DataFrame

Since the result obtained in these steps is likely to be in table format, convert it to a DataFrame by importing the data in its dictionary format. Next, sort the songs by increasing popularity and display the resulting top 3.

### Step 7: Analyze statistical relationship

Does duration have a relationship with popularity? Could we say that a song that lasts a short time may be more popular than a song that lasts longer? Analyze it by plotting a `scatter plot` and argue your answer.