import rclpy
from rclpy.node import Node
from rcl_interfaces.srv import GetParameters

class testPrint(Node):
	def __init__(self):
		super().__init__('test_params_rclpy')
		param_str = self.get_parameter('my_global_param')
		print("Hello")
"""
class TestGetGlobalParam(Node):
	def __init__(self):
		#super().__init__('test_params_rclpy')
		param_str = self.get_parameter('my_global_param')
		self.get_logger().info("Parametro trovato: "+str(param_str.value))


#test = TestGetGlobalParam()
"""
