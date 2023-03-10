#! /usr/bin/env python3

###
# KINOVA (R) KORTEX (TM)
#
# Copyright (c) 2023 Kinova inc. All rights reserved.
#
# This software may be modified and distributed
# under the terms of the BSD 3-Clause license.
#
# Refer to the LICENSE file for details.
#
###

import os
import sys

from kortex_api.autogen.client_stubs.BaseClientRpc import BaseClient
from kortex_api.autogen.messages import Base_pb2
from kortex_api.exceptions.KServerException import KServerException

# This example causes an error on purpose which is caught to print the detail of errors and sub errors.
def example_error_management(base):

    try:
        base.CreateUserProfile(Base_pb2.FullUserProfile())

    except KServerException as ex:
        # Get error and sub error codes
        error_code = ex.get_error_code()
        sub_error_code = ex.get_error_sub_code()
        print("Error_code:{0} , Sub_error_code:{1} ".format(error_code, sub_error_code))
        print("Caught expected error: {0}".format(ex))


def main():
    # Import the utilities helper module
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    import utilities

    # Parse arguments
    args = utilities.parseConnectionArguments()

    # Create connection to the device and get the router
    with utilities.DeviceConnection.createMqttConnection(args) as router:

        # Create required services
        base = BaseClient(router)

        # Example core
        example_error_management(base)


if __name__ == "__main__":
    main()
