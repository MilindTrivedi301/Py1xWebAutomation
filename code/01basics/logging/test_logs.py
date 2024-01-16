# Logging Means - Capture details, Which are useful while debugging
# and show the user details about execution of program.

# Warning to the users
# Information to the users
# Errors, Critical Errors user.

import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)

    # Intentional Logging to User
    LOGGER.info("This is information Logs")
    LOGGER.warning("This is Warning Logs")
    LOGGER.error("This is Error Logs")
    LOGGER.critical("This is Critical Logs")

    # __name__ wil also provide the info about which file is printing or to navigate
    # if we don't use -s the all the print statements are not going to be printed
    # -v is used for verbos used to print logs and additional info (more details would be shown)