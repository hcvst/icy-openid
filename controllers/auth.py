# This controller handles login etc. in user() and
# authorisation for data transfer to the relaying party in data()

def user():
    views = {'login':dict(title='Please login', text='', dialogView=True),
             'register':dict(title='Register an openID', text='Sing up for your free openID. The fields up to and including password are required.', dialogView=True),
             'profile':dict(title='Your openID profile', text='Update your profile using the form below. Please not that changing your nickname will not change your openid.'),
             'change_password':dict(title='Change password', text='Please use the form below to change your password.')
            }
    view = views.get(request.args[0], dict(title='', text=''))
    view['form'] = auth()
    return view


def data():
    from openid.extensions.sreg import SRegRequest
    orequest = session.oid_orequest
    auth_user = auth.user.oid_name
    oid_user = orequest.identity.split('/').pop().lower()
    if not orequest:
        response.flash="An error occured!"
        return response.render('auth/data-error.html', dict(dialogView=True))
    elif not session.oid_user_owns_id:
        response.flash="Incorrect user!"
        return response.render('auth/data-idmismatch.html', dict(auth_user=auth_user, oid_user=oid_user, dialogView=True))
    else:

        body = "You are about to log in to %s as %s." % (orequest.trust_root, auth_user)
        sreg_req = SRegRequest.fromOpenIDRequest(orequest)
        if sreg_req.wereFieldsRequested():
            body += '<br />In addition the site has requested the following information.'
            if sreg_req.required:
                body += '<h2>Required information</h2>'
                for r in sreg_req.required:
                    body += r.capitalize()
            if sreg_req.optional:
                body += '<h2>Optional information</h2>'
                for o in sreg_req.optional:
                    body += o.capitalize()
            if sreg_req.policy_url:
                body += "The site's data usage policy can be found here: <a href='%(url)s'>%(url)s</a>" % {"url":sreg_req.policy_url}
            else:
                body += """This site did not include a link to their data usage policy. 
                           This might be a bad thing. If you are the site-admin please
                           consider adding one."""
                    
        resp = dict(body=body)
    return resp
    
    if request.args:
        mode = request.args[0]
        if mode == 'once':
            session.trust_root_once = session.trust_root
        elif mode == 'trust':
            query = (db.oid_trust.auth_user == auth.user.id) & (db.oid_trust.trust_root == session.trust_root)
            assert db(query).count() == 0
            db.oid_trust.insert(auth_user = auth.user, trust_root = session.trust_root)
        elif mode == 'cancel':
            session.cancel = True
        return redirect(session.oid_url)
    else: return """
Grant access to data?<br/>
<a href="%s">Yes once</a> |<a href="%s">Yes always</a> |<a href="%s">No, cancel</a> 
""" % (URL(r=request,args=['once']),URL(r=request,args=['trust']),URL(r=request,args=['cancel']))

def submit():
    pass
