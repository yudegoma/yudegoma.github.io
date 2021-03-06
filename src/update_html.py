from utils import *

def dict_to_html(rank: dict) -> str:
    i = 0
    result = ""
    for uuid, value in rank.items():
        i += 1
        print(i)
        result += "\n<div>\n" \
                  "<img src=\"https://crafatar.com/avatars/" + uuid + "/?size=60&&default=MHF_Steve&helm\">\n \
                    {:>3}位: {:>16}: {:,}<br>\n".format(i, value["name"], value["data"]) +\
                  "</div>"
    return result


def create_html(contents: str, title: str, path: str):
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
            </ul>
        </div>
        <p>イベント:</p>
            <ul>
                <li><a href="./4thAnniv.html">4周年記念整地量ランキング</a></li>
            </ul>
        </div>
        <main>
            <h1> """ + title + """ </h1>
            <p>""" + contents + """ 
            </p>
            Thank you to <a href="https://crafatar.com">Crafatar</a> for providing avatars.
        </main>
    </body>
</html>
    """

    with open(path, mode='w') as f:
        f.write(html)


min30_html = 'index.html'
daily_html = 'daily.html'
weekly_html = 'weekly.html'
monthly_html = 'monthly.html'

create_html(dict_to_html(min30_rank()), "30分整地量ランキング", min30_html)
# create_html(dict_to_html(daily_rank()), "日間整地量ランキング", daily_html)
# create_html(dict_to_html(weekly_rank()), "週間整地量ランキング", weekly_html)
# create_html(dict_to_html(monthly_rank()), "月間整地量ランキング", monthly_html)
