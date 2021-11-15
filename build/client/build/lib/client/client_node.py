import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter, ParameterType
from rcl_interfaces.srv import GetParameters, SetParameters
import time
from threading import Thread

class TestGetGlobalParam(Node):
    def callback_global_param(self):
        self.req = GetParameters.Request()
        self.req.names = ['my_global_param']
        self.future = self.cli.call_async(self.req)
        #self.future.add_done_callback(self.callback_global_param)
        #self.callback_global_param()

        
        """result = self.future.result()
    
        param = result.values[0]
        print(param.string_value)"""
            
        

            #self.get_logger().info("Got global param: %s" % (param.string_value,))
        
    def __init__(self):
        super().__init__("test_get_global_param")
        
        self.cli = self.create_client(GetParameters,
                                         '/global_parameter_server/get_parameters')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = None
        #self.callback_global_param()
        #value = future.result().values[0].string_value
        #print(future.result())
    
class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(SetParameters, '/global_parameter_server/set_parameters')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = None

    def send_request(self):
        self.req = SetParameters.Request()

        new_param_value = ParameterValue(type=ParameterType.PARAMETER_STRING, string_value="test")
        self.req.parameters = [Parameter(name='my_global_param', value=new_param_value)]
        
        #self.req.parameters.append(param)


        self.future = self.cli.call_async(self.req)      
    
def main():
    rclpy.init()

    minimal_client = TestGetGlobalParam()
    minimal_client.callback_global_param()
    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            if minimal_client.future.result() is not None:
                response = minimal_client.future.result()

                value = response.values[0].string_value
                print(future.result())
            else:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (minimal_client.future.exception(),))
            break
    

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

