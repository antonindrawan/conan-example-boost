#include <boost/asio/io_service.hpp>
#include <boost/asio/signal_set.hpp>
#include <boost/thread.hpp>

#include <iostream>

int main()
{
  boost::asio::io_service io;

  boost::asio::signal_set signal_set {io, SIGINT, SIGTERM};
  signal_set.async_wait([](const boost::system::error_code& error_code, int signal_no) {
      if (!error_code) {
          std::cout << "[tid="<< boost::this_thread::get_id() << "] Received signal: " << signal_no << "; error message: " << error_code.message() << "\n";
      } else {
          std::cout << "[tid="<< boost::this_thread::get_id() << "] Received an error on the signal handler: " << error_code.message() << "\n";
      }
  });

  std::cout << "[tid="<< boost::this_thread::get_id() << "] Main thread" << "\n";

  io.run();

  return 0;
}
