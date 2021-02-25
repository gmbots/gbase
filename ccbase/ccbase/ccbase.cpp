#include <boost/lambda/lambda.hpp>

#include "damo_controller.h"
#include "uwebsockets/App.h"
#include "damo.h"
int main() {
  runDm();
  auto app = uWS::App();
  app.get("/*", [](auto* res, auto*) {
    damo_controller::run();
    res->end("欢迎使用自动化脚本合集" + runDm());
  });
  app.listen(3000, [](auto* listen_socket) {
    if (listen_socket) {
      std::cout << "Listening on port " << 3000 << std::endl;
    } else {
      std::cout << "Failed to listen on port 3000" << std::endl;
    }
  });
  app.run();
}
