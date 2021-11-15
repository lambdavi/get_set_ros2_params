import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType, ParameterValue, Parameter
from rcl_interfaces.srv import GetParameters, SetParameters
import time
from threading import Thread

class ClientNode(Node):
    def __init__(self):
        super().__init__('client_node')
        self.getSrv = self.create_client(GetParameters, '/global_parameter_server/get_parameters')
        self.setSrv = self.create_client(SetParameters, '/global_parameter_server/set_parameters')
        self.stringToSet = ""

    def callback_set_param(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().warn("service call failed %r" % (e,))
        else:
            self.get_logger().info(
                    'Result of set parameters: for %s' % (str(response)))

    def getParams(self):
        request = GetParameters.Request()
        request.names = ['my_global_param']
        self.getSrv.wait_for_service()
        self.futureGet = self.getSrv.call_async(request)

    def setParams(self):
        req = SetParameters.Request()
        new_param_value = ParameterValue(type=ParameterType.PARAMETER_STRING, string_value=self.stringToSet)
        req.parameters = [Parameter(name='my_global_param', value=new_param_value)]
        self.futureSet = self.setSrv.call_async(req)
        self.futureSet.add_done_callback(self.callback_set_param)

def main(args=None):
    rclpy.init(args=args)
    client_node = ClientNode()
    
    spin_thread = Thread(target=rclpy.spin, args=(client_node,))
    spin_thread.start()
    i = 0
    while rclpy.ok() and i <20:
        i+=1
        client_node.getParams()
        print("Waiting 1sec until next check on parameters..")
        time.sleep(1)
        if client_node.futureGet.done():
            if client_node.futureGet.result() is not None:
                response = client_node.futureGet.result()
                param = response.values[0]
                print("Parameter value: "+param.string_value)
                if param.string_value == "miao":
                    client_node.stringToSet="test"
                    client_node.setParams()
            else:
                client_node.futureGet.get_logger().info(
                    'Service call failed %r' % (client_node.futureGet.exception(),))
                
    client_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

