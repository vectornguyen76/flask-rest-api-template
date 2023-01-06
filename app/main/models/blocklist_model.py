from .models import db

class BlocklistModel(db.Model):
    __tablename__ = "blocklist"
    
    blocklist = db.Column(db.String(), primary_key = True) 