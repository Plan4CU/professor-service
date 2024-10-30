from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService
import json
import os
from dotenv import load_dotenv


def get_db_service():
    
    load_dotenv()
    
    db_user = str(os.getenv("DB_USER"))
    db_password = str(os.getenv("DB_PASSWORD"))
    db_host = str(os.getenv("DB_HOST")) # populate this with the URL of the DB
    db_port = int(os.getenv("DB_PORT", 3306)) # default to 3306 if not set 
    
    context = dict(user=db_user, password=db_password,
                   host=db_host, port=db_port)
    
    data_service = MySQLRDBDataService(context=context)
    
    if data_service is None:
        raise Exception("Could not create data service")
    return data_service


def t1():
    data_service = get_db_service()
    result = data_service.get_data_object(
        "registrar_data",
        "Professor",
        key_field="p_uni",
        key_value="bsb2151"
    )
    print("t1 result = \n", json.dumps(result, indent=4, default=str))


if __name__ == '__main__':
    t1()