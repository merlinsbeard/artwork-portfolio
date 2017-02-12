from django import template
import requests
import json

register = template.Library()

def markdown_old(value):
    """ Turn markdown text into html using the github api"""
    url = "https://api.github.com/markdown"
    data = {
            "text": value,
            "mode": "gfm",
            }
    data_json = json.dumps(data)
    r = requests.post(url, data=data_json)
    return r.text

import markdown2

@register.filter
def markdown(value):
    """ Turn markdown text into html using python-markdown2 """
    return markdown2.markdown(value)
