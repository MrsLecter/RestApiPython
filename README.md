## About

Simple REST API

## Technology

- cherrypy
- SQL

## Before running commands from the command line, you must:

- Install postgreSQL, cherrypy
- Clone a repository using git

## Live demo

https://mrslecter.github.io/RestApiPython/

## API path

* **GET** '/artist' or '/artist/${artistName}' returns all atrists or artist with the required 'artistName';
          'artist/{artistName}/song' returns all songs for current artist;
          'artist/{artistName}/song/${songName} returns required 'songName' for current 'artistName';
* **POST** '/artist' or '/artist/${artistName}/song is used to create record about new artist and store it in database (you must pass all the required fields described below to successfully complete the request)
* **PUT** '/artist/${artistName}' or 'artist/{artistName}/song/${songName}' is used to update record about existing artist (you must pass all the required fields described below to successfully complete the request)
* **DELETE** '/artist/${artistName}'  or '/artist/${artistName}/song/${songName}' is used to delete record about existing artist from database
</code>

## Artists and Songs are stored as objects that have following properties:
* id - unique identifier (`string`, `uuid`) generated on server side;
* artist_name
* album_name, album_year, album_info
* song_name, song_text, song_year, origin_lang

<h4>Downloading</h4>
<code>git clone {repository URL}</code>


