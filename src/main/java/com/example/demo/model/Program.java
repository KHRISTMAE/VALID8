package com.example.demo.model;

import jakarta.persistence.*;

@Entity
@Table(name = "program")
public class Program {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long programID; // Changed from courseID to programID

    @Column(nullable = false)
    private String programName; // Changed from courseName to programName

    @Column(nullable = false)
    private String college;

    // Getters and Setters
    public Long getProgramID() { return programID; }
    public void setProgramID(Long programID) { this.programID = programID; }

    public String getProgramName() { return programName; }
    public void setProgramName(String programName) { this.programName = programName; }

    public String getCollege() { return college; }
    public void setCollege(String college) { this.college = college; }
}
