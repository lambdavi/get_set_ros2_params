import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType, ParameterValue, Parameter
from rcl_interfaces.srv import GetParameters, SetParameters
import time
from threading import Thread

class TestGetGlobalParam(Node):
    
    def callback_global_param(self, future):
        global miao
        try:
            result = future.result()
        except Exception as e:
            self.get_logger().warn("service call failed %r" % (e,))
        else:
            param = result.values[0]
            
            self.get_logger().info("Got global param: %s" % (param.string_value,))
            miao = param.string_value
            
        
    def __init__(self):
        super().__init__("test_get_global_param")

        self.client = self.create_client(GetParameters,
                                         '/global_parameter_server/get_parameters')
        request = GetParameters.Request()
        request.names = ['my_global_param']
        self.client.wait_for_service()
        future = self.client.call_async(request)
        future.add_done_callback(self.callback_global_param)
    

class MinimalClientAsync(Node):
   
    def __init__(self):
        super().__init__('minimal_client_async')
        
        self.cli = self.create_client(SetParameters, '/global_parameter_server/set_parameters')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = None
        
    def send_request(self):
        self.req = SetParameters.Request()

        new_param_value = ParameterValue(type=ParameterType.PARAMETER_STRING, string_value="set")
        self.req.parameters = [Parameter(name='my_global_param', value=new_param_value)]
        
        #self.req.parameters.append(param)


        self.future = self.cli.call_async(self.req)
    def get_value(self):

        test = TestGetGlobalParam()
        spin_thread = Thread(target=rclpy.spin, args=(test,))
        spin_thread.start()
        test.destroy_node()

def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()
    minimal_client.get_value()
    minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            if minimal_client.future.result() is not None:
                response = minimal_client.future.result()

                minimal_client.get_logger().info(
                    'Result of set parameters: for %s' %
                    (str(response)))
            else:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (minimal_client.future.exception(),))
            break

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
