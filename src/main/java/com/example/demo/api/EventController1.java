/*package com.example.demo.api;

import com.example.demo.model.Event;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("/api/events")
public class EventController1 {

    private final EventService eventService;

    public EventController1(EventService eventService) {
        this.eventService = eventService;
    }

    // Create Event
    @PostMapping("/create")
    public ResponseEntity<Map<String, Object>> createEvent(@RequestBody Event event) {
        try {
            Event newEvent = eventService.createEvent(event);
            Map<String, Object> response = new HashMap<>();
            response.put("message", "Event successfully created!");
            response.put("eventId", newEvent.getEventID());
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            return ResponseEntity.badRequest().body(Map.of("error", "Failed to create event: " + e.getMessage()));
        }
    }


    // ✅ Edit Event
    @PutMapping("/edit/{eventId}")
    public ResponseEntity<Map<String, Object>> editEvent(@PathVariable int eventId, @RequestBody Event event) {
        Optional<Event> updatedEvent = eventService.editEvent(eventId, event);
        if (updatedEvent.isPresent()) {
            Map<String, Object> response = new HashMap<>();
            response.put("message", "Event successfully updated!");
            return ResponseEntity.ok(response);
        } else {
            return ResponseEntity.badRequest().body(Map.of("error", "Event not found"));
        }
    }

    // ✅ Delete Event
    @DeleteMapping("/delete/{eventId}")
    public ResponseEntity<Map<String, Object>> deleteEvent(@PathVariable int eventId) {
        boolean deleted = eventService.deleteEvent(eventId);
        if (deleted) {
            return ResponseEntity.ok(Map.of("message", "Event successfully deleted or cancelled"));
        } else {
            return ResponseEntity.badRequest().body(Map.of("error", "Event not found"));
        }
    }
}*/
