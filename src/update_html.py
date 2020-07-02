from utils import *


def dict_to_html(rank: dict) -> str:
    i = 0
    result = ""
    for uuid, value in rank.items():
        i += 1
        result += "{:>3}位: {:>16}: {}<br>\n".format(i, uuid_to_name(uuid), value)
    return result

def create_html(contents: str, title: str, path: str) -> str:
    html = """
    <html>
    <head>
    <meta charset="UTF-8">
    <title>整地ランキング</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/marx/2.0.4/marx.css">
    </head>

    <body>
    <div>
        <p>MENU:</p>
        <ul>
            <li><a href="./index.html">30分整地量ランキング</a></li>
            <li><a href="./daily.html">日間整地量ランキング</a></li>
            <li><a href="./weekly.html">週間整地量ランキング</a></li>
            <li><a href="./monthly.html">月間整地量ランキング</a></li>
        </ul>
    </div>
    <main>
        <h1> """ + title + """ </h1>
        <p>""" + contents + """
    </p>
    </main>
    </body>
    </html>
    """
    
    with open(path, mode='w') as f:
        f.write(html)
        
    return 

min30_html = 'index.html'
daily_html = 'daily.html'
weekly_html = 'weekly.html'
monthly_html = 'monthly.html'

create_html(min30_rank(), "30分整地量ランキング", min30_html)
create_html(daily_rank(), "日間整地量ランキング", daily_html)
create_html(weekly_rank(), "週間整地量ランキング", weekly_html)
create_html(monthly_rank(), "月間整地量ランキング", monthly_html)
