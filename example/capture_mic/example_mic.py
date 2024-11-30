from pyrogram import Client

from pytgcalls_hikka import idle
from pytgcalls_hikka import PyTgCalls
from pytgcalls_hikka.media_devices import MediaDevices
from pytgcalls_hikka.types import MediaStream

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
        MediaDevices.get_audio_devices()[0],
    ),
)
idle()
