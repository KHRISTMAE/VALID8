package com.example.demo.model;

import jakarta.persistence.*;

@Entity
@Table(name = "officer_event")
public class Officer_Event {
    @EmbeddedId
    private OfficerEventKey id;

    @ManyToOne
    @MapsId("officerID")
    @JoinColumn(name = "officerID", nullable = false)
    private SSGOfficer officer;

    @ManyToOne
    @MapsId("eventID")
    @JoinColumn(name = "eventID", nullable = false)
    private Event event;

    // Constructors
    public Officer_Event() {}

    public Officer_Event(SSGOfficer officer, Event event) {
        this.id = new OfficerEventKey(officer.getOfficerID(), event.getEventID());
        this.officer = officer;
        this.event = event;
    }

    // Getters and Setters
    public OfficerEventKey getId() { return id; }
    public void setId(OfficerEventKey id) { this.id = id; }

    public SSGOfficer getOfficer() { return officer; }
    public void setOfficer(SSGOfficer officer) { this.officer = officer; }

    public Event getEvent() { return event; }
    public void setEvent(Event event) { this.event = event; }
}