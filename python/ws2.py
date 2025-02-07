from tornado.websocket import websocket_connect
def on_message( msg ):
    print(f"[In on message] {msg}")
ws = await websocket_connect("ws://localhost:3060/ws",
  on_message_callback=on_message)
await ws.write_message("coucou")
await ws.write_message("byebye")
await ws.write_message("vive la MMC")
