#include <iostream>
#include <string>

int score_of_a(char opp, char you) {
    if (opp == 'A' && you == 'X') {
        return 3 + 1;
    } else if (opp == 'A' && you == 'Y') {
        return 6 + 2;
    } else if (opp == 'A' && you == 'Z') {
        return 0 + 3;
    } else if (opp == 'B' && you == 'X') {
        return 0 + 1;
    } else if (opp == 'B' && you == 'Y') {
        return 3 + 2;
    } else if (opp == 'B' && you == 'Z') {
        return 6 + 3;
    } else if (opp == 'C' && you == 'X') {
        return 6 + 1;
    } else if (opp == 'C' && you == 'Y') {
        return 0 + 2;
    } else {
        return 3 + 3;
    }
}

int score_of_b(char opp, char you) {
    if (opp == 'A' && you == 'X') {
        return 0 + 3;
    } else if (opp == 'A' && you == 'Y') {
        return 3 + 1;
    } else if (opp == 'A' && you == 'Z') {
        return 6 + 2;
    } else if (opp == 'B' && you == 'X') {
        return 0 + 1;
    } else if (opp == 'B' && you == 'Y') {
        return 3 + 2;
    } else if (opp == 'B' && you == 'Z') {
        return 6 + 3;
    } else if (opp == 'C' && you == 'X') {
        return 0 + 2;
    } else if (opp == 'C' && you == 'Y') {
        return 3 + 3;
    } else {
        return 6 + 1;
    }
}

int main() {
    int a = 0;
    int b = 0;

    for (std::string line; std::getline(std::cin, line);) {
        char opp = line.at(0);
        char you = line.at(2);

        a += score_of_a(opp, you);
        b += score_of_b(opp, you);
    }

    std::cout << a << std::endl;
    std::cout << b << std::endl;

    return 0;
}