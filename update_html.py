from utils import *


def dict_to_html_str(rank: dict) -> str:
    i = 0
    result = ""
    for uuid, value in rank.items():
        i += 1
        result += "{}位: {:>16}: {}<br>".format(i, uuid_to_name(uuid), value)
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
  <h1>ここになんか書く</h1>
  <p>
""" + dict_to_html_str(daily_rank()) + """
</p>
</main>
</body>
</html>
"""

with open(path_w, mode='w') as f:
    f.write(html)
    
