import os

class env(object):
    @staticmethod
    def host():
        return os.getenv('host','')
    
    def user():
        return os.getenv('user','')
    
    def password():
        return os.getenv('password','')
    
    def dbname():
        return os.getenv('dbname','')
    
    def sslmode():
        return os.getenv('sslmode','')