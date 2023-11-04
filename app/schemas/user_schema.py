from marshmallow import Schema, fields


class PlainUserSchema(Schema):
    # Dump only: chỉ read
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    time_created = fields.Str(dump_only=True)


class UserUpdateSchema(Schema):
    username = fields.Str(allow_none=True, required=True)
    password = fields.Str(allow_none=True, required=True)
    roles = fields.List(cls_or_instance=fields.Int, required=True)


class PlainPermissionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    route = fields.Str(required=True)


class PlainRoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    permissions = fields.List(fields.Nested(PlainPermissionSchema()), dump_only=True)


class RoleSchema(PlainRoleSchema):
    users = fields.List(fields.Nested(PlainUserSchema()), dump_only=True)


class UserSchema(PlainUserSchema):
    block = fields.Bool(dump_only=True)
    roles = fields.List(fields.Nested(PlainRoleSchema()), dump_only=True)


class PermissionSchema(PlainPermissionSchema):
    roles = fields.List(fields.Nested(PlainRoleSchema()), dump_only=True)


class UserExportSchema(Schema):
    role_id = fields.Int(allow_none=True, required=True)
    search_content = fields.Str(allow_none=True, required=True)


class UserFilterSchema(UserExportSchema):
    page_size = fields.Int(allow_none=True, required=True)
    page = fields.Int(allow_none=True, required=True)


class UserPageSchema(Schema):
    results = fields.List(fields.Nested(UserSchema()))
    total_page = fields.Int()
    total_user = fields.Int()


class UserAndRoleSchema(Schema):
    message = fields.Str()
    user = fields.Nested(UserSchema)
    role = fields.Nested(RoleSchema)


class RoleAndPermissionSchema(Schema):
    message = fields.Str()
    role = fields.Nested(RoleSchema)
    permission = fields.Nested(PermissionSchema)


class GetRolePermissionSchema(Schema):
    id = fields.Int(dump_only=True)
    role_id = fields.Int(dump_only=True)
    permission_id = fields.Int(dump_only=True)


class UpdateUserRoleSchema(Schema):
    roles = fields.List(cls_or_instance=fields.Int, required=True)


class UpdateBlockUserSchema(Schema):
    block = fields.Bool(required=True)


class UpdateRolePermissionSchema(PlainRoleSchema):
    permissions = fields.List(cls_or_instance=fields.Int, required=True)


class UpdatePermissionRoleSchema(Schema):
    data_update = fields.Dict(required=True)


class CheckUserExistsSchema(Schema):
    email = fields.Str(required=True)


class UserLoginSchema(Schema):
    access_token = fields.Str()
    refresh_token = fields.Str()
    user = fields.Nested(UserSchema)
