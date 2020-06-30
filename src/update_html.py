from utils import *


def dict_to_html(rank: dict) -> str:
    i = 0
    result = ""
    for uuid, value in rank.items():
        i += 1
        result += "{:>3}位: {:>16}: {}<br>\n".format(i, uuid_to_name(uuid), value)
    return result


path_w = 'index.html'
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
  <p>""" + dict_to_html(min30_rank()) + """
</p>
</main>
</body>
</html>
"""

with open(path_w, mode='w') as f:
    f.write(html)

with open(path_w, mode='r') as f:
    print(f.read())
