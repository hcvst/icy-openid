def index():
    posts = []
    posts.append(format_post('Welcome to ICY openid', 'your openid provider', P('openID is single-sign-on for the web. '*10 )))
    posts.append(format_post('What is openID?', 'single-sign-on for the web', P('openID is single-sign-on for the web. '*10 )))
    posts.append(format_post('Who uses openID?', 'single-sign-on for the web', P('openID is single-sign-on for the web. '*10 )))
    return dict(posts=posts)
