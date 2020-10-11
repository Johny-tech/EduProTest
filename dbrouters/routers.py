class MongoDBRouter(object):

    def allow_syncdb(self, db, model):
        # "Make sure the myapp app only appears on the 'other' db"
        if db == 'testdb':
            return model._meta.app_label == 'testApp'
        