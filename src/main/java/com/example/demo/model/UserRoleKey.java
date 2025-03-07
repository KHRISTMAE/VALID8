package com.example.demo.model;

import java.io.Serializable;
import java.util.Objects;
import jakarta.persistence.*;

@Embeddable
public class UserRoleKey implements Serializable {
    private static final long serialVersionUID = 1L; // ✅ Added serialVersionUID

    @Column(name = "userID")
    private Long userID;

    @Column(name = "roleID")
    private Long roleID;

    // ✅ No-Args Constructor (Required for JPA)
    public UserRoleKey() {}

    // ✅ Parameterized Constructor
    public UserRoleKey(Long userID, Long roleID) {
        this.userID = userID;
        this.roleID = roleID;
    }

    // ✅ Getters and Setters
    public Long getUserID() { return userID; }
    public void setUserID(Long userID) { this.userID = userID; }

    public Long getRoleID() { return roleID; }
    public void setRoleID(Long roleID) { this.roleID = roleID; }

    // ✅ Equals and HashCode (Required for Composite Key)
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

    // ✅ Added toString() for Debugging
    @Override
    public String toString() {
        return "UserRoleKey{" +
                "userID=" + userID +
                ", roleID=" + roleID +
                '}';
    }
}