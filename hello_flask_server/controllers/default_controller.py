import os
import mysql.connector
from hello_flask_server.controllers import logHandler


from pykafka import KafkaClient

import configparser



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
    txt=""

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

    config = configparser.ConfigParser()
    my_file = (os.path.join(os.getcwd(), 'hello_flask_server/controllerssettings.conf'))

    logger.debug(my_file)
    config.read(my_file)
    #config.read('settings.conf')

    kafka_client = KafkaClient(hosts=config.get('kafka_demo', 'kafka_hosts'))  # Create Kafka client
    #kafka_client = KafkaClient(hosts='hello-ocp-kafka-kafka-bootstrap:9092')  # Create Kafka client
    topic = kafka_client.topics['datacom']  # This will create the topic if it does not exist

    logger.debug("Producing messages to topic {}. Press Ctrl-C to interrupt.".format(topic))

    producer = topic.get_producer()

    producer.produce("Testing Kafka from hello Flask".encode('utf-8'),"key1".encode('utf-8'))
    return txt
