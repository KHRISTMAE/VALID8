package com.example.demo.model;

import jakarta.persistence.*;
import java.util.Objects;

@Entity
@Table(name = "user_table")
public class UserTable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userID;

    @ManyToOne
    @JoinColumn(name = "roleID", nullable = false) // FK for Role
    private Role role;

    @Column(unique = true, nullable = false)
    private String email;

    @Column(unique = true, nullable = false)
    private String username;

    @Column(nullable = false)
    private String password; // ✅ Added password field

    // ✅ Constructors

    public UserTable(String email, String username, String password, Role role) {
        this.email = email;
        this.username = username;
        this.password = password;
        this.role = role;
    }

    // ✅ Getters and Setters
    public Long getUserID() { return userID; }
    public void setUserID(Long userID) { this.userID = userID; }

    public Role getRole() { return role; }
    public void setRole(Role role) { this.role = role; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }

    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }

    // ✅ Equals and HashCode (Required for Entity Comparisons)
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        UserTable userTable = (UserTable) o;
        return Objects.equals(userID, userTable.userID) &&
                Objects.equals(email, userTable.email) &&
                Objects.equals(username, userTable.username);
    }

    @Override
    public int hashCode() {
        return Objects.hash(userID, email, username);
    }

    // ✅ toString() for Debugging
    @Override
    public String toString() {
        return "UserTable{" +
                "userID=" + userID +
                ", role=" + role.getRoleName() +
                ", email='" + email + '\'' +
                ", username='" + username + '\'' +
                '}';
    }
}