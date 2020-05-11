import connexion
import six
import mysql.connector
from hello_flask_server import util


def hello_swagger_get(first_name):  # noqa: E501
    """hello_swagger_get

    Say hello!  # noqa: E501

    :param first_name: Name of the person
    :type first_name: str

    :rtype: str
    """

    cnx = mysql.connector.connect(user='mysql', password='dbpwd123',
                                  host='172.21.177.144',
                                  database='sample_db')

    cursor = cnx.cursor()

    query = ("show databases")

    cursor.execute(query)

    txt = 'do some magic @'

    for (database) in cursor:
        txt = txt + database + ' '

    #return 'do some more magic!'

    return txt
