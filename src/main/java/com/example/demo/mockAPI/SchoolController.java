package com.example.demo.mockAPI;

import com.example.demo.model.*;
import com.example.demo.model.Attendance;
import org.springframework.web.bind.annotation.*;
import java.time.LocalDateTime;

import java.util.List;


@RestController
@RequestMapping("/api")
public class SchoolController {

    // Mock data for Students
    @GetMapping("/students")
    public List<Student> getAllStudents() {
        Program program = new Program("Computer Engineering", "College of Engineering"); // Example program
        Role studentRole = new Role("Student"); // Create a Role instance for "Student"

// Correcting UserTable instances
        UserTable user1 = new UserTable("alice@example.com", "Alice123", "ALICE", studentRole);
        UserTable user2 = new UserTable("bob@example.com", "Bob123", "BOB", studentRole); // Removed 2L and fixed password field

        Student student1 = new Student("Alice", "alice@example.com", "password123", program, 12, user1);
        Student student2 = new Student("Bob", "bob@example.com", "password456", program, 11, user2);


        return List.of(student1, student2);
    }


    // Mock data for SSG Officers
    @GetMapping("/ssg-officers")
    public List<SSGOfficer> getAllSSGOfficers() {
        // Sample Response:
        /*
        [
            {
                "id": 1,
                "name": "John Doe",
                "position": "President",
                "email": "johndoe@example.com"
            },
            {
                "id": 2,
                "name": "Jane Smith",
                "position": "Vice President",
                "email": "janesmith@example.com"
            }
        ]
        */
        SSGOfficer officer1 = new SSGOfficer("John Doe", "President", "johndoe@example.com", "john");
        SSGOfficer officer2 = new SSGOfficer("Jane Smith", "Vice President", "janesmith@example.com", "john");
        return List.of(officer1, officer2);
    }

    // Mock data for Organizers
    @GetMapping("/organizers")
    public List<EventOrganizer> getAllOrganizers() {
        // Sample Response:
        /*
        [
            {
                "id": 1,
                "name": "Michael",
                "email": "michael@example.com"
            },
            {
                "id": 2,
                "name": "Sophia",
                "email": "sophia@example.com"
            }
        ]
        */
        EventOrganizer organizer1 = new EventOrganizer(1L, "Michael", "michael@example.com");
        EventOrganizer organizer2 = new EventOrganizer(2L, "Sophia", "sophia@example.com");
        return List.of(organizer1, organizer2);
    }

    // Mock data for getting individual Student by ID
    @GetMapping("/students/{id}")
    public Student getStudentById(@PathVariable Long id) {
        // Sample Response for /students/1
        /*
        {
            "id": 1,
            "name": "Alice",
            "gradeLevel": "12th Grade",
            "email": "alice@example.com"
        }
        */
        Program program = new Program("Computer Science", "Engineering College"); // Example program
        Role studentRole = new Role("Student"); // Example role
        UserTable user = new UserTable("alice@example.com", "Alice123", "ALICE", studentRole);

// Corrected Student instantiation
        return new Student("Alice", "alice@example.com", "Alice123", program, 12, user);
    }

    // Mock data for getting individual SSG Officer by ID
    @GetMapping("/ssg-officers/{id}")
    public SSGOfficer getSSGOfficerById(@PathVariable Long id) {
        // Sample Response for /ssg-officers/1
        /*
        {
            "id": 1,
            "name": "John Doe",
            "position": "President",
            "email": "johndoe@example.com"
        }
        */
        return new SSGOfficer("John Doe", "President", "johndoe@example.com", "securePassword123");
    }

    // Mock data for getting individual Organizer by ID
    @GetMapping("/organizers/{id}")
    public EventOrganizer getOrganizerById(@PathVariable Long id) {
        // Sample Response for /organizers/1
        /*
        {
            "id": 1,
            "name": "Michael",
            "email": "michael@example.com"
        }
        */
        return new EventOrganizer(id, "Michael", "michael@example.com");
    }

    // Mock data for attendance records
    public List<Attendance> getAllAttendance() {
        // Creating sample Student and Event objects
        Program program = new Program("Computer Science", "Engineering College");
        Role studentRole = new Role("Student");


        UserTable user1 = new UserTable("alice@example.com", "Alice123", "password123", studentRole);
        Student student1 = new Student("Alice", "alice@example.com", "password123", program, 12, user1);

        UserTable user2 = new UserTable("bob@example.com", "Bob123", "password123", studentRole);
        Student student2 = new Student("Bob", "bob@example.com", "password123", program, 11, user2);

        // Fixed EventOrganizer object
        EventOrganizer organizer = new EventOrganizer(1L, "johndoe@example.com", "securePassword123");


// Fixed Event Objects
        Event event1 = new Event("Seminar on AI", LocalDateTime.of(2025, 3, 2, 10, 0), "Conference Hall", organizer);
        Event event2 = new Event("Workshop on Robotics", LocalDateTime.of(2025, 3, 2, 14, 0), "Engineering Lab", organizer);
        // Creating Attendance records
        Attendance record1 = new Attendance(student1, event1, LocalDateTime.of(2025, 3, 2, 10, 5), "Present");
        Attendance record2 = new Attendance(student2, event2, LocalDateTime.of(2025, 3, 2, 14, 15), "Absent");

        return List.of(record1, record2);
    }
    // Mock data for getting individual attendance record by ID
    @GetMapping("/attendance/{id}")
    public Attendance getAttendanceById(@PathVariable Long id) {
        // Create necessary objects first
        Student student = new Student("Alice", "alice@example.com", "securePassword123", new Program("Computer Science", "Engineering"), 12, new UserTable("alice@example.com", "Alice123", "password123", new Role("Student")));
        Event event = new Event("Seminar on AI", LocalDateTime.of(2025, 3, 2, 10, 0), "Main Hall", new EventOrganizer(1L, "organizer@example.com", "password123"));

// Return Attendance object with correct parameters
        return new Attendance(student, event, LocalDateTime.of(2025, 3, 2, 10, 0), "Present");

    }
}

