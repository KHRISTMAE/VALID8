package com.example.demo.model;

import jakarta.persistence.Embeddable;
import java.io.Serializable;
import java.util.Objects;

@Embeddable
public class OfficerEventKey implements Serializable {
    private Long officerID;
    private Long eventID;

    // Constructors
    public OfficerEventKey() {}

    public OfficerEventKey(Long officerID, Long eventID) {
        this.officerID = officerID;
        this.eventID = eventID;
    }

    // Getters and Setters
    public Long getOfficerID() { return officerID; }
    public void setOfficerID(Long officerID) { this.officerID = officerID; }

    public Long getEventID() { return eventID; }
    public void setEventID(Long eventID) { this.eventID = eventID; }

    // Override equals() and hashCode()
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        OfficerEventKey that = (OfficerEventKey) o;
        return Objects.equals(officerID, that.officerID) && Objects.equals(eventID, that.eventID);
    }

    @Override
    public int hashCode() {
        return Objects.hash(officerID, eventID);
    }
}