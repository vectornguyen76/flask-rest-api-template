from marshmallow import fields

from app.schemas.permission_schema import PlainPermissionSchema
from app.schemas.role_schema import PlainRoleSchema
from app.schemas.user_schema import PlainUserSchema


class PermissionSchema(PlainPermissionSchema):
    roles = fields.List(fields.Nested(PlainRoleSchema()), dump_only=True)


class RoleSchema(PlainRoleSchema):
    permissions = fields.List(fields.Nested(PlainPermissionSchema()), dump_only=True)
    users = fields.List(fields.Nested(PlainUserSchema()), dump_only=True)


class UpdateRolePermissionSchema(PlainRoleSchema):
    permissions = fields.List(cls_or_instance=fields.Int, required=True)
