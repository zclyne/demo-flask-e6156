from application_services.BaseApplicationResource import BaseApplicationResource
import database_services.RDBService as d_service

class UserResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    # TODO This can go into the base class.
    @classmethod
    def get_by_template(cls, template):
        res = d_service.RDBService.find_by_template("imdbnew", "users", template, None)
        return res

    @classmethod
    def get_by_first_name_prefix(cls, first_name_prefix):
        res = d_service.RDBService.get_by_prefix("imdbnew", "users",
                                                 "first_name", first_name_prefix)
        return res

    @classmethod
    def get_by_last_name_prefix(cls, last_name_prefix):
        res = d_service.RDBService.get_by_prefix("imdbnew", "users",
                                                 "last_name", last_name_prefix)
        return res