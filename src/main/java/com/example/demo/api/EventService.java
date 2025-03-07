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
        event.setEventID((long) eventIdCounter++);
        eventList.add(event);
        return event;
    }

    public Optional<Event> editEvent(int eventId, Event updatedEvent) {
        for (Event event : eventList) {
            if (event.getEventID() == eventId) {
                event.setEventName(updatedEvent.getEventName());
                event.setDateAndTime(updatedEvent.getDateAndTime());  // ✅ Fixed setter method
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
