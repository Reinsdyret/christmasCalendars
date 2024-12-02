#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;


tuple<int, string> getFirstWord(string &line, map<string, string> numbers) {
    for (int i = 0; i < line.length(); i++) {
        for (int j = i; j < line.length(); j++) {
            if (numbers.count(line.substr(i, j - i)) > 0) {
                return {i, numbers[line.substr(i, j - i)]};
            }
        }
    }
    return {9999999, ""};
}

tuple<int, string> getLastWord(string &line, map<string, string> numbers) {
    for (int i = line.length(); i > 0; i--) {
        for (int j = i; j <= line.length(); j++) {
            if (numbers.count(line.substr(i - 1, j - i + 1)) > 0) {
                return {i, numbers[line.substr(i - 1, j - i + 1)]};
            }
        }
    }
    return {-1, ""};
}

tuple<int, char> getFirstIntValue(string &line) {
    for (size_t i = 0; i < line.length(); i++) {
            if (isdigit(line[i])) {
                return {i, line[i]};
            }
    }

    return {9999999, 0};
}

tuple<int, char> getLastIntValue(string &line) {
    for (size_t i = line.length(); i > 0; i--) {
            if (isdigit(line[i - 1])) {
                return {i - 1, line[i - 1]};
            }
    }

    return {-1, 0};
}

int main() {
    int fwIndex, lwIndex, fiIndex, liIndex;
    string fwValue, lwValue, fiValue, liValue;
    int number_sum = 0;

    

    
    map<string, string> numbers;
    numbers["one"] = "1";
    numbers["two"] = "2";
    numbers["three"] = "3";
    numbers["four"] = "4";
    numbers["five"] = "5";
    numbers["six"] = "6";
    numbers["seven"] = "7";
    numbers["eight"] = "8";
    numbers["nine"] = "9";
    
    fstream input_file;
    input_file.open("input.txt", ios::in);

    string input;
    while( true ) {
        getline(input_file, input);
        if (input == "") {break;}

        string line_numbers = "";

        tie(fwIndex, fwValue) = getFirstWord(input, numbers);
        tie(lwIndex, lwValue) = getLastWord(input, numbers);

        tie(fiIndex, fiValue) = getFirstIntValue(input);
        tie(liIndex, liValue) = getLastIntValue(input);

        cout << fwIndex << " " << fwValue << "\n";
        cout << lwIndex << " " << lwValue << "\n";
        cout << fiIndex << " " << fiValue << "\n";
        cout << liIndex << " " << liValue << "\n";

        if (fwIndex < fiIndex) {
            line_numbers += fwValue;
        } else {
            line_numbers += fiValue;
        }

        if (lwIndex > liIndex) {
            line_numbers += lwValue;
        } else {
            line_numbers += liValue;
        }

        cout << line_numbers;

        number_sum += stoi(line_numbers);
        cout << line_numbers + "\n";
    }

    cout << number_sum;

    input_file.close();
    
    return 0;
}

