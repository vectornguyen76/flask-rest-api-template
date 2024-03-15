from marshmallow import Schema, fields


class PlainRoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)


class GetRolePermissionSchema(Schema):
    id = fields.Int(dump_only=True)
    role_id = fields.Int(dump_only=True)
    permission_id = fields.Int(dump_only=True)
