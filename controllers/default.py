def index():
    posts = []
    posts.append(format_post('Welcome to ICY openid', 'your openid provider', P('blah '*500)))
    return dict(posts=posts)