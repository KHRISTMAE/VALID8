package com.example.demo.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "event")
public class Event {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long eventID;

    @Column(nullable = false)
    private String eventName;

    @Column(nullable = false)
    private LocalDateTime dateAndTime;

    @Column(nullable = false)
    private String location;

    @ManyToOne
    @JoinColumn(name = "organizerID", nullable = false) // FK constraint
    private EventOrganizer organizer;

    // Default constructor (needed for JPA)
    public Event() {
    }

    // Parameterized Constructor
    public Event(String eventName, LocalDateTime dateAndTime, String location, EventOrganizer organizer) {
        this.eventName = eventName;
        this.dateAndTime = dateAndTime;
        this.location = location;
        this.organizer = organizer;
    }

    // Getters and Setters
    public Long getEventID() { return eventID; }
    public void setEventID(Long eventID) { this.eventID = eventID; }

    public String getEventName() { return eventName; }
    public void setEventName(String eventName) { this.eventName = eventName; }

    public LocalDateTime getDateAndTime() { return dateAndTime; }
    public void setDateAndTime(LocalDateTime dateAndTime) { this.dateAndTime = dateAndTime; }

    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }

    public EventOrganizer getOrganizer() { return organizer; }
    public void setOrganizer(EventOrganizer organizer) { this.organizer = organizer; }
}