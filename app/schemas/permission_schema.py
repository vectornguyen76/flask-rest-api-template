from marshmallow import Schema, fields

from app.schemas.role_schema import PlainRoleSchema


class PlainPermissionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    route = fields.Str(required=True)


class PermissionSchema(PlainPermissionSchema):
    roles = fields.List(fields.Nested(PlainRoleSchema()), dump_only=True)


class UpdatePermissionRoleSchema(Schema):
    data_update = fields.Dict(required=True)
