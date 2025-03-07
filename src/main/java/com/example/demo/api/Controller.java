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

@RestController
@RequestMapping("/api/officers")
public class Controller {

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
    public SSGOfficer createOfficer(@RequestBody SSGOfficer officer) {
        return officerRepository.save(officer);
    }

    // Create a student
    @PostMapping("/student")
    public Student createStudent(@RequestBody Student student) {
        return studentRepo.save(student);
    }

    // Create an event
    @PostMapping("/event")
    public Event createEvent(@RequestBody Event event) {
        return eventRepo.save(event);
    }

    // Create an event organizer
    @PostMapping("/organizer")
    public EventOrganizer createOrganizer(@RequestBody EventOrganizer organizer) {
        return organizerRepository.save(organizer);
    }

    // Get all officers
    @GetMapping("/officers")
    public List<SSGOfficer> getAllOfficers() {
        return officerRepository.findAll();
    }

    // Get an officer by ID
    @GetMapping("/officer/{id}")
    public Optional<SSGOfficer> getOfficerById(@PathVariable Long id) {
        return officerRepository.findById(id);
    }

    // Get all students
    @GetMapping("/students")
    public List<Student> getAllStudents() {
        return studentRepo.findAll();
    }

    // Get a student by ID
    @GetMapping("/student/{id}")
    public Optional<Student> getStudentById(@PathVariable Long id) {
        return studentRepo.findById(id);
    }

    // Get all events
    @GetMapping("/events")
    public List<Event> getAllEvents() {
        return eventRepo.findAll();
    }

    // Get an event by ID
    @GetMapping("/event/{id}")
    public Optional<Event> getEventById(@PathVariable Long id) {
        return eventRepo.findById(id);
    }

    // Get all event organizers
    @GetMapping("/organizers")
    public List<EventOrganizer> getAllOrganizers() {
        return organizerRepository.findAll();
    }

    // Get an event organizer by ID
    @GetMapping("/organizer/{id}")
    public Optional<EventOrganizer> getOrganizerById(@PathVariable Long id) {
        return organizerRepository.findById(id);
    }

    // Update an officer
    @PutMapping("/officer/{id}")
    public SSGOfficer updateOfficer(@PathVariable Long id, @RequestBody SSGOfficer officerDetails) {
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
        officerRepository.deleteById(id);
    }

    // Update a student
    @PutMapping("/student/{id}")
    public Student updateStudent(@PathVariable Long id, @RequestBody Student studentDetails) {
        return studentRepo.findById(id).map(student -> {
            student.setStudentName(studentDetails.getStudentName());
            student.setEmail(studentDetails.getEmail());
            student.setPassword(studentDetails.getPassword());
            return studentRepo.save(student);
        }).orElseThrow(() -> new RuntimeException("Student not found"));
    }

    // Delete a student
    @DeleteMapping("/student/{id}")
    public void deleteStudent(@PathVariable Long id) {
        studentRepo.deleteById(id);
    }

    // Update an event
    @PutMapping("/event/{id}")
    public Event updateEvent(@PathVariable Long id, @RequestBody Event eventDetails) {
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
        eventRepo.deleteById(id);
    }

    // Update an event organizer
    @PutMapping("/organizer/{id}")
    public EventOrganizer updateOrganizer(@PathVariable Long id, @RequestBody EventOrganizer organizerDetails) {
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
        organizerRepository.deleteById(id);
    }
}
