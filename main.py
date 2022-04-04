import cherrypy
import os
from src import controller


# way for pages and classes
root = controller.Router()
root.search_apge = controller.SearchPage()
root.artists_page = controller.ArtistsPage()
root.artists_page.all_songs_page = controller.AllSongsPage()
root.all_songs_page = controller.AllSongsPage()
root.all_albums_page = controller.AllAlbumsPage()

# way to package configuration
pakage_conf = os.path.join(os.path.dirname(__file__), "package_conf.conf")

if __name__ == "__main__":
    # choose start page
    cherrypy.quickstart(controller.Router(), config=pakage_conf)
