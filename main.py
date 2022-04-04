import cherrypy
import os.path

# /artist/
class ArtistsPage:
    @cherrypy.expose
    def index(self):
        return """
            <p>"This is a list of all artists: "</p>
            <p>You are here --> '/artist/' </p>
            <p>[<a href="/artist/current">Show current artist page</a>]
            <p>[<a href="../">Return home</a>]</p>"""

    # /artist/<artist>
    @cherrypy.expose
    def current(self):
        return """
            <p>"This is a current artist page"</p>
            <p>[<a href="/artist/current/song">Show all songs current artist</a>]
            
            <p>You are here --> '/artist/current' </p>
            
            <p>[<a href="../artist/">Go to all artist page</a>]</p>
            <p>[<a href="../">Return home</a>]</p>"""


# /artist/<artist>/song
class AllSongsPage:
    @cherrypy.expose
    def index(self):
        return """
            <p>"This is a list of all songs current artist: "</p>
            <p>You are here --> '/artist/current/song' </p>
            
            <ul>
                <li>[<a  href="/artist/current/song/currentsong">Current song </a>]</li>
                <li>[<a  href="/artist/current/song/currentsong">Current song </a>]</li>
                <li>[<a  href="/artist/current/song/currentsong">Current song </a>]</li>
                <li>[<a  href="/artist/current/song/currentsong">Current song </a>]</li>
            </ul>
            
            <p>[<a href="../../../artist/">Go to all artist page</a>]</p>
            <p>[<a href="../../../artist/current/">Go to current artist page</a>]</p>
            <p>[<a href="../">Return home</a>]</p>"""

    # /artist/<artist>/song/<song>
    @cherrypy.expose
    def currentsong(self):
        return """
                <p>"This is a list of current song current artist"</p>
                <p>You are here --> '/artist/current/song' </p>
                                
                <p>[<a href="../../../artist/">Go to all artist page</a>]</p>
                <p>[<a href="../../../artist/current/">Go to current artist page</a>]</p>
                <p>[<a href="../artist/current/song/>Go to all songs</a>]</p>''
                <p>[<a href="../">Return home</a>]</p>"""


# /
class Router:
    def __init__(self):
        self.artists_page = ArtistsPage()
        self.all_songs_page = AllSongsPage()

    @cherrypy.expose
    def index(self):
        return """
            <p>Home page! </p>
            <p>You are here --> '/' </p>
            <ul>
                <li><a href="/artist">Show all artist</a></li>
            </ul>"""

    def _cp_dispatch(self, vpath):
        if len(vpath) == 1:
            return self.artists_page
        elif len(vpath) == 2:
            vpath.pop(0)  # delete artist
            # cherrypy.request.params['artist'] = vpath.pop() # /artist current/
            vpath.pop(0)  # заменить на верхнюю строку
            return self.artists_page.current
        elif len(vpath) == 3:
            vpath.pop(0)  # delete artist
            # cherrypy.request.params['artist'] = vpath.pop() # /artist current/
            vpath.pop(0)  # заменить на верхнюю строку
            vpath.pop(0)
            return self.all_songs_page
        elif len(vpath) == 4:
            vpath.pop(0)  # delete artist
            # cherrypy.request.params['artist'] = vpath.pop() # /artist current/
            vpath.pop(0)  # заменить на верхнюю строку
            vpath.pop(0)
            # cherrypy.request.params['song'] = vpath.pop() # /song current/
            vpath.pop(0)  # заменить на верхнюю строку
            return self.all_songs_page.currentsong
        else:
            return "incorrect input"


root = Router()
root.artists_page = ArtistsPage()
root.all_songs_page = AllSongsPage()


pakage_conf = os.path.join(os.path.dirname(__file__), "package_conf.conf")

if __name__ == "__main__":
    cherrypy.quickstart(Router(), config=pakage_conf)
