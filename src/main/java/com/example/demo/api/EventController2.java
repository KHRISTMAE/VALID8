package com.example.demo.api;

import com.example.demo.model.Event;
import com.example.demo.repository.EventRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/events")
public class EventController2 {

    // Injecting the EventRepository to interact with the database
    @Autowired
    private EventRepository eventRepository;

    // Create a new event (POST method)
    @PostMapping("/")
    public Event createEvent(@RequestBody Event event) {
        // The request body should contain event details like event name, location, date, etc.
        // Example JSON format:
        // {
        //     "eventName": "Annual Science Fair",
        //     "location": "Room 101",
        //     "dateTime": "2025-03-10T10:00:00"
        // }
        return eventRepository.save(event); // Save the event in the database and return it
    }

    // Get all events (GET method)
    @GetMapping("/")
    public List<Event> getAllEvents() {
        // This endpoint will return a list of all the events stored in the database
        // Example response:
        // [
        //     {
        //         "eventID": 1,
        //         "eventName": "Annual Science Fair",
        //         "location": "Room 101",
        //         "dateTime": "2025-03-10T10:00:00"
        //     }
        // ]
        return eventRepository.findAll(); // Retrieve all events from the database
    }

    // Get an event by its ID (GET method with path variable)
    @GetMapping("/{id}")
    public Optional<Event> getEventById(@PathVariable Long id) {
        // This endpoint will return a single event by its unique ID
        // If the event is found, it will return the event, otherwise it will return a "not found" message
        return eventRepository.findById(id); // Retrieve the event by ID from the database
    }

    // Update an event (PUT method)
    @PutMapping("/{id}")
    public Event updateEvent(@PathVariable Long id, @RequestBody Event eventDetails) {
        // The request body should contain updated event details
        // Example JSON format:
        // {
        //     "eventName": "Updated Event Name",
        //     "location": "Updated Location",
        //     "dateTime": "2025-03-12T10:00:00"
        // }

        return eventRepository.findById(id).map(event -> {
            // Update the event's fields with the details provided in the request body
            event.setEventName(eventDetails.getEventName());
            event.setLocation(eventDetails.getLocation());
            event.setDateTime(eventDetails.getDateTime());

            // Save the updated event and return it
            return eventRepository.save(event);
        }).orElseThrow(() -> new RuntimeException("Event not found")); // If event not found, throw error
    }

    // Delete an event (DELETE method)
    @DeleteMapping("/{id}")
    public void deleteEvent(@PathVariable Long id) {
        // This endpoint deletes an event by its ID
        // If the event is found, it will be deleted from the database
        eventRepository.deleteById(id); // Delete the event by ID from the database
    }
}
 /*
 package com.example.demo.api;

import com.example.demo.model.Event;
import com.example.demo.repository.EventRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/events")
public class EventController2 {

    // Injecting the EventRepository to interact with the database
    @Autowired
    private EventRepository eventRepository;

    // Create a new event (POST method)
    @PostMapping("/")
    public String createEvent(@RequestBody Event event) {
        // Save the event in the database
        eventRepository.save(event);

        // Return success message after creating the event
        return "Event successfully created: " + event.getEventName() + " on " + event.getDateTime();
        // Sample Response: "Event successfully created: Annual Science Fair on 2025-03-10T10:00:00"
    }

    // Get all events (GET method)
    @GetMapping("/")
    public List<Event> getAllEvents() {
        // Retrieve all events from the database
        return eventRepository.findAll();
    }

    // Get an event by its ID (GET method with path variable)
    @GetMapping("/{id}")
    public Optional<Event> getEventById(@PathVariable Long id) {
        // Retrieve the event by ID from the database
        return eventRepository.findById(id);
    }

    // Update an event (PUT method)
    @PutMapping("/{id}")
    public String updateEvent(@PathVariable Long id, @RequestBody Event eventDetails) {
        // Find the event and update its details
        return eventRepository.findById(id).map(event -> {
            // Update event details
            event.setEventName(eventDetails.getEventName());
            event.setLocation(eventDetails.getLocation());
            event.setDateTime(eventDetails.getDateTime());

            // Save the updated event and return success message
            eventRepository.save(event);
            // Sample Response: "Event successfully updated: Updated Event Name on 2025-03-12T10:00:00"
            return "Event successfully updated: " + event.getEventName() + " on " + event.getDateTime();
        }).orElseThrow(() -> new RuntimeException("Event not found"));
    }

    // Delete an event (DELETE method)
    @DeleteMapping("/{id}")
    public String deleteEvent(@PathVariable Long id) {
        // Delete the event by ID
        eventRepository.deleteById(id);

        // Return success message after deleting the event
        // Sample Response: "Event successfully deleted."
        return "Event successfully deleted.";
    }
}

  */