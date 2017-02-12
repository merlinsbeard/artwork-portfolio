from django import template
import requests
import json

register = template.Library()

@register.filter
def markdown(value):
    """ Turn markdown text into html """
    url = "https://api.github.com/markdown"
    data = {
            "text": value,
            }
    data_json = json.dumps(data)
    r = requests.post(url, data=data_json)
    return r.text
