package com.example.demo.model;

import jakarta.persistence.*;

@Entity
@Table(name = "ssg_officer")
public class SSGOfficer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long officerID;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String position;

    @Column(unique = true, nullable = false)
    private String email;

    @Column(nullable = false)
    private String password;

    // Getters and Setters
    public Long getOfficerID() { return officerID; }
    public void setOfficerID(Long officerID) { this.officerID = officerID; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getPosition() { return position; }
    public void setPosition(String position) { this.position = position; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
}
