#!/bin/sh
import rclpy
from rclpy.node import Node
from rcl_interfaces.srv import GetParameters

class TestGetGlobalParam(Node):

    def callback_global_param(self, future):
        try:
            result = future.result()
        except Exception as e:
            self.get_logger().warn("service call failed %r" % (e,))
        else:
            param = result.values[0]
            self.get_logger().info("Got global param: %s" % (param.string_value,))

    def __init__(self):
        super().__init__("test_get_global_param")

        self.client = self.create_client(GetParameters,
                                         '/global_parameter_server/get_parameters')

        request = GetParameters.Request()
        request.names = ['my_global_param']

        self.client.wait_for_service()

        future = self.client.call_async(request)
        future.add_done_callback(self.callback_global_param)


