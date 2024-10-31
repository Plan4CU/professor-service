from typing import List, Dict, Any
from framework.resources.base_resource import BaseResource
from app.models.professor import Professor
from app.services.service_factory import ServiceFactory

class ProfessorResource(BaseResource):

    def __init__(self, config):
        super().__init__(config)
        self.data_service = ServiceFactory.get_service("ProfessorResourceDataService")
        self.database = "registrar_data"
        self.collection = "Professor"
        self.key_field = "p_uni"

    def get_by_key(self, key: str) -> Professor:
        result = self.data_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )
        return Professor(**result) if result else None

    def insert_by_fields(self, first_name: str, last_name: str) -> Professor:
        result = self.data_service.insert_data_object(
            self.database, self.collection, {"first_name": first_name, "last_name": last_name}
        )
        return Professor(**result)

    def update_by_fields(self, p_uni: str, column_name: str, new_value: str) -> Professor:
        result = self.data_service.update_data_object(
            self.database, self.collection, p_uni, {column_name: new_value}
        )
        return Professor(**result)

    def delete_by_key(self, p_uni: str) -> bool:
        return self.data_service.delete_data_object(
            self.database, self.collection, p_uni
        )

    def get_all_professors(self, page: int, size: int, professor_id: str = None) -> Dict[str, Any]:
        query_params = {}
        if professor_id:
            query_params["p_uni"] = professor_id

        results, total = self.data_service.get_data_objects(
            self.database, self.collection, query_params=query_params, page=page, size=size
        )

        professors = [Professor(**result) for result in results]
        return {
            "items": professors,
            "total": total,
            "page": page,
            "size": size
        }