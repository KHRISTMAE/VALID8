package com.example.demo.mockAPI;

import org.springframework.web.bind.annotation.*;
import com.example.demo.model.Student;
import com.example.demo.model.SSGOfficer;
import com.example.demo.model.EventOrganizer;
import java.util.List;

@RestController
@RequestMapping("/api")
public class SchoolController {

    // Mock data for Students
    @GetMapping("/students")
    public List<Student> getAllStudents() {
        // Sample Response:
        /*
        [
            {
                "id": 1,
                "name": "Alice",
                "gradeLevel": "12th Grade",
                "email": "alice@example.com"
            },
            {
                "id": 2,
                "name": "Bob",
                "gradeLevel": "11th Grade",
                "email": "bob@example.com"
            }
        ]
        */
        Student student1 = new Student(1L, "Alice", "12th Grade", "alice@example.com");
        Student student2 = new Student(2L, "Bob", "11th Grade", "bob@example.com");
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
        SSGOfficer officer1 = new SSGOfficer(1L, "John Doe", "President", "johndoe@example.com");
        SSGOfficer officer2 = new SSGOfficer(2L, "Jane Smith", "Vice President", "janesmith@example.com");
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
        return new Student(id, "Alice", "12th Grade", "alice@example.com");
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
        return new SSGOfficer(id, "John Doe", "President", "johndoe@example.com");
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
    @GetMapping("/attendance")
    public List<Attendance> getAllAttendance() {
        Attendance record1 = new Attendance(1L, 101L, 21l, "2025-03-02", "Present");
        Attendance record2 = new Attendance(2L, 102L, 22l, "2025-03-02", "Absent");
        return List.of(record1, record2);
    }

    // Mock data for getting individual attendance record by ID
    @GetMapping("/attendance/{id}")
    public Attendance getAttendanceById(@PathVariable Long id) {
        return new Attendance(id, 101L, 21l, "2025-03-02", "Present");
    }
}

