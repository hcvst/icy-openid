from openid.server.server import Server
exec "from applications.%s.modules.web2pystore import Web2pyStore" % request.application
    
def index():
    oidstore = Web2pyStore(db)
    cache.ram('oid_cleanup', lambda: oidstore.cleanup(), time_expire=25200) #call cleanup approx. every 7h
    oserver = Server(oidstore, OID_SERVER)
    orequest = oserver.decodeRequest(request.vars)
    
    #if another controller asked to cancel this authentication request do so
    if session.oid_cancel:
       session.oid_cancel = None
       return redirect(orequest.getCancelURL())
    
    user_is_logged_in = auth.is_logged_in()
    user_owns_id = user_is_logged_in and auth.user['nickname'] == orequest.identity.split('/').pop().lower() #lazy eval
    user_trusts_root = user_is_logged_in and _userTrustsRoot(orequest.trust_root) #lazy eval

    if orequest.mode in ['checkid_immediate', 'checkid_setup']:
        if user_is_logged_in and user_owns_id and user_trusts_root:
            resp = orequest.answer(True)
        elif orequest.immediate:
            resp = orequest.answer(False)
        else:
            #populate oid session with details as required by other controllers such as the url to
            #redirect to after logon or after approving data transfer to the relying party.
            session.oid_url = URL(r=request, args=request.args, vars=request.vars)
            #redirect user to authenticate herself or to authorise request 
            if user_is_logged_in:
                session.oid_orequest = orequest
                session.oid_user_owns_id = user_owns_id
                return redirect(URL(r=request, c='auth', f='data'))
            else:
                return redirect(URL(r=request, c='auth', f='user', args=['login']))            
    else:
        #let the library handle it
        resp = oserver.handleRequest(orequest)
    
    oresp = oserver.encodeResponse(resp)
    if oresp.code==200:
        return oresp.body
    else:
        return redirect(oresp.headers['location'], oresp.code)


# helper functions

def _userTrustsRoot(root):
    if session.oid_trust_root_once == root:
        session.oid_trust_root_once = None
        return True
    else:
        query = (db.oid_trust.auth_user == auth.user.id) & (db.oid_trust.trust_root == root)
        return db(query).count() == 1 # > 1 should not happen, will check for duplicates when adding trust records
