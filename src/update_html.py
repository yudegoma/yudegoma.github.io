from utils import *


def dict_to_html(rank: dict) -> str:
    i = 0
    result = ""
    for uuid, value in rank.items():
        i += 1
        result += "{:>3}位: {:>16}: {}<br>\n".format(i, uuid_to_name(uuid), value)
    return result

def create_html(contents: str) -> str:
    html = """
    <html>
    <head>
    <meta charset="UTF-8">
    <title>整地ランキング</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/marx/2.0.4/marx.css">
    </head>

    <body>
    <main>
      <h1>30分整地量</h1>
      <p>""" + contents + """
    </p>
    </main>
    </body>
    </html>
    """
    return 

min30 = 'index.html'

with open(min30, mode='w') as f:
    f.write(create_html(dict_to_html(min30_rank())))
