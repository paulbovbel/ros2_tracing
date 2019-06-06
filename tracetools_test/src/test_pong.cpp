#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class PongNode : public rclcpp::Node
{
public:
  explicit PongNode(rclcpp::NodeOptions options)
  : Node("pong_node", options)
  {
    sub_ = this->create_subscription<std_msgs::msg::String>(
      "ping",
      rclcpp::QoS(10),
      std::bind(&PongNode::callback, this, std::placeholders::_1));
    pub_ = this->create_publisher<std_msgs::msg::String>(
      "pong",
      rclcpp::QoS(10));
  }

private:
  void callback(const std_msgs::msg::String::SharedPtr msg)
  {
    RCLCPP_INFO(this->get_logger(), "[output] %s", msg->data.c_str());
    auto next_msg = std::make_shared<std_msgs::msg::String>();
    next_msg->data = "some random pong string";
    pub_->publish(*next_msg);
    rclcpp::shutdown();
  }

  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr sub_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr pub_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);

  rclcpp::executors::SingleThreadedExecutor exec;
  auto pong_node = std::make_shared<PongNode>(rclcpp::NodeOptions());
  exec.add_node(pong_node);

  printf("spinning\n");
  exec.spin();

  // Will actually be called inside the node's callback
  rclcpp::shutdown();
  return 0;
}