from marshmallow import Schema, fields

class UserSchema(Schema):
    # Dump only: chỉ read
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    time_created = fields.Str(dump_only=True)
    
class UserUpdateSchema(Schema):
    username = fields.Str(allow_none=True)
    password = fields.Str(allow_none=True)
    time_created = fields.Str(allow_none=True)