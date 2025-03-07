package com.example.demo.api;

import com.example.demo.model.EventOrganizer;
import com.example.demo.repository.EventOrganizerRepository;
import com.example.demo.repository.SSGOfficerRepository;
import com.example.demo.model.SSGOfficer;
import com.example.demo.model.Student;
import com.example.demo.repository.StudentRepository;
import com.example.demo.model.Event;
import com.example.demo.repository.EventRepository;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.Optional;
import java.util.List;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;


@RestController
@RequestMapping("/api/officers")
public class Controller2 {

    @Autowired
    private SSGOfficerRepository officerRepository;

    @Autowired
    private StudentRepository studentRepo;

    @Autowired
    private EventRepository eventRepo;

    @Autowired
    private EventOrganizerRepository organizerRepository;

    // Create an officer
    @PostMapping("/officer")
    public SSGOfficer createOfficer( @RequestBody SSGOfficer officer) {
        // Example Response (201 Created):
        // {
        //     "officerID": 1,
        //     "name": "John Doe",
        //     "position": "President",
        //     "email": "johndoe@example.com"
        // }
        return officerRepository.save(officer);
    }

    // Create a student
    @PostMapping("/student")
    public Student createStudent( @RequestBody Student student) {
        // Example Response (201 Created):
        // {
        //     "studentID": 1,
        //     "studentName": "Jane Doe",
        //     "email": "janedoe@example.com"
        // }
        return studentRepo.save(student);
    }

    // Create an event
    @PostMapping("/event")
    public Event createEvent( @RequestBody Event event) {
        // Example Response (201 Created):
        // {
        //     "eventID": 1,
        //     "eventName": "Annual Science Fair",
        //     "location": "Room 101",
        //     "dateTime": "2025-03-10T10:00:00"
        // }
        return eventRepo.save(event);
    }

    // Create an event organizer
    @PostMapping("/organizer")
    public EventOrganizer createOrganizer( @RequestBody EventOrganizer organizer) {
        // Example Response (201 Created):
        // {
        //     "organizerID": 1,
        //     "organizerName": "Alice Johnson",
        //     "email": "alicej@example.com"
        // }
        return organizerRepository.save(organizer);
    }

    // Get all officers
    @GetMapping("/officers")
    public List<SSGOfficer> getAllOfficers() {
        // Example Response (200 OK):
        // [
        //     {
        //         "officerID": 1,
        //         "name": "John Doe",
        //         "position": "President",
        //         "email": "johndoe@example.com"
        //     },
        //     {
        //         "officerID": 2,
        //         "name": "Jane Smith",
        //         "position": "Vice President",
        //         "email": "janesmith@example.com"
        //     }
        // ]
        return officerRepository.findAll();
    }

    // Get an officer by ID
    @GetMapping("/officer/{id}")
    public Optional<SSGOfficer> getOfficerById(@PathVariable Long id) {
        // Example Response (200 OK):
        // {
        //     "officerID": 1,
        //     "name": "John Doe",
        //     "position": "President",
        //     "email": "johndoe@example.com"
        // }

        // Example Response (404 Not Found):
        // {
        //     "message": "Officer not found"
        // }
        return officerRepository.findById(id);
    }

    // Get all students
    @GetMapping("/students")
    public List<Student> getAllStudents() {
        // Example Response (200 OK):
        // [
        //     {
        //         "studentID": 1,
        //         "studentName": "Jane Doe",
        //         "email": "janedoe@example.com"
        //     }
        // ]
        return studentRepo.findAll();
    }

    // Get a student by ID
    @GetMapping("/student/{id}")
    public Optional<Student> getStudentById(@PathVariable Long id) {
        // Example Response (200 OK):
        // {
        //     "studentID": 1,
        //     "studentName": "Jane Doe",
        //     "email": "janedoe@example.com"
        // }

        // Example Response (404 Not Found):
        // {
        //     "message": "Student not found"
        // }
        return studentRepo.findById(id);
    }

    // Get all events
    @GetMapping("/events")
    public List<Event> getAllEvents() {
        // Example Response (200 OK):
        // [
        //     {
        //         "EventID": 1,
        //         "eventName": "Annual Science Fair",
        //         "location": "Room 101",
        //         "dateTime": "2025-03-10T10:00:00"
        //     }
        // ]
        return eventRepo.findAll();
    }

    // Get an event by ID
    @GetMapping("/event/{id}")
    public Optional<Event> getEventById(@PathVariable Long id) {
        // Example Response (200 OK):
        // {
        //     "EventID": 1,
        //     "eventName": "Annual Science Fair",
        //     "location": "Room 101",
        //     "dateTime": "2025-03-10T10:00:00"
        // }

        // Example Response (404 Not Found):
        // {
        //     "message": "Event not found"
        // }
        return eventRepo.findById(id);
    }

    // Update an officer
    @PutMapping("/officer/{id}")
    public SSGOfficer updateOfficer(@PathVariable Long id, @RequestBody SSGOfficer officerDetails) {
        // Example Response (200 OK):
        // {
        //     "officerID": 1,
        //     "name": "John Doe",
        //     "position": "President",
        //     "email": "updatedemail@example.com"
        // }
        return officerRepository.findById(id).map(officer -> {
            officer.setName(officerDetails.getName());
            officer.setPosition(officerDetails.getPosition());
            officer.setEmail(officerDetails.getEmail());
            officer.setPassword(officerDetails.getPassword());
            return officerRepository.save(officer);
        }).orElseThrow(() -> new RuntimeException("Officer not found"));
    }

    // Delete an officer
    @DeleteMapping("/officer/{id}")
    public void deleteOfficer(@PathVariable Long id) {
        // Example Response (204 No Content):
        // No content response indicating that the officer was successfully deleted
        officerRepository.deleteById(id);
    }

    // Update a student
    @PutMapping("/student/{id}")
    public Student updateStudent(@PathVariable Long id, @RequestBody Student studentDetails) {
        // Example Response (200 OK):
        // {
        //     "StudentID": 1,
        //     "studentName": "Updated Student Name",
        //     "email": "updatedemail@example.com"
        // }
        return studentRepo.findById(id).map(student -> {
            student.setStudentName(studentDetails.getStudentName());
            student.setEmail(studentDetails.getEmail());
            student.setPassword(studentDetails.getPassword());
            return studentRepo.save(student);
        }).orElseThrow(() -> new RuntimeException("Student not found"));
    }

    @DeleteMapping("/student/{id}")
    public ResponseEntity<String> deleteStudent(@PathVariable Long id) {
        // Check if the student exists before attempting to delete
        if (studentRepo.existsById(id)) {
            studentRepo.deleteById(id);
            // Return a response indicating success
            return ResponseEntity.status(HttpStatus.OK).body("Student successfully deleted.");
        } else {
            // Return a response indicating the student was not found
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Student not found.");
        }
    }

    // Update an event
    @PutMapping("/event/{id}")
    public Event updateEvent(@PathVariable Long id, @RequestBody Event eventDetails) {
        // Example Response (200 OK):
        // {
        //     "EventID": 1,
        //     "eventName": "Updated Event Name",
        //     "location": "Updated Location",
        //     "dateTime": "2025-03-12T10:00:00"
        // }
        return eventRepo.findById(id).map(event -> {
            event.setEventName(eventDetails.getEventName());
            event.setLocation(eventDetails.getLocation());
            event.setDateAndTime(eventDetails.getDateAndTime());
            return eventRepo.save(event);
        }).orElseThrow(() -> new RuntimeException("Event not found"));
    }

    // Delete an event
    @DeleteMapping("/event/{id}")
    public void deleteEvent(@PathVariable Long id) {
        // Example Response (204 No Content):
        // No content response indicating that the event was successfully deleted
        eventRepo.deleteById(id);
    }

    // Update an event organizer
    @PutMapping("/organizer/{id}")
    public EventOrganizer updateOrganizer(@PathVariable Long id, @RequestBody EventOrganizer organizerDetails) {
        // Example Response (200 OK):
        // {
        //     "organizerID": 1,
        //     "organizerName": "Updated Organizer Name",
        //     "email": "updatedemail@example.com"
        // }
        return organizerRepository.findById(id).map(organizer -> {
            organizer.setOrganizerName(organizerDetails.getOrganizerName());
            organizer.setEmail(organizerDetails.getEmail());
            organizer.setPassword(organizerDetails.getPassword());
            return organizerRepository.save(organizer);
        }).orElseThrow(() -> new RuntimeException("Organizer not found"));
    }

    // Delete an event organizer
    @DeleteMapping("/organizer/{id}")
    public void deleteOrganizer(@PathVariable Long id) {
        // Example Response (204 No Content):
        // No content response indicating that the organizer was successfully deleted
        organizerRepository.deleteById(id);
    }
}
