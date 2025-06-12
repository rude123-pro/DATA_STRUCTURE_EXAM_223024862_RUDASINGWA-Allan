#include <iostream>  // Standard input/output stream library
#include <cstring>   // For string manipulation functions (strcpy, strcmp)
using namespace std; // Use standard namespace to avoid std:: prefixes

// Date structure to hold day, month, and year
struct Date {  // Use standard namespace to avoid std:: prefixes
    int day, month, year;  
};

// AttendanceRecord structure holds student ID, pointer to Date, and presence status
struct AttendanceRecord {
    char studentID[10];
    Date* date;
    bool present;
};

// Abstract base class for different report types
class ReportInterface {
public:
    // Pure virtual function to generate report from attendance records
    virtual void generate(const AttendanceRecord* recs, int n) = 0;
    virtual ~ReportInterface() {}  // Virtual destructor for proper cleanup
};

// DailyAttendanceReport class derived from ReportInterface
class DailyAttendanceReport : public ReportInterface {
public:
    // Override generate to print daily attendance for each record
    void generate(const AttendanceRecord* recs, int n) override {
        cout << "\n--- Daily Attendance Report ---\n";
        for (int i = 0; i < n; ++i) {
            cout << "Student ID: " << recs[i].studentID
                 << " | Date: " << recs[i].date->day << "/"
                 << recs[i].date->month << "/" << recs[i].date->year
                 << " | Status: " << (recs[i].present ? "Present" : "Absent") << endl;
        }
    }
};

// TrendAttendanceReport class derived from ReportInterface
class TrendAttendanceReport : public ReportInterface {
public:
    // Override generate to calculate and display attendance trends per student
    void generate(const AttendanceRecord* recs, int n) override {
        cout << "\n--- Attendance Trends ---\n";
        for (int i = 0; i < n; ++i) {
            int presentCount = 0;
            // Count how many times this student was present
            for (int j = 0; j < n; ++j) {
                if (strcmp(recs[i].studentID, recs[j].studentID) == 0 && recs[j].present)
                    presentCount++;
            }

            int totalDays = 0;
            // Count total attendance records for this student
            for (int j = 0; j < n; ++j) {
                if (strcmp(recs[i].studentID, recs[j].studentID) == 0)
                    totalDays++;
            }

            // Calculate presence percentage
            double rate = (totalDays == 0) ? 0 : (presentCount * 100.0) / totalDays;
            cout << "Student " << recs[i].studentID << ": " << presentCount
                 << "/" << totalDays << " Present (" << rate << "%)\n";
        }
    }
};

// AttendanceSystem class manages records and reports
class AttendanceSystem {
    AttendanceRecord* recs;     // Dynamic array of attendance records
    int size;                   // Current number of records
    ReportInterface** reports;  // Array of pointers to report objects
    int reportCount;            // Number of report types

public:
    // Constructor initializes member variables and report objects
    AttendanceSystem() {
        recs = nullptr;  // Initially no records
        size = 0;
        reportCount = 2; // We have two reports: daily and trend
        reports = new ReportInterface*[reportCount];  // Allocate array for reports
        reports[0] = new DailyAttendanceReport();    // Create daily report
        reports[1] = new TrendAttendanceReport();    // Create trend report
    }

    // Destructor to free dynamic memory
    ~AttendanceSystem() {
        for (int i = 0; i < size; ++i)
            delete recs[i].date;  // Delete each dynamically allocated Date
        delete[] recs;             // Delete attendance record array

        for (int i = 0; i < reportCount; ++i)
            delete reports[i];     // Delete report objects
        delete[] reports;          // Delete report pointers array
    }

    // Add a new attendance record, copying the input and duplicating the date dynamically
    void addAttendance(const AttendanceRecord& newRecord) {
        AttendanceRecord* temp = new AttendanceRecord[size + 1];  // Create new larger array
        for (int i = 0; i < size; ++i)
            temp[i] = recs[i];            // Copy existing records

        // Deep copy the date to avoid shared pointers
        temp[size].date = new Date(*newRecord.date);
        // Copy student ID string safely
        strcpy(temp[size].studentID, newRecord.studentID);
        temp[size].present = newRecord.present;

        delete[] recs;  // Delete old array
        recs = temp;    // Point to new array
        size++;         // Increase record count
        cout << "Attendance added!\n";
    }

    // Remove attendance record by index
    void removeAttendance(int index) {
        if (index < 0 || index >= size) {
            cout << "Invalid index.\n";
            return;
        }
        delete recs[index].date;  // Delete dynamically allocated date for the record

        AttendanceRecord* temp = new AttendanceRecord[size - 1];  // New smaller array
        for (int i = 0, j = 0; i < size; ++i) {
            if (i != index)             // Skip record to remove
                temp[j++] = recs[i];   // Copy other records
        }

        delete[] recs;  // Delete old array
        recs = temp;    // Update pointer
        size--;         // Decrease record count
        cout << "Attendance removed.\n";
    }

    // Generate all reports by calling their respective generate() functions
    void generateReports() {
        for (int i = 0; i < reportCount; ++i)
            reports[i]->generate(recs, size);
    }

    // Run method provides a menu-driven interface for user interaction
    void run() {
        int choice;
        while (true) {
            cout << "\nAttendance Report Generator:\n1. Add Attendance\n2. Remove Attendance\n3. Generate Reports\n4. Exit\nChoice: ";
            cin >> choice;
            cin.ignore();  // Clear newline character from input buffer

            if (choice == 1) {
                AttendanceRecord ar;          // Temporary record to add
                cout << "Student ID: ";
                cin.getline(ar.studentID, 10);  // Get student ID input

                ar.date = new Date();         // Dynamically allocate date
                cout << "Enter date (day month year): ";
                cin >> ar.date->day >> ar.date->month >> ar.date->year;
                cin.ignore();                 // Clear buffer again

                char status;
                cout << "Present? (y/n): ";
                cin >> status;
                ar.present = (status == 'y' || status == 'Y');  // Convert input to bool

                addAttendance(ar);            // Add the new record

                delete ar.date;               // Delete temporary date to avoid leak
            }
            else if (choice == 2) {
                int idx;
                cout << "Enter index to remove: ";
                cin >> idx;
                removeAttendance(idx);        // Remove record at index
            }
            else if (choice == 3) {
                generateReports();            // Generate all reports
            }
            else if (choice == 4) {
                cout << "Exiting...\n";
                break;                       // Exit the menu loop
            }
            else {
                cout << "Invalid choice.\n"; // Invalid input handling
            }
        }
    }
};

int main() {
	AttendanceSystem system; //create AttendanceSystem object
	system.run(); //Start interactive menu-driven program
	return 0;
	
}
