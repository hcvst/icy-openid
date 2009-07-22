response.menu = [('home', URL(r=request, c='default', f='index')),
                 ('profile', URL(r=request, c='acc')),
                 ('developer', 'http://icy.co.za'),
                 ('contact', 'http://icy.co.za')
                ]

def format_post(title, subtitle, entry):
    return DIV(H2(title, _class='title'),
               P(subtitle, _class='byline'),
               DIV(entry, _class='entry'),
              _class='post'
              )
