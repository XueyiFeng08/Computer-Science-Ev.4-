import flet as ft
import flet_audio as fta


def main(page: ft.Page):
    page.title = "Music Player"
    page.bgcolor = "#F5F5F5"
    page.window_width = 400
    page.window_height = 500

    songs = [
        {"title": "娱乐世纪", "artist": "汪苏泷", "album": "娱乐世纪", "file": "audio/song1.mp3"},
        {"title": "晴", "artist": "汪苏泷", "album": "Single", "file": "audio/song2.mp3"},
        {"title": "像晴天像雨天", "artist": "汪苏泷", "album": "Single", "file": "audio/song3.mp3"},
        {"title": "苦笑", "artist": "汪苏泷", "album": "慢慢懂", "file": "audio/song4.mp3"},
        {"title": "闪耀", "artist": "汪苏泷", "album": "娱乐世纪", "file": "audio/song5.mp3"},
    ]

    current_song = 0
    is_playing = False
    is_paused = False

    titleText = ft.Text(size=22, weight=ft.FontWeight.BOLD, color="black")
    artistText = ft.Text(size=16, color="black")
    albumText = ft.Text(size=16, color="black")

    audio1 = fta.Audio(src=songs[current_song]["file"])

    def updateSong():
        song = songs[current_song]

        titleText.value = song["title"]
        artistText.value = "Artist: " + song["artist"]
        albumText.value = "Album: " + song["album"]

        audio1.src = song["file"]
        page.update()

    async def playPause(e):
        nonlocal is_playing, is_paused

        if not is_playing:
            await audio1.play()
            is_playing = True
            is_paused = False
        elif is_playing and not is_paused:
            await audio1.pause()
            is_paused = True
        else:
            try:
                await audio1.resume()
            except:
                await audio1.play()
            is_paused = False

        page.update()

    async def nextSong(e):
        nonlocal current_song, is_playing, is_paused

        if current_song == 0:
            current_song = 1
        elif current_song == 1:
            current_song = 2
        elif current_song == 2:
            current_song = 3
        elif current_song == 3:
            current_song = 4
        else:
            current_song = 0

        updateSong()
        await audio1.play()
        is_playing = True
        is_paused = False

    async def previousSong(e):
        nonlocal current_song, is_playing, is_paused

        if current_song == 0:
            current_song = 4
        elif current_song == 4:
            current_song = 3
        elif current_song == 3:
            current_song = 2
        elif current_song == 2:
            current_song = 1
        else:
            current_song = 0

        updateSong()
        await audio1.play()
        is_playing = True
        is_paused = False

    updateSong()

    playPauseButton = ft.ElevatedButton("Play / Pause", on_click=playPause)
    nextButton = ft.ElevatedButton("Next", on_click=nextSong)
    previousButton = ft.ElevatedButton("Previous", on_click=previousSong)

    page.add(
        ft.Column(
            [
                ft.Text("Music Player 0.0", size=32, weight=ft.FontWeight.BOLD, color="black"),

                ft.Container(
                    content=ft.Column(
                        [
                            titleText,
                            artistText,
                            albumText,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=330,
                    padding=25,
                    bgcolor="white",
                    border_radius=20,
                ),

                ft.Row(
                    [
                        previousButton,
                        playPauseButton,
                        nextButton,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
        )
    )


ft.run(main=main, assets_dir="assets")