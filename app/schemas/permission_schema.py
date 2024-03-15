from marshmallow import Schema, fields


class PlainPermissionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    route = fields.Str(required=True)


class UpdatePermissionRoleSchema(Schema):
    data_update = fields.Dict(required=True)
