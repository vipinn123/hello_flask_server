import os
import mysql.connector
from hello_flask_server.controllers import logHandler


# Initialize the logger
logger = logHandler.get_logger(os.path.basename(__file__))


# noqa: E501
def hello_swagger_get(first_name):
    """hello_swagger_get

    Say hello!  # noqa: E501

    :param first_name: Name of the person
    :type first_name: str

    :rtype: str
    """

    cnx = mysql.connector.connect(user='mysql', passwd='dbpwd123',
                                  host='172.21.177.144', port='3306',
                                  db='mysql_db')

    cursor = cnx.cursor()

    query = "show databases;"

    cursor.execute(query)
    results = cursor.fetchall()

    txt = str(first_name) + 'do some magic @ '

    for (database) in results:
        logger.debug(database)
        txt = txt + str(database[0]) + "  "

    logger.debug(txt)

    return txt
