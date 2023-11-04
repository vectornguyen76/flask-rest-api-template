from app.db import db


class BlocklistModel(db.Model):
    __tablename__ = "blocklist"

    jti_blocklist = db.Column(db.String(), primary_key=True)
