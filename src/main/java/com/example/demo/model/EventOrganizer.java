package com.example.demo.model;

import jakarta.persistence.*;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

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
    private String password; // This should be stored as a hashed password

    // Default constructor (needed for JPA)
    public EventOrganizer() {
    }


    // Parameterized Constructor (with password hashing)
    public EventOrganizer(long organizerID, String email, String password) {
        this.organizerID = organizerID;
        this.email = email;
        this.password = hashPassword(password); // Hash password upon creation
    }

    // Hash the password using BCrypt
    private String hashPassword(String password) {
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
        return passwordEncoder.encode(password);
    }

    // Getters and Setters
    public Long getOrganizerID() { return organizerID; }
    public void setOrganizerID(Long organizerID) { this.organizerID = organizerID; }

    public String getOrganizerName() { return organizerName; }
    public void setOrganizerName(String organizerName) { this.organizerName = organizerName; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getPassword() { return password; }
    public void setPassword(String password) {
        this.password = hashPassword(password); // Ensure password is always hashed
    }
}