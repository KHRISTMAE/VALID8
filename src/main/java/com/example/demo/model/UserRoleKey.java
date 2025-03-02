package com.example.demo.model;

import java.io.Serializable;
import java.util.Objects;
import jakarta.persistence.*;

@Embeddable
public class UserRoleKey implements Serializable {
    @Column(name = "userID")
    private Long userID;

    @Column(name = "roleID")
    private Long roleID;

    // Constructors
    public UserRoleKey() {}
    public UserRoleKey(Long userID, Long roleID) {
        this.userID = userID;
        this.roleID = roleID;
    }

    // Getters and Setters
    public Long getUserID() { return userID; }
    public void setUserID(Long userID) { this.userID = userID; }

    public Long getRoleID() { return roleID; }
    public void setRoleID(Long roleID) { this.roleID = roleID; }

    // Equals and HashCode (Required for Composite Key)
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        UserRoleKey that = (UserRoleKey) o;
        return Objects.equals(userID, that.userID) && Objects.equals(roleID, that.roleID);
    }

    @Override
    public int hashCode() {
        return Objects.hash(userID, roleID);
    }
}