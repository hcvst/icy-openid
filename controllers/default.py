def index():
    posts = []
    posts.append(format_post('Welcome to ICY openid', 'your openid provider', P('openID is single-sign-on for the web. '*10 )))
    posts.append(format_post('What is openID?', 'single-sign-on for the web', P(IMG(_src=URL(r=request, c='static', f='openid-100x100.png'), _style="margin-right:1em", _align="left", _alt="openID logo"),'openID is single-sign-on for the web. '*10 )))
    posts.append(format_post('Where to use openID?', 'single-sign-on for the web', P('openID is single-sign-on for the web. '*10 )))
    return dict(posts=posts)
