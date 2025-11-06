from pypresence import Presence
import time


CLIENT_ID = "1435943038223650937"

def DiscordRpcThread(Options):
    while True:
        try:
            presence = Presence(CLIENT_ID)
            presence.connect()
            updated = False
            while True:
                if Options.get("EnableDiscordRPC", False):
                    if not updated:
                        try:
                            presence.update(
                                details="NexWare - CS2 External",            
                                start=int(time.time()),         
                                large_image="nixware_image",   
                                large_text="Made by C00leHu"           
                            )
                        except Exception as e:
                            pass
                    updated = True
                    time.sleep(1)
                else:
                    time.sleep(1)
        except:
            time.sleep(30)
