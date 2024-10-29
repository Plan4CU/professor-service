from framework.services.service_factory import BaseServiceFactory
# import app.resources.course_resource as course_resource

from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService


# TODO -- Implement this class
class ServiceFactory(BaseServiceFactory):

    def __init__(self):
        super().__init__()

    # @classmethod
    # def get_service(cls, service_name):
    #     #
    #     # TODO -- The terrible, hardcoding and hacking continues.
    #     #
    #     if service_name == 'CourseResource':
    #         result = course_resource.CourseResource(config=None)
    #     elif service_name == 'CourseResourceDataService':
    #         context = dict(user="root", password="dbuserdbuser",
    #                        host="35.226.242.252", port=3306)
    #         data_service = MySQLRDBDataService(context=context)
    #         result = data_service
    #     else:
    #         result = None

    #     return result
    
    @classmethod
    def get_service(cls, service_name):

        if service_name == 'ProfessorResource':
            # TODO: figure out what config is supposed to pass into the object
            
            # figure out why importing the professor_rsource allowed
            # for it work here 
            import app.resources.professor_resource as professor_resource
            result = professor_resource.ProfessorResource(config=None)
        elif service_name == 'ProfessorResourceDataService':
            context = dict(user="root", password="dbuserdbuser",
                           host="localhost", port=3306)
            data_service = MySQLRDBDataService(context=context)
            result = data_service
        else:
            result = None

        return result




