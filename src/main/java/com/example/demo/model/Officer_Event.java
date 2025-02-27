package com.example.demo.model;

import jakarta.persistence.*;

@Entity
@Table(name = "officer_event")
public class Officer_Event {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "officerID", nullable = false)
    private SSGOfficer officer;

    @ManyToOne
    @JoinColumn(name = "eventID", nullable = false)
    private Event event;

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public SSGOfficer getOfficer() { return officer; }
    public void setOfficer(SSGOfficer officer) { this.officer = officer; }

    public Event getEvent() { return event; }
    public void setEvent(Event event) { this.event = event; }
}
