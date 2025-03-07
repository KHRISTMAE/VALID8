package com.example.demo.model;

import jakarta.persistence.*;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

@Entity
@Table(name = "ssg_officer")
public class SSGOfficer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long officerID;

    @Column(nullable = false, length = 100) // ✅ Prevent overly long names
    private String name;

    @Column(nullable = false, length = 50) // ✅ Position should have a limit
    private String position;

    @Column(unique = true, nullable = false, length = 100) // ✅ Limit email length
    private String email;

    @Column(nullable = false)
    private String password; // ✅ Store hashed password

    // ✅ Default Constructor (Required for JPA)
    public SSGOfficer() {}

    // ✅ Correct Parameterized Constructor with Password Hashing
    public SSGOfficer(String name, String position, String email, String password) {
        this.name = name;
        this.position = position;
        this.email = email;
        this.password = hashPassword(password);
    }

    // ✅ Hash the password using BCrypt
    private String hashPassword(String password) {
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
        return passwordEncoder.encode(password);
    }

    // ✅ Getters and Setters
    public Long getOfficerID() { return officerID; }
    public void setOfficerID(Long officerID) { this.officerID = officerID; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getPosition() { return position; }
    public void setPosition(String position) { this.position = position; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getPassword() { return password; }
    public void setPassword(String password) {
        this.password = hashPassword(password);
    }
}