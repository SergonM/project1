from markdown2 import Markdown
from django.shortcuts import render
from . import util

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki_entry(request, entry_title):
    entry = util.get_entry(entry_title)

    if (entry == None):
        return render(request, "encyclopedia/not_found.html")

    markdowner = Markdown()
    entry_html = markdowner.convert(entry)
    return render(request, "encyclopedia/wiki_entry.html", {"name": entry_title, "entry_html": entry_html})

