package com.example.demo.model;

import jakarta.persistence.*;

@Entity
@Table(name = "user_roles")
public class UserRoles {
    @EmbeddedId
    private UserRoleKey id = new UserRoleKey(); // ✅ Initialize Composite Key

    @ManyToOne
    @MapsId("userID") // ✅ Maps to userID in Composite Key
    @JoinColumn(name = "userID", nullable = false)
    private UserTable user;

    @ManyToOne
    @MapsId("roleID") // ✅ Maps to roleID in Composite Key
    @JoinColumn(name = "roleID", nullable = false)
    private Role role;

    // ✅ Default Constructor (Required for JPA)
    public UserRoles() {}

    // ✅ Parameterized Constructor to Auto-Generate `id`
    public UserRoles(UserTable user, Role role) {
        this.user = user;
        this.role = role;
        this.id = new UserRoleKey(user.getUserID(), role.getRoleID()); // ✅ Auto-assign ID
    }

    // ✅ Getters and Setters
    public UserRoleKey getId() { return id; }
    public void setId(UserRoleKey id) { this.id = id; }

    public UserTable getUser() { return user; }
    public void setUser(UserTable user) {
        this.user = user;
        this.id.setUserID(user.getUserID()); // ✅ Keep ID in sync
    }

    public Role getRole() { return role; }
    public void setRole(Role role) {
        this.role = role;
        this.id.setRoleID(role.getRoleID()); // ✅ Keep ID in sync
    }
}