package com.example.demo.model;

import jakarta.persistence.*;

@Entity
@Table(name = "face_entity")
public class FaceEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long faceID;

    @OneToOne(mappedBy = "face", cascade = CascadeType.ALL)
    private UserTable user;

    // Getters and Setters
    public Long getFaceID() { return faceID; }
    public void setFaceID(Long faceID) { this.faceID = faceID; }

    public UserTable getUser() { return user; }
    public void setUser(UserTable user) { this.user = user; }
}
