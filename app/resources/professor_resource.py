from typing import Any

from framework.resources.base_resource import BaseResource

from app.models.professor import Professor
from app.services.service_factory import ServiceFactory


class ProfessorResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)

        # TODO -- Replace with dependency injection.
        # TODO: get_service allows you to choose which SQL DB to connect to?
        self.data_service = ServiceFactory.get_service("ProfessorResourceDataService")
        self.database = "Professor" # TODO: change to the name of the DB 
        self.collection = "course_sections" # TODO: change to the name of the table 
        # TODO: change to the name of the column you are searching for in table 
        self.key_field= "sis_course_id" 

    def get_by_key(self, key: str) -> Professor:

        d_service = self.data_service

        # this is constructing the SQL query to grab the item by the key_field
        # parameter and it returns an object of type CourseSection 
        # where I'm assuming it populates the SQL data into a CourseSection object 
        result = d_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )

        result = CourseSection(**result)
        return result


