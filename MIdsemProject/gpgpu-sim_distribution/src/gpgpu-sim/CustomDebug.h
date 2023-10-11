// This header file is used to create a custom debug file to get the output of
// counters ans debug statements in a separate txt file.
#include <fstream>
#include <string>

class CustomDebug {
 private:
  std::string filename;
  std::ofstream stream;
  void createStream() { stream.open(filename); }

 public:
  CustomDebug(std::string _filename) : filename(_filename) { createStream(); }
  CustomDebug() {
    filename = "CustomDebugOutput";
    createStream();
  }
  void putLine(std::string line) { stream << line << std::endl; }
  ~CustomDebug() { stream.close(); }
  void close() { stream.close(); }
};