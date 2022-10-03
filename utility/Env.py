import os

class env(object):
    @staticmethod
    def host():
        return os.getenv('host','')
		
    @staticmethod
    def user():
        return os.getenv('user','')
		
    @staticmethod
    def password():
        return os.getenv('password','')
		
    @staticmethod
    def dbname():
        return os.getenv('dbname','')
		
    @staticmethod
    def sslmode():
        return os.getenv('sslmode','')