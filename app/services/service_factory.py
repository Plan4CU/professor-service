import os
from dotenv import load_dotenv
from framework.services.service_factory import BaseServiceFactory
from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService

class ServiceFactory(BaseServiceFactory):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_service(cls, service_name):

        load_dotenv()

        if service_name == 'ProfessorResource':
            import app.resources.professor_resource as professor_resource
            result = professor_resource.ProfessorResource(config=None)

        elif service_name == 'ProfessorResourceDataService':

            # populate the database information given the environment variable
            db_user = str(os.getenv("DB_USER"))
            db_password = str(os.getenv("DB_PASSWORD"))
            db_host = str(os.getenv("DB_HOST")) # populate this with the URL of the DB
            db_port = int(os.getenv("DB_PORT", 3306)) # default to 3306 if not set

            context = dict(user=db_user, password=db_password,
                           host=db_host, port=db_port)
            data_service = MySQLRDBDataService(context=context)
            result = data_service
        else:
            result = None

        return result