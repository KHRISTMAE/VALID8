/*package com.example.demo.api;

import com.example.demo.model.Event;
import com.example.demo.repository.EventRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/events")
public class EventController2 {

    @Autowired
    private EventRepository eventRepository;

    // Create a new event (POST method)
    @PostMapping("/")
    public String createEvent(@RequestBody Event event) {
        eventRepository.save(event);
        return "Event successfully created: " + event.getEventName() + " on " + event.getDateAndTime();
    }

    // Get all events (GET method)
    @GetMapping("/")
    public List<Event> getAllEvents() {
        return eventRepository.findAll();
    }

    // Get an event by its ID (GET method with path variable)
    @GetMapping("/{id}")
    public Optional<Event> getEventById(@PathVariable Long id) {
        return eventRepository.findById(id);
    }

    // Update an event (PUT method)
    @PutMapping("/{id}")
    public String updateEvent(@PathVariable Long id, @RequestBody Event eventDetails) {
        return eventRepository.findById(id).map(event -> {
            event.setEventName(eventDetails.getEventName());
            event.setLocation(eventDetails.getLocation());
            event.setDateAndTime(eventDetails.getDateAndTime());  // ✅ Sakto na ang method call

            eventRepository.save(event);
            return "Event successfully updated: " + event.getEventName() + " on " + event.getDateAndTime();
        }).orElseThrow(() -> new RuntimeException("Event not found"));
    }

    // Delete an event (DELETE method)
    @DeleteMapping("/{id}")
    public String deleteEvent(@PathVariable Long id) {
        eventRepository.deleteById(id);
        return "Event successfully deleted.";
    }
}*/