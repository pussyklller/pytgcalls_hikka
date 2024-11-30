from pyrogram import Client

from pytgcalls_hikka import idle
from pytgcalls_hikka import PyTgCalls
from pytgcalls_hikka.types import AudioQuality
from pytgcalls_hikka.types import MediaStream
from pytgcalls_hikka.types import VideoQuality

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()
call_py.play(
    -1001234567890,
    MediaStream(
        'https://www.youtube.com/watch?v=msiLgFkXvD8',
        AudioQuality.HIGH,
        VideoQuality.HD_720p,
        ytdlp_parameters='--proxy URL',
    ),
)
idle()
