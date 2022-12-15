#include <iostream>
#include <string>
#include <vector>

int main() {
    int curr_calories = 0;
    std::vector<int> calories;

    for (std::string line; std::getline(std::cin, line);) {
        if (line == "") {
            calories.push_back(curr_calories);
            curr_calories = 0;
        } else {
            curr_calories += std::stoi(line, NULL, 10);
        }
    }

    std::sort(calories.begin(), calories.end());

    int a, b, n;
    n = calories.size();
    a = calories[n - 1];
    b = 0;
    
    for (int i = 0; i < 3; i++) {
        b += calories[n - i];
    }
    
    std::cout << a << std::endl;
    std::cout << b << std::endl;

    return 0;
}