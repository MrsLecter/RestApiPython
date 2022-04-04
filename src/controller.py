import cherrypy
import os
from src import db_managing
from src import JSONconverter
from src import translator

#/artist
class ArtistsPage:
    @cherrypy.expose
    def index(self):
        return f"""
            <p>All artists page</p>
            <hr>
            <p>"This is a list of all artists: "</p>
            <p>{JSONconverter.getJSONFromList(db_managing.getItems('artists'))}
            <p>You are here --> '/artist/' </p>
            <p>Choose your page: <p>
            <p>[<a href="/artist/Bob%20Klose">Show <u>[Bob Klose]</u> artist page</a>]
            <p>[<a href="/artist/Eminem">Show <u>[Eminem]</u> artist page</a>]
            <p>[<a href="/artist/George%20Harrison">Show <u>[George Harrison]</u> artist page</a>]
            <p>[<a href="/artist/Jimi%20Hendrix">Show <u>[Jimi Hendrix]</u> artist page</a>]
            <p>[<a href="/artist/John%20Lennon">Show <u>[John Lennon]</u> artist page</a>]
            <hr>
            <p>[<a href="../">Return home</a>]</p>"""


    # /artist/<artist>
    @cherrypy.expose
    def current(self, current):
        artist_url = current.replace(' ', '%20')
        urls = [f'/artist/{artist_url}/songs', f'/artist/{artist_url}/albums']
        print("current:", cherrypy.request.params['current'])
        return f"""
            <p>Current artist page</p>
            <hr>
            <p><a href={urls[0]}>Show all songs current artist</a></p>
            <p><a href={urls[1]}>Show all albums current artist</a></p>
            <p>{JSONconverter.getJSONFromList(db_managing.getItems('artists', current))}</p>
            <p>You are here --> '/artist/current' </p>
            <hr>
            <p>[<a href="../artist/">Go to all artist page</a>]</p>
            <p>[<a href="../">Return home</a>]</p>"""
        


# /artist/<artist>/song
class AllSongsPage:
    @cherrypy.expose
    def songs(self, current):
        return f"""
            <p>All songs page</p>
            <hr>
            <p>"This is a list of all songs current artist: "</p>
            <p>{JSONconverter.getJSONFromList(db_managing.getSongsForArtist(current))}</p>
            
            <p>You are here --> '/artist/current/songs' </p>
            <p>Go to current song...</p>
            <p>/input song</p>
            <hr>
            <p>[<a href="../../">Go back</a>]</p>
            <p>[<a href="../">Return home</a>]</p>"""


    # /artist/<artist>/song/<song>
    @cherrypy.expose
    def currentsong(self, current, currentsong):
        return f"""
                <p>Current song page</p>
                <hr>
                <p>"This is a list of current song current artist"</p>
                <p>{JSONconverter.getJSONFromList(db_managing.getCurrentSongForArtist(current, currentsong))}</p>            
                <p>Translated text(en -> ru)</p>
                <p>{translator.getTranslation(db_managing.getCurrentTextSongForArtist(current, currentsong)[0][0], 'en', 'ru')}</p>
                <p>You are here --> '/artist/current/songs' </p>
                <hr>
                <p>[<a href="../../../artist/">Go to all artist page</a>]</p>
                <p>[<a href="../../../artist/current/">Go to current artist page</a>]</p>
                <p>[<a href="../artist/current/songs/>Go to all songs</a>]</p>''
                <p>[<a href="../">Return home</a>]</p>"""


class AllAlbumsPage:
    @cherrypy.expose
    def albums(self, current):
        return f"""
            <p>All albums page</p>
            <hr>
            <p>"This is a list of all albums current artist: "</p>
            <p>[<a href="/artist/current/albums/currentalbum">Show all songs current artist current album</a>]
            <p>{JSONconverter.getJSONFromList(db_managing.getAlbumsForArtist(current))}
            <p>You are here --> '/artist/current/song' </p>
            <hr>
            <p>[<a href="../../../artist/">Go to all artist page</a>]</p>
            <p>[<a href="../../../artist/current/">Go to current artist page</a>]</p>
            <p>[<a href="../">Return home</a>]</p>"""


    # /artist/<artist>/song/<song>
    @cherrypy.expose
    def currentalbum(self,current, currentalbum):
        return f"""
                <p>Current artist page</p>
                <hr>
                <p>"This is a list of current song current artist"</p>
                <p>{JSONconverter.getJSONFromList(db_managing.getCurrentAlbumForAlbumsForArtist(current, currentalbum))}
                <p>You are here --> '/artist/current/song' </p>
                <hr>  
                <p>[<a href="../../../artist/">Go to all artist page</a>]</p>
                <p>[<a href="../../../artist/current/">Go to current artist page</a>]</p>
                <p>[<a href="../artist/current/song/>Go to all songs</a>]</p>''
                <p>[<a href="../">Return home</a>]</p>"""


class SearchPage:
    @cherrypy.expose
    def index(self):
        return f"""
            <p>Search page</p>
            <hr>
            <p>/input here/</p>
            <p>You are here --> '/search/' </p>
            <p>Maybe you want to search <u>['item_name']</u> in <u>[table_name]</u> storage?</p>
            <p>[<a href="/search/John%20Lennon%20artists">Go to search <u>['John Lennon']</u> in <u>[artists]</u> storage</a>]</p>
            <p>[<a href="/search/Revolver%20albums">Go to search <u>['Revolver']</u> in <u>[albums]</u> storage</a>]</p>
            <p>[<a href="/search/Echoes%20songs">Go to search <u>['Echoes']</u> in <u>[songs]</u> storage</a>]</p>
            <hr>
            <p>[<a href="../">Return home</a>]</p>"""


    # /artist/<artist>
    @cherrypy.expose
    def searchable(self, searchable):
        return f"""
            <p>Search page</p>
            <hr>
            <p>You looking for {searchable.split(' ')[len(searchable.split(' '))-2]} in {searchable.split(' ')[len(searchable.split(' '))-1]}</p>
            <p>Search result: </p>
            <p>{JSONconverter.getJSONFromList(db_managing.searchItems(searchable.split(' ')[len(searchable.split(' '))-1], searchable.split(' ')[len(searchable.split(' '))-2]))}</p>         
            <hr>
            <p>[<a href="../search/">Go to search page</a>]</p>
            <p>[<a href="../">Return home</a>]</p>"""


# /
class Router:
    def __init__(self):

        self.artists_page = ArtistsPage()
        self.search_page = SearchPage()
        self.artists_page.all_songs_page = AllSongsPage()
        self.all_songs_page = AllSongsPage()
        self.all_albums_page = AllAlbumsPage()

    @cherrypy.expose
    def index(self):
        return """
            <p>Home page! </p>
            <hr>
            <p>You are here --> '/' </p>
            <ul>
                <li><a href="/artist">Show all artist</a></li>
                <li><a href="/search">Show search page</a></li>
            </ul>"""

    def _cp_dispatch(self, vpath):
        if len(vpath) == 1:
            if vpath[0] == 'search':
                return self.search_page
            elif vpath[0] == 'artist':
                return self.artists_page
        elif len(vpath) == 2:
            print('2 vpath', vpath)
            if vpath[0] == 'search':
                vpath.pop(0)
                cherrypy.request.params['searchable'] = vpath.pop(0)
                return self.search_page.searchable
            elif vpath[0] == 'artist':
                vpath.pop(0)
                cherrypy.request.params['current'] = vpath.pop(0)
                return self.artists_page.current
        elif len(vpath) == 3:
            vpath.pop(0)  # delete artist
            cherrypy.request.params['current'] = vpath.pop(0)
            if vpath[0] == 'songs':
                return self.all_songs_page
            elif vpath[0] == 'albums':
                return self.all_albums_page
        elif len(vpath) == 4:
            print(vpath)
            vpath.pop(0)
            cherrypy.request.params['current'] = vpath.pop(0)
            print(vpath)
            if vpath[0] == 'songs':
                vpath.pop(0)
                print(vpath)
                cherrypy.request.params['currentsong'] = vpath.pop(0)
                return self.all_songs_page.currentsong
            elif vpath[0] == 'albums':
                vpath.pop(0)
                print(vpath)
                cherrypy.request.params['currentalbum'] = vpath.pop(0)  
                return self.all_albums_page.currentalbum
            
        else:
            return "incorrect input"
