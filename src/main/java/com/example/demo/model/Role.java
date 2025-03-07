package com.example.demo.model;

import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "role", uniqueConstraints = {
        @UniqueConstraint(columnNames = "roleName") // ✅ Prevents duplicate roles
})
public class Role {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long roleID; // ✅ Primary Key

    @Column(unique = true, nullable = false, length = 50) // ✅ Limit role name length
    private String roleName;

    @OneToMany(mappedBy = "role", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<UserTable> users = new ArrayList<>(); // ✅ Prevents NullPointerException

    // ✅ Default Constructor (Required for JPA)
    public Role() {}

    // ✅ Parameterized Constructor
    public Role(String roleName) {
        this.roleName = roleName;
    }

    // ✅ Getters and Setters
    public Long getRoleID() { return roleID; }
    public void setRoleID(Long roleID) { this.roleID = roleID; }

    public String getRoleName() { return roleName; }
    public void setRoleName(String roleName) { this.roleName = roleName; }

    public List<UserTable> getUsers() { return users; }
    public void setUsers(List<UserTable> users) { this.users = users; }
}
