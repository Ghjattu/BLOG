try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

import json
import requests
from flask import request, redirect, url_for


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect_back(default='blog.index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


def load_image(cnt):
    url = 'https://api.ixiaowai.cn/mcapi/mcapi.php?return=json'
    images = []
    session = requests.Session()
    for _ in range(cnt):
        try:
            response = session.get(url, headers={"Accept": "application/json"})
            data = json.loads(response.text, strict=False)
            images.append(data['imgurl'])
        except json.JSONDecodeError:
            images.append('https://api.ixiaowai.cn/mcapi/mcapi.php')
    return images
