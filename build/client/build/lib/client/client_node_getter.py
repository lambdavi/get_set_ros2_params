import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter, ParameterType
from rcl_interfaces.srv import GetParameters, SetParameters
import time
from threading import Thread
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
        request.names = ['my_global_param', 'my_global_param2']
        self.client.wait_for_service()
        future = self.client.call_async(request)
        future.add_done_callback(self.callback_global_param)
                   
    
def main():
    rclpy.init()

    minimal_client = TestGetGlobalParam()

    spin_thread = Thread(target=rclpy.spin, args=(minimal_client,))
    spin_thread.start()
    

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

