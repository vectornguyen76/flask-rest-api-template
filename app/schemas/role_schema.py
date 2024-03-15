from marshmallow import Schema, fields

from app.schemas.permission_schema import PlainPermissionSchema
from app.schemas.user_schema import PlainUserSchema


class PlainRoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)


class RoleSchema(PlainRoleSchema):
    permissions = fields.List(fields.Nested(PlainPermissionSchema()), dump_only=True)
    users = fields.List(fields.Nested(PlainUserSchema()), dump_only=True)


class UpdateRolePermissionSchema(PlainRoleSchema):
    permissions = fields.List(cls_or_instance=fields.Int, required=True)


class GetRolePermissionSchema(Schema):
    id = fields.Int(dump_only=True)
    role_id = fields.Int(dump_only=True)
    permission_id = fields.Int(dump_only=True)
