def profile():
    id = request.args[0]
    return dict(identity=id, xrds_location = OID_XRDS_BASE+id)
   
def xrds():
    if request.args[0]:
        return OID_XRDS % (OID_SERVER, OID_DELEGATION_BASE + request.args[0]) #constants defined in openid.py model
    else:
        return
