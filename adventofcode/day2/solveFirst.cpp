#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

vector<int> splitStringToInt(const std::string& str, char delimiter) {
    std::vector<int> result;
    std::stringstream ss(str);
    std::string temp;

    // Loop to split the string based on the delimiter
    while (std::getline(ss, temp, delimiter)) {
        result.push_back(std::stoi(temp));
    }

    return result;
}

bool strictlyDecreasing(vector<int>& nums) {
  int prev = nums[0];

  for (size_t i = 1; i < nums.size(); i++) {
    if (nums[i] > prev) return false;

    prev = nums[i];
  }

  return true;
}

bool strictlyIncreasing(vector<int>& nums) {
  int prev = nums[0];

  for (size_t i = 1; i < nums.size(); i++) {
    if (nums[i] < prev) {
      cout << "FAAAAAAIL";
      return false;
    }

    prev = nums[i];
  }

  return true;
}

bool difference_check(vector<int>& nums) {
  int prev = nums[0];

  for (size_t i = 1; i < nums.size(); i++) {
    int diff = abs(prev - nums[i]);
    if (diff < 1 || diff > 3) {
      cout << "FAIL";
      return false;
    }

    prev = nums[i];
  }

  return true;
}

int main() {
  int count_safe_reports = 0;

  fstream input_file;
  input_file.open("input.txt", ios::in);

  string line;
  vector<int> levels;

  int i = 0;

  while(i < 10000) {
    getline(input_file, line);

    if (line == "") break;

    vector<int> numbers = splitStringToInt(line, ' ');


    i++;

    // Check that numbers are strictly decreasing or strictlyIncreasing
    if (numbers.size() <= 1) {
      cout << "Hit small size";
      count_safe_reports += 1;
      continue;
    }

    if (numbers[0] < numbers[1]) {
      if (!strictlyIncreasing(numbers)) continue;
    } else {
      if (!strictlyDecreasing(numbers)) continue;
    }

    // Check that two numbers in order have between 1 and 3 difference 
    if (difference_check(numbers)) count_safe_reports += 1;
  }

  input_file.close();

  cout << count_safe_reports;

  return 0;
} 
