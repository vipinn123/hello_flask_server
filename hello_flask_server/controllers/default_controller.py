import connexion
import six

from hello_flask_server import util


def hello_swagger_get(first_name):  # noqa: E501
    """hello_swagger_get

    Say hello!  # noqa: E501

    :param first_name: Name of the person
    :type first_name: str

    :rtype: str
    """
    return 'do some magic!'
