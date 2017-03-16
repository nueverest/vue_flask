import uuid


def is_production():
    """ Determines if app is running on the production server or not.

    Compare uuid for the machine against the know uuid of the development machine.
    :return: (bool) True if code is running on the production server, and False otherwise.
    """
    developer_machines = [111111111, ]
    return uuid.getnode() not in developer_machines