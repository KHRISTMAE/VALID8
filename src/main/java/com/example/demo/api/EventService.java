package com.example.demo.api;

import com.example.demo.model.Event;
import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class EventService {

    private final List<Event> eventList = new ArrayList<>();
    private int eventIdCounter = 1;

    public Event createEvent(Event event) {
        event.setEventID((long) eventIdCounter++); // Fix: Use instance method
        eventList.add(event);
        return event;
    }

    public Optional<Event> editEvent(int eventId, Event updatedEvent) {
        for (Event event : eventList) {
            if (event.getEventID() == eventId) { // Fix: Use instance method
                event.setEventName(updatedEvent.getEventName());
                event.setDateTime(updatedEvent.getDateTime());
                event.setLocation(updatedEvent.getLocation());
                event.setOrganizer(updatedEvent.getOrganizer());
                return Optional.of(event);
            }
        }
        return Optional.empty();
    }

    public boolean deleteEvent(int eventId) {
        return eventList.removeIf(event -> event.getEventID() == eventId);
    }
}

