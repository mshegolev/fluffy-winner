# coding: utf-8
from horoscope import generate_prophecies
from datetime import datetime as dt, timedelta


def generate_head(title):
    head = f"""<head>
    <meta charset='utf-8'>
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css"/>
    </head>
    """
    return head


def generate_navbar():
    return f"""
        &nbsp;
        <a href="about.html">О нас</a>
        &nbsp;&nbsp;
        <a href="contacts.html">Сontacts</a>
            <hr/>
    """


def generate_page(head, body, navbar=generate_navbar()):
    page = f"""<html>
    {head}
    {navbar}
    {body}
    </html>
    """
    return page


def generate_body(header, paragraphs):
    body = f"<h1>{header}</h1>"
    i = 0
    for p in paragraphs:
        body = body + f"<p>{p}</p>"
        i = i + 1
    return f"<body>{body}</body>"


def save_page(title, header, paragraphs, output="index.html"):
    fp = open(output, "w")
    today = dt.now().date()
    page = generate_page(head=generate_head(title),
                         body=generate_body(header=header, paragraphs=paragraphs))
    print(page, file=fp)
    fp.close()


def generate_body(header, paragraphs):
    body = "<h1>" + header + "</h1>"
    for p in paragraphs:
        body += "<p>" + p + "</p>"
    return "<body>" + body + "</body>"


# body = generate_body(header="Гороскоп на 2018-11-12", paragraphs=generate_prophecies())

# today = dt.now().date()
today = dt.today() + timedelta(days=1)
today = today.strftime('%d %m %Y')
save_page(title="Гороскоп на сегодня",
          header="Что день " + str(today) + " готовит",
          paragraphs=generate_prophecies())
