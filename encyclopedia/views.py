from django import forms
from markdown2 import Markdown
from django.shortcuts import redirect, render
from . import util

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki_entry(request, entry_title):
    entry = util.get_entry(entry_title)

    if (entry == None):
        return render(request, "encyclopedia/error_page.html", {"message": "The page was not found"})

    entry_html = convert_to_html(entry)
    return render(request, "encyclopedia/wiki_entry.html", {"name": entry_title, "entry_html": entry_html})

def search(request):
    if request.method == "POST":
        entry_title = request.POST["q"]
        entry = util.get_entry(entry_title)

        if (entry != None):
            entry_html = convert_to_html(entry)
            return render(request, "encyclopedia/wiki_entry.html", {"name": entry_title, "entry_html": entry_html})

        else:
            entries = util.list_entries()
            print(entries)
            entries_with_sub = list(filter(lambda title: entry_title.lower() in title.lower(), entries))
            print(entries_with_sub)
            return render(request, "encyclopedia/search_result.html", {"entries": entries_with_sub, "search": entry_title})

def new_page(request):

    if request.method == "POST":
        entry_title = request.POST["title"]
        entry_content = request.POST["content"]

        if util.get_entry(entry_title):
            return render(request, "encyclopedia/error_page.html", {"message": "The entry already exists"})

        else:
            util.save_entry(entry_title, entry_content)
            return redirect(f"/wiki/{entry_title}/")

    return render(request, "encyclopedia/new_page.html")

def convert_to_html(entry):
    markdowner = Markdown()
    return markdowner.convert(entry)

