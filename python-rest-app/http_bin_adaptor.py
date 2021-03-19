import requests


def get_response():
    
    headers = {'Content-Type':'application/json'}
    return requests.get(_url('/get'),headers=headers)

def post_response(summary, description=""):
    return requests.post(_url('/post'), json={
        'summary': summary,
        'description': description,
        })

def _url(path):
    return 'http://httpbin.org' + path