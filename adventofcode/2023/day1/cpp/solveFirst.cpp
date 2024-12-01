#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    // Your code goes here
    int number_sum = 0;

    fstream input_file;
    input_file.open("input.txt", ios::in);

    string input;
    while( true ) {
        getline(input_file, input);
        if (input == "") {break;}
        

        string line_num = "";
        for (size_t i = 0; i < input.length(); i++) {
            if (isdigit(input[i])) {
                line_num += input[i];
                break;
            }
        }

        for (size_t i = input.length(); i > 0; i--) {
            if (isdigit(input[i - 1])) {
                line_num += input[i - 1];
                break;
            }
        }

        if (line_num.length() < 2) {
            cout << "Something wrong man" << line_num;
        }

        number_sum += stoi(line_num);
        
    }
    input_file.close();
    cout << number_sum;
    return 0;
}