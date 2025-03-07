package com.example.demo.model;

import jakarta.persistence.*;

@Entity
@Table(name = "program", uniqueConstraints = {
        @UniqueConstraint(columnNames = "programName") // ✅ Prevents duplicate programs
})
public class Program {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long programID;

    @Column(nullable = false, length = 100, unique = true) // ✅ Limits name length
    private String programName;

    @Column(nullable = false, length = 100) // ✅ Limits college name length
    private String college;

    // ✅ Default Constructor (required for JPA)
    public Program() {}

    // ✅ Parameterized Constructor (for easier object creation)
    public Program(String programName, String college) {
        this.programName = programName;
        this.college = college;
    }

    // ✅ Getters and Setters
    public Long getProgramID() { return programID; }
    public void setProgramID(Long programID) { this.programID = programID; }

    public String getProgramName() { return programName; }
    public void setProgramName(String programName) { this.programName = programName; }

    public String getCollege() { return college; }
    public void setCollege(String college) { this.college = college; }
}