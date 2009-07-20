from openid.association import Association
from openid.store.interface import OpenIDStore
from openid.store import nonce
import time

class Web2pyStore(OpenIDStore):
    """Web2pySore implements the OpenIDStore interface. OpenID stores take care
       of persisting nonces and associations. The openid librabry comes with implementations
       for file and memory storage. Web2pyStore uses the web2py db abstration layer.
       See the source code docs of OpenIDStore for a comprehensive description of this
       interface. 
    """

    def __init__(self, database):
        self._database = database
    
    @property
    def database(self):
        return self._database
    
    def storeAssociation(self, server_url, association):
        """Store associations. If there already is one with the same 
           server_url and handle in the table replace it."""
        
        db = self.database      
        query = (db.oid_associations.server_url == server_url) & (db.oid_associations.handle == association.handle)
        db(query).delete()
        db.oid_associations.insert(server_url = server_url,
                                   handle = association.handle,
                                   secret = association.secret,
                                   issued = association.issued,
                                   lifetime = association.lifetime,
                                   assoc_type = association.assoc_type)
              
    def getAssociation(self, server_url, handle=None):
        """Return the association for server_url and handle. If handle is
           not None return the latests associations for that server_url.
           Return None if no association can be found."""
           
        db = self.database
        query = (db.oid_associations.server_url == server_url)
        if handle:
            query &= (db.oid_associations.handle == handle)
        rows = db(query).select(orderby=db.oid_associations.issued)
        keep_assoc, _ = self._removeExpiredAssocations(rows)
        if len(keep_assoc) == 0:
            return None
        else:
            assoc = keep_assoc.pop() # pop the last one as it should be the latest one
            return Association(assoc['handle'],
                               assoc['secret'],
                               assoc['issued'],
                               assoc['lifetime'],
                               assoc['assoc_type'])
        
    def removeAssociation(self, server_url, handle):
        db = self.database
        query = (db.oid_associations.server_url == server_url) & (db.oid_associations.handle == handle)
        return db(query).delete() != None
        
    def useNonce(self, server_url, timestamp, salt):
        """This method returns Falase if a nonce has been used before or its 
           timestamp is not current."""
        
        db = self.database
        if abs(timestamp - time.time()) > nonce.SKEW:
            return False
        query = (db.oid_nonces.server_url == server_url) & (db.oid_nonces.timestamp == timestamp) & (db.oid_nonces.salt == salt)
        if db(query).count() > 0:
            return False
        else:
           db.oid_nonces.insert(server_url = server_url,
                                timestamp = timestamp,
                                salt = salt)
           return True
   
    def _removeExpiredAssocations(self, rows):
        """This helper function is not part of the interface. Given a list of association rows
           it checks which associations have expired and deletes them from the db.
           It returns a tuple of the form ([valid_assoc], no_of_expired_assoc_deleted)."""
           
        keep_assoc = []
        remove_assoc = []
        t1970 = time.time()
        for r in rows:
            if r['issued'] + r['lifetime'] < t1970:
                remove_assoc.append(r)
            else:
                keep_assoc.append(r)
        for r in remove_assoc:
            del db.oid_associations[r['id']]       
        return (keep_assoc, len(remove_assoc)) # return tuple (list of valid associations, number of deleted associations)
          
    def cleanupNonces(self):
        """Remove expired nonce entries from DB and return the number
           of entries deleted. """
           
        db = self.database
        query = (db.oid_nonces.timestamp < time.time() - nonce.SKEW)
        return db(query).delete()
        
    def cleanupAssociations(self):
        """Remove expired associations from db and return the number
           of entries deleted."""
           
        db = self.database
        query = (db.oid_associations.id > 0)
        return self._removeExpiredAssocations(db(query).select())[1] #return number of assoc removed
        
    def cleanup(self):
        """This method should be run periodically to free the db from
           expired nonce and association entries."""
           
        print "Running cleanup..."
        return self.cleanupNonces(), self.cleanupAssociations()
