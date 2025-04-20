BurnAudio
---------

A small python script which I use to burn MP3 CDs from my iTunes AAC playlists. It estimates (badly) the size of the burn so you don't waste time. 

There are lots of improvements that could be made, but it works well enough for my needs. Please feel free to fork and if you add anything useful please submit those changes back!

Changes in the latest version:
- Replaced `print` statements with `logging` module for logging.
- Made paths and commands for `FAAD` and `LAME` configurable.
- Improved exception handling for better error management.
- Allowed the number of processes in the multiprocessing pool to be configurable.
- Provided a user-friendly interface for selecting playlists and tracks.
- Added unit tests for better maintainability.
- Updated code to be compatible with Python 3.11.
