#include <iostream>
#include <string>
#include <list>
#include <vector>

using namespace std;

// Possible Improvements: Create a Weighted GPA option, allow the user to choose
// Remember the users previous grades, allow user to add/change values and recalculate accordingly

class userInput {
public:
    // Variables
    std::string name;
    double size;
    std::list<double> grades;
    double gpa;
    double sum;

    const vector<pair<int, double>> gpaScale = {
        {97,4.0}, {93,4.0}, {90,3.7}, {87,3.3}, {83,3.0},
        {80,2.7}, {77,2.3}, {73,2.0}, {70,1.7},
        {67,1.3}, {65,1.0}, {0,0.0}
    };

    // Initial values
    userInput(){
        name = " ";
        size = 0;
        sum = 0.0;
        gpa = 0.0;
    }

    void calculations() {
        // User input for Grades
        double grade;
        sum = 0; // Reset

        for (int i = 0; i < size; i++) {
            cout << "Grade for Class " << i + 1 << ": ";
            cin >> grade;

            if (grade > 100 || grade < 0) {
                cout << "Please enter a valid grade" << endl;
                i--;
                continue;
            }

            // Converts Grade to a GPA value
            for (auto scale : gpaScale) {
                if (grade >= scale.first) {
                    grades.push_back(scale.second);
                    break;
                }
            }
        }

        // Average results for total gpa
        for (double value : grades) {
            sum += value;
        }

        if (grades.empty()) {
            std::abort();
        }

        double average = sum / grades.size();
        cout << "Your GPA is: " << average << ".0";
    }
};

int main() {
    userInput vars;

    // Text menus & variable values
    cout << "Welcome to the unweighted gpa calculator! What is your name?: ";
    cin >> vars.name;
    cout << "Welcome, " << vars.name << std::endl;
    cout << "How many classes do you have a grade for?: ";
    cin >> vars.size;
    // cout << size; (DEBUG)

    // Calls functions
    vars.calculations();

    return 0;
}
