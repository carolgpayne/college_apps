#include <iostream>
#include <string>
#include <list>
#include <fstream>
#include <algorithm>
#include <memory>
#include <utility>

using namespace std;

// added similar for loop for reminders so there's no multiples in the .txt file
// ADDITIONS - allow user to try again after incorrect attempts? cap at 3
// ADDITIONS - hide password while user is typing it in

class userInput {
private:
    std::string username;
    std::string password;
    std::string account;
    std::list<string> usernameList = {};
    std::list<string> passwordList = {};
public:
    void loadAccountsFromFile() {
        std::ifstream infile("accounts.txt");
        std::string u, p;

        while (infile >> u >> p) {
            usernameList.push_back(u);
            passwordList.push_back(p);
    }

    infile.close();
}

    void accountSetup() {
        std::cout << "Welcome!" << std::endl;
        std::cout << "Would you like to create an account (y) or login to an existing account (n)?: ";
        std::cin >> account;
        std::string logAgain;

        while(true) {
            if(account == "y" || account == "Y") {
                std::cout << "Please enter your desired username: ";
                std::cin >> username;
                for (const string& value : usernameList) {
                    if (value == username) {
                        std::cout << "Sorry, this username has already been taken" << std::endl;
                        break;
                    } else if (value != username) {
                        usernameList.push_back(username);

                        std::cout << "Please enter your desired password: ";
                        std::cin >> password;
                        passwordList.push_back(password);
                    }

                    if (value != username) {
                        std::ofstream outfile("accounts.txt", std::ios::app);
                        outfile << username << " " << password << std::endl;
                        outfile.close();

                        std::cout << "You account has been saved. Log in? (y/n): ";
                        std::cin >> logAgain;
                        account = "n";
                        if(logAgain == "y" || logAgain == "Y") {
                            account = "n";
                            break;
                        } else {
                            std::cout << "Exiting program" << std::endl;
                            exit(0);
                        }
                    }
                }
            }

            if(account == "n" || account == "N") {
                std::cout << "Please enter your username: ";
                std::cin >> username;
                std::cout << "Please enter your password: ";
                std::cin >> password;
                break;
            } else if (account != "y") {
                std::cout << "Please enter y (create an account) or n (login to account): ";
                std::cin >> account;
            }
        }
    }

    bool validityCheck() {
        if(account == "n") {
            bool found = false;

            auto userIt = usernameList.begin();
            auto passIt = passwordList.begin();

            while(userIt != usernameList.end() && passIt != passwordList.end()) {
                if(*userIt == username && *passIt == password) {
                    found = true;
                    break;
                }
                ++userIt;
                ++passIt;
            }

            if(found) {
                std::cout << "Welcome to your account!" << std::endl;
                return true;
            } else {
                std::cout << "Sorry, your username or password was incorrect" << std::endl;
                return false;
            }
        }
        return false;
    }

    [[nodiscard]] std::string getUsername() const {
        return username;
    }
};

class dayofweek {
private:
    std::list <string> reminders{};
    std::string newRem;
    std::string currentDay;
    std::string receivedUsername;
public:

        explicit dayofweek(std::string  username) : receivedUsername(std::move(username)) {}

        void date() {
            std::cout << "What day of the week is it?: ";
            std::cin >> currentDay;

            if (!currentDay.empty()) {
                currentDay[0] = toupper(currentDay[0]);
                for (size_t i = 1; i < currentDay.size(); ++i)
                    currentDay[i] = tolower(currentDay[i]);
            }
        }

        void loadReminders() {
            reminders.clear();
            std::ifstream infile("reminders.txt");
            std::string u, d, r; // username, day, and reminder

            while (infile >> u >> d) {
                std::getline(infile >> std::ws, r);
                if (!r.empty() && currentDay == d && receivedUsername == u) {
                    if (ranges::find(reminders, r) == reminders.end()) {
                        reminders.push_back(r);
                    }
                }
            }

            infile.close();
        }

        void newInput() {
            std::cout << "Please enter your new Reminder: ";
            std::cin.ignore();
            getline(cin, newRem);

            for (const string& value : reminders) {
                if (value != newRem) {
                    std::ofstream outfile("reminders.txt", std::ios::app);
                    outfile << receivedUsername << " " << currentDay << " " << newRem << std::endl;
                    outfile.close();
                } else {
                    std::cout << "Reminder previously saved" << std::endl;
                }
            }
        }

        void displayInput() const {
            cout << "Reminders for " << currentDay << ":\n";
            for (const std::string& value : reminders) {
                std::cout << "- " << value << std::endl;
            }
        }
};

int main(int argc, char const *argv[]) {
    // login
    userInput input;
    input.loadAccountsFromFile();
    input.accountSetup();

    // reminders
    if (bool loggedIn = input.validityCheck()) {
        const std::string username = input.getUsername();
        std::string remAgain;
        while (true) {
            dayofweek day(username);
            day.date();
            day.loadReminders();
            day.newInput();
            day.loadReminders();
            day.displayInput();
            // repeat
            std::cout << "Set another reminder? (y/n): ";
            std::cin >> remAgain;
            if (remAgain == "n" || remAgain == "N") {
                std::cout << "Bye!";
                break;
            }
        }
    }
    return 0;
}
