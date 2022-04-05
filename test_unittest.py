import unittest
import src.JSONconverter
import src.translator


class TestCalc(unittest.TestCase):

    def test_getDictFromList_array(self):
        self.strArr = [(9, 'Bob Klose', 'lead guitarist of an early rock band that would later become Pink Floyd'),
                       (12, 'Eminem', 'American rapper, songwriter, and record producer')]
        self.assertEqual(src.JSONconverter.getDictFromList(self.strArr), [{'artist_id': 9, 'artist_name': 'Bob Klose', 'artist_info': 'lead guitarist of an early rock band that would later become Pink Floyd'},
                                                                          {'artist_id': 12, 'artist_name': 'Eminem', 'artist_info': 'American rapper, songwriter, and record producer'}])

    def test_getDictFromList_singleArtist(self):
        self.str = [
            (9, 'Bob Klose', 'lead guitarist of an early rock band that would later become Pink Floyd')]
        self.assertEqual(src.JSONconverter.getDictFromList(self.str), [
                         {'artist_id': 9, 'artist_name': 'Bob Klose', 'artist_info': 'lead guitarist of an early rock band that would later become Pink Floyd'}])

    def test_getDictFromList_singleSong(self):
        self.str = [('Astronomy Domine', "Lime and limpid green, a second scene\nNow fights between the blue you once knew\nFloating down, the sound resounds\nAround the icy waters underground\nJupiter and Saturn, Oberon, Miranda and Titania\nNeptune, Titan, stars can frighten\nBlinding signs flap,\nFlicker, flicker, flicker blam, pow, pow\nStairway scare, Dan Dare, who's there?\nLime and limpid green, the sounds around\nThe icy waters under\nLime and limpid green, the sounds around\nThe icy waters underground\n", 1967, 'ENG')]
        self.assertEqual(src.JSONconverter.getDictFromList(self.str), [{'song_name': 'Astronomy Domine', 'song_text': "Lime and limpid green, a second scene\nNow fights between the blue you once knew\nFloating down, the sound resounds\nAround the icy waters underground\nJupiter and Saturn, Oberon, Miranda and Titania\nNeptune, Titan, stars can frighten\nBlinding signs flap,\nFlicker, flicker, flicker blam, pow, pow\nStairway scare, Dan Dare, who's there?\nLime and limpid green, the sounds around\nThe icy waters under\nLime and limpid green, the sounds around\nThe icy waters underground\n", 'song_year': 1967, 'original_lang': 'ENG'}])

    def test_getDictFromList_singleAlbum(self):
        self.str = [('Electric Ladyland', 1968,
                     "final studio album released in Hendrix's lifetime before his death")]
        self.assertEqual(src.JSONconverter.getDictFromList(self.str), [
                         {'album_name': 'Electric Ladyland', 'album_year': 1968, 'album_info': "final studio album released in Hendrix's lifetime before his death"}])

    def getJSONFromList(self):
        self.str = [('Electric Ladyland', 1968,
                     "final studio album released in Hendrix's lifetime before his death")]
        self.assertEqual(src.JSONconverter.getJSONFromList(self.str)), [
            {"album_name": "Electric Ladyland", "album_year": 1968, "album_info": "final studio album released in Hendrix's lifetime before his death"}]

    def getTranslation(self):
        self.strForTranslate = '''Ticking away the moments that make up a dull day
                                    Fritter and waste the hours in an offhand way
                                    Kicking around on a piece of ground in your hometown
                                    Waiting for someone or something to show you the way'''
        self.sourceLang = 'en'
        self.targetLang = 'ru'
        self.assertEqual(src.translator.getTranslation(self.strForTranslate, self.sourceLang, self.targetLang), '''Отмечая моменты, которые составляют скучный день
                                                                                                                   Оладьи и тратить часы навскидку
                                                                                                                   Пинать на куске земли в вашем родном городе
                                                                                                                   Ожидание кого-то или чего-то, чтобы показать вам путь''')


if __name__ == '__main__':
    unittest.main()
