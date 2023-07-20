from enum import Enum

class DiscHolderState(Enum):
    CLOSED = 1
    OPEN = 2

class DiscPlacedState(Enum):
    EMPTY = 1
    PLACED = 2

class SongPlayState(Enum):
    SILENT = 1
    PLAYING = 2

class MusicPlayer:
    def __init__(self):
        self.disc_holder_state = DiscHolderState.CLOSED
        self.disc_placed_state = DiscPlacedState.EMPTY
        self.song_play_state = SongPlayState.SILENT

        # supporting state for disc_placed_state
        self.song_list = []

        # supporting states for song_play_state
        self.playing_song = 0
        self.paused = False

    def __str__(self):
        result = ""
        result += "DiscHolder -- " + str(self.disc_holder_state) + "\n"
        result += "DiscPlaced -- " + str(self.disc_placed_state) + "\n"
        result += "SongPlay -- " + str(self.song_play_state) + "\n"
        result += "SongList -- " + str(self.song_list)
        if self.playing_song > 0:
            result += "\n" + "PlayingSong -- " + self.song_list[self.playing_song - 1] + "\n"
            result += "SongPaused -- " + "Yes" if self.paused else "No"
        return result

    def _isEmpty(self):
        return self.disc_placed_state == DiscPlacedState.EMPTY

    def _isPlaced(self):
        return self.disc_placed_state == DiscPlacedState.PLACED

    def _isPlaying(self):
        return self.song_play_state == SongPlayState.PLAYING

    def _isSilent(self):
        return self.song_play_state == SongPlayState.SILENT

    def _isClosed(self):
        return self.disc_holder_state == DiscHolderState.CLOSED

    def _isOpen(self):
        return self.disc_holder_state == DiscHolderState.OPEN

    # if its PLAYING then it is also CLOSED and PLACED

    def _isClosedAndPlaced(self):
        return self._isClosed() and self._isPlaced()

    # if its SILENT, it can be CLOSED and PLACED, CLOSED and EMPTY, OPEN and PLACED, OPEN and EMPTY

    def _isClosedAndEmpty(self):
        return self._isClosed() and self._isEmpty()

    def _isOpenAndPlaced(self):
        return self._isOpen() and self._isPlaced()

    def _isOpenAndEmpty(self):
        return self._isOpen() and self._isEmpty()

    # to OPEN the disc holder which is CLOSED, it cannot be OPEN if it is PLAYING

    def eject(self):
        print("ejecting..")

        if (not self._isPlaying()) and self._isClosed():
            self.disc_holder_state = DiscHolderState.OPEN
            return

        raise Exception("Operation Not Supported.")

    # to CLOSE the disc holder which is OPEN

    def load(self):
        print("loading..")

        if self._isOpen():
            self.disc_holder_state = DiscHolderState.CLOSED
            return

        raise Exception("Operation Not Supported.")

    # only when its OPEN and EMPTY a disc can be PLACED,
    # it also brings in the list of songs support state

    def place(self, songs):
        print("placing..")

        if self._isOpenAndEmpty():
            self.disc_placed_state = DiscPlacedState.PLACED
            self.song_list = songs
            return

        raise Exception("Operation Not Supported.")

    # only when its OPEN and PLACED a disc can be EMPTIED
    # it also resets the list of songs support state

    def remove(self):
        print("removing..")

        if self._isOpenAndPlaced():
            self.disc_placed_state = DiscPlacedState.EMPTY
            self.song_list = []
            return

        raise Exception("Operation Not Supported.")

    # play puts the SILENT player into PLAYING state, silent does the reverse
    # when its PLAYING there is always a playing song selected
    # play also unpauses an already PLAYING but paused player

    def play(self):
        print("playing..")

        if self._isClosedAndPlaced() and self._isSilent():
            self.song_play_state = SongPlayState.PLAYING
            if not (len(self.song_list) >= 1):
                raise Exception("No songs to play.")
            self.playing_song = 1
            return

        if self._isPlaying() and self.paused:
            self.paused = False
            return

        raise Exception("Operation Not Supported.")

    def silent(self):
        print("silencing..")

        if self._isPlaying():
            self.song_play_state = SongPlayState.SILENT
            self.playing_song = 0
            self.paused = False
            return

        raise Exception("Operation Not Supported.")

    # pause, go forward, go backward can only happen when the player is PLAYING

    def pause(self):
        print("pausing..")

        if self._isPlaying() and not self.paused:
            self.paused = True
            return

        raise Exception("Operation Not Supported.")

    def go_forward(self):
        print("going forward..")

        if self._isPlaying():
            if self.paused:
                self._play()
            self.playing_song = ((self.playing_song % len(self.song_list)) + 1)
            return

        raise Exception("Operation Not Supported.")

    def go_backward(self):
        print("going backward..")

        if self._isPlaying():
            if self.paused:
                self._play()
            self.playing_song = ((((self.playing_song - 2) + len(self.song_list)) % len(self.song_list)) + 1)
            return

        raise Exception("Operation Not Supported.")

try:
    player = MusicPlayer()
    print(player)
    print()
    player.eject()
    print(player)
    print()
    player.load()
    print(player)
    print()
    player.eject()
    print(player)
    print()
    player.place(["old sunday", "broken hearts"])
    print(player)
    print()
    player.remove()
    print(player)
    print()
    player.place(["good sunday", "little hearts"])
    print(player)
    print()
    player.load()
    print(player)
    print()
    player.play()
    print(player)
    print()
    player.go_backward()
    print(player)
    print()
    player.go_forward()
    print(player)
    print()
    player.pause()
    print(player)
    print()
    player.silent()
    print(player)
    print()
    player.play()
    print(player)
    print()
    player.silent()
    print(player)
    print()
    player.eject()
    print(player)
    print()
    player.remove()
    print(player)
    print()
    player.place(["good sunday", "little hearts", "work like a boss", "make your mind", "untouchable"])
    print(player)
    print()
    player.load()
    print(player)
    print()
    player.play()
    print(player)
    print()
    player.go_backward()
    print(player)
    print()
    player.go_backward()
    print(player)
    print()
    player.go_backward()
    print(player)
    print()
    player.go_backward()
    print(player)
    print()
    player.go_backward()
    print(player)
    print()
    player.go_backward()
    print(player)
    print()
    player.go_backward()
    print(player)
    print()
    player.go_backward()
    print(player)
    print()
    player.go_forward()
    print(player)
    print()
    player.go_forward()
    print(player)
    print()
    player.go_forward()
    print(player)
    print()
    player.go_forward()
    print(player)
    print()
    player.go_forward()
    print(player)
    print()
    player.go_forward()
    print(player)
    print()
    player.go_forward()
    print(player)
    print()
    player.go_forward()
    print(player)
    print()
    player.go_forward()
    print(player)
    print()
    player.go_forward()
    print(player)
    print()
except Exception as e:
    print(e)
