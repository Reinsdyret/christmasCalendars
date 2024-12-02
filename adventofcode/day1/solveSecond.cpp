#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <map>
using namespace std;

int main() {
    // Your code goes here
    
    int total_sum = 0;

    fstream input_file;
    input_file.open("input.txt", ios::in);

    string line;
    map<int, int> location_count = {};
    map<int, int> key_count = {};
    vector<int> v = {};
    
    while (true) {
        getline(input_file, line);

        if (line.empty()) break;

        std::istringstream iss(line);
        int numA, numB;

        if (iss >> numA >> numB) {
            if (key_count.find(numA) != key_count.end()) {
                key_count[numA] += 1;
            } else{
                key_count[numA] = 1;
                location_count[numA] = 0;
            }

            v.push_back(numB);
        } else {
            cerr << "Error: Something went wrong when parsing as two ints from line: " << line;
        }
    }

    for (int num : v) {
        if (location_count.find(num) != location_count.end()) {
            location_count[num] += 1;
        }
    }

    for (auto i : location_count) {
        //cout << "Num: " << i.first << " seen: " << i.second << " times. \n";
        //cout << i.first * i.second * key_count[i.first] << "\n";
        total_sum += i.first * i.second * key_count[i.first];
    }

    cout << total_sum;
    
    return 0;
}
