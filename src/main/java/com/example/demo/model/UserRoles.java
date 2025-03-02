package com.example.demo.model;

import jakarta.persistence.*;

@Entity
@Table(name = "user_roles")
public class UserRoles {
    @EmbeddedId
    private UserRoleKey id; // Composite Key

    @ManyToOne
    @MapsId("userID") // Maps to composite key
    @JoinColumn(name = "userID", nullable = false)
    private UserTable user;

    @ManyToOne
    @MapsId("roleID") // Maps to composite key
    @JoinColumn(name = "roleID", nullable = false)
    private Role role;

    // Getters and Setters
    public UserRoleKey getId() { return id; }
    public void setId(UserRoleKey id) { this.id = id; }

    public UserTable getUser() { return user; }
    public void setUser(UserTable user) { this.user = user; }

    public Role getRole() { return role; }
    public void setRole(Role role) { this.role = role; }
}