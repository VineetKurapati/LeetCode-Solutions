#include <vector>
using namespace std;

class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int n = students.size();
        int mismatches = 0;

        while (!students.empty() && !sandwiches.empty()) {
            if (students.front() == sandwiches.front()) {
                students.erase(students.begin());
                sandwiches.erase(sandwiches.begin());
                mismatches = 0; // Reset mismatches when there's a match
            } else {
                // Mismatch, move the student to the end and increment mismatches
                students.push_back(students.front());
                students.erase(students.begin());
                mismatches++;
            }

            // If all students have been considered and there are still mismatches,
            // it means some students cannot be served, so return the count of mismatches
            if (mismatches == students.size())
                return mismatches;
        }

        return students.size(); // Return the count of remaining students
    }
};
