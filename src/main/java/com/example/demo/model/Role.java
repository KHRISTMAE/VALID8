package com.example.demo.model;

import jakarta.persistence.*;
import java.util.List;

@Entity
@Table(name = "role")
public class Role {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long roleID; // ✅ PK

    @Column(unique = true, nullable = false)
    private String roleName; // ✅ Present

    @OneToMany(mappedBy = "role", cascade = CascadeType.ALL)
    private List<UserTable> users;

    // Getters and Setters
    public Long getRoleID() { return roleID; }
    public void setRoleID(Long roleID) { this.roleID = roleID; }

    public String getRoleName() { return roleName; }
    public void setRoleName(String roleName) { this.roleName = roleName; }

    public List<UserTable> getUsers() { return users; }
    public void setUsers(List<UserTable> users) { this.users = users; }
}