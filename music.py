from rubpy import filters, Client
from rubpy.types import Update
import requests as r
app = Client('h_o')

@app.on_message_updates(filters.is_group)
async def random_music(m:Update):
    if m.text == "موزیک":
            if m.author_guid :
                url = r.get("https://api-free.ir/api/music").json()
                name,link = url["result"]["title"], url["result"]["song"]
                
                await m.reply(f"""

**name music**: {name} 

**download music**: {link}

""")
                
                
app.run()