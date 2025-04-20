import unittest
from unittest.mock import patch, MagicMock
import burn

class TestBurnAudio(unittest.TestCase):

    @patch('burn.get_app')
    def test_get_playlists(self, mock_get_app):
        mock_itunes = MagicMock()
        mock_get_app.return_value = mock_itunes
        mock_itunes.user_playlists.return_value = ['Playlist1', 'Playlist2']
        playlists = burn.get_playlists()
        self.assertEqual(playlists, ['Playlist1', 'Playlist2'])

    @patch('burn.get_app')
    def test_list_playlists(self, mock_get_app):
        mock_itunes = MagicMock()
        mock_get_app.return_value = mock_itunes
        mock_itunes.user_playlists.return_value = [MagicMock(name='Playlist1'), MagicMock(name='Playlist2')]
        playlists = burn.list_playlists()
        self.assertEqual(playlists, ['Playlist1', 'Playlist2'])

    @patch('burn.get_app')
    def test_search_playlists(self, mock_get_app):
        mock_itunes = MagicMock()
        mock_get_app.return_value = mock_itunes
        mock_itunes.user_playlists.return_value = [MagicMock(name='Playlist1'), MagicMock(name='Playlist2')]
        self.assertTrue(burn.search_playlists('Playlist1'))
        self.assertFalse(burn.search_playlists('Playlist3'))

    @patch('burn.get_app')
    def test_get_playlist(self, mock_get_app):
        mock_itunes = MagicMock()
        mock_get_app.return_value = mock_itunes
        mock_itunes.user_playlists.return_value = [MagicMock(name='Playlist1'), MagicMock(name='Playlist2')]
        playlist = burn.get_playlist('Playlist1')
        self.assertEqual(playlist.name(), 'Playlist1')

    @patch('burn.get_app')
    def test_get_tracks(self, mock_get_app):
        mock_itunes = MagicMock()
        mock_get_app.return_value = mock_itunes
        mock_playlist = MagicMock()
        mock_get_app.return_value.user_playlists.return_value = [mock_playlist]
        mock_playlist.name.return_value = 'Playlist1'
        mock_playlist.file_tracks.return_value = ['Track1', 'Track2']
        tracks = burn.get_tracks('Playlist1')
        self.assertEqual(tracks, ['Track1', 'Track2'])

    @patch('burn.get_app')
    def test_list_tracks(self, mock_get_app):
        mock_itunes = MagicMock()
        mock_get_app.return_value = mock_itunes
        mock_playlist = MagicMock()
        mock_get_app.return_value.user_playlists.return_value = [mock_playlist]
        mock_playlist.name.return_value = 'Playlist1'
        mock_playlist.file_tracks.return_value = [MagicMock(name='Track1'), MagicMock(name='Track2')]
        tracks = burn.list_tracks('Playlist1')
        self.assertEqual(tracks, ['Track1', 'Track2'])

    def test_is_track_transcodeable(self):
        self.assertTrue(burn.is_track_transcodeable('Purchased AAC audio file'))
        self.assertFalse(burn.is_track_transcodeable('MPEG audio file'))

    @patch('burn.os.path.isfile')
    def test_get_track_abspath(self, mock_isfile):
        mock_track = MagicMock()
        mock_track.location().path = '/path/to/track'
        mock_isfile.return_value = True
        self.assertEqual(burn.get_track_abspath(mock_track), '/path/to/track')

        mock_isfile.return_value = False
        with self.assertRaises(burn.TrackNotFound):
            burn.get_track_abspath(mock_track)

if __name__ == '__main__':
    unittest.main()
