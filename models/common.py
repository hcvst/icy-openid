def format_post(title, subtitle, entry):
    return DIV(H2(title, _class='title'),
               P(subtitle, _class='byline'),
               DIV(entry, _class='entry'),
              _class='post'
              )
