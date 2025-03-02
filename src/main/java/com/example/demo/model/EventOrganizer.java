package com.example.demo.model;

import jakarta.persistence.*;

@Entity
@Table(name = "event_organizer")
public class EventOrganizer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long organizerID;

    @Column(nullable = false)
    private String organizerName;

    @Column(nullable = false, unique = true)
    private String email;

    @Column(nullable = false)
    private String password; // Store as a hashed password for security

    // Getters and Setters
    public Long getOrganizerID() { return organizerID; }
    public void setOrganizerID(Long organizerID) { this.organizerID = organizerID; }

    public String getOrganizerName() { return organizerName; }
    public void setOrganizerName(String organizerName) { this.organizerName = organizerName; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
}