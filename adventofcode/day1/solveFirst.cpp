#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

int main() {
    // Your code goes here
    
    int total_sum = 0;

    fstream input_file;
    input_file.open("input.txt", ios::in);

    string line;
    vector<int> v1 = {};
    vector<int> v2 = {};
    
    while (true) {
        getline(input_file, line);

        if (line.empty()) break;

        std::istringstream iss(line);
        int numA, numB;

        if (iss >> numA >> numB) {
            v1.push_back(numA);
            v2.push_back(numB);
        } else {
            cerr << "Error: Something went wrong when parsing as two ints from line: " << line;
        }
    }

    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());

    for (size_t i = 0; i < v1.size(); i++) {
        total_sum += abs(v1[i] - v2[i]);
    }

    cout << total_sum;
    
    return 0;
}