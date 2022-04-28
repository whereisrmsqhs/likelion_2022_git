#include <iostream>
#include <sstream>
#include <string>

int main() {
  // greet the user
  std::string name;
  std::cout << "What is your name? ";
  std::getline(std::cin, name);
  std::cout << "Hello " << name << ", nice to meet you.\n";

  // stringstream 은 마치 문자열을 입력 스트림으로 생각하게 해줍니다.
  std::istringstream input;
  input.str("1\n2\n3\n4\n5\n6\n7\n");
  int sum = 0;
  for (std::string line; std::getline(input, line);) {
    sum += std::stoi(line);
  }
  std::cout << "\nThe sum is: " << sum << "\n";
}