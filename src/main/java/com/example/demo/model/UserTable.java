package com.example.demo.model;

import jakarta.persistence.*;

@Entity
@Table(name = "user_table")
public class UserTable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userID;

    @ManyToOne
    @JoinColumn(name = "roleID", nullable = false)
    private Role role;

    @Column(unique = true, nullable = false)
    private String email;

    @Column(unique = true, nullable = false)
    private String username;

    @OneToOne
    @JoinColumn(name = "faceID")
    private FaceEntity face;

    // Getters and Setters
    public Long getUserID() { return userID; }
    public void setUserID(Long userID) { this.userID = userID; }

    public Role getRole() { return role; }
    public void setRole(Role role) { this.role = role; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }

    public FaceEntity getFace() { return face; }
    public void setFace(FaceEntity face) { this.face = face; }
}
