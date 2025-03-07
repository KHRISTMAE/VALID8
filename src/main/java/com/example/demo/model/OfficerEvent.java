package com.example.demo.model;

import jakarta.persistence.*;

@Entity
@Table(name = "officer_event") // ✅ Correctly mapped to PostgreSQL table
public class OfficerEvent { // ✅ Changed class name for better Java conventions
    @EmbeddedId
    private OfficerEventKey id;

    @ManyToOne
    @MapsId("officerID") // ✅ Maps the FK from the composite key
    @JoinColumn(name = "officerID", nullable = false)
    private SSGOfficer officer;

    @ManyToOne
    @MapsId("eventID") // ✅ Maps the FK from the composite key
    @JoinColumn(name = "eventID", nullable = false)
    private Event event;

    // ✅ Default Constructor (required for JPA)
    public OfficerEvent() {}

    // ✅ Parameterized Constructor
    public OfficerEvent(SSGOfficer officer, Event event) {
        this.id = new OfficerEventKey(officer.getOfficerID(), event.getEventID());
        this.officer = officer;
        this.event = event;
    }

    // ✅ Getters and Setters
    public OfficerEventKey getId() { return id; }
    public void setId(OfficerEventKey id) { this.id = id; }

    public SSGOfficer getOfficer() { return officer; }
    public void setOfficer(SSGOfficer officer) { this.officer = officer; }

    public Event getEvent() { return event; }
    public void setEvent(Event event) { this.event = event; }
}