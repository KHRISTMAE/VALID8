package com.example.demo.model;

import jakarta.persistence.*;

@Entity
@Table(name = "course")
public class Course {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long courseID;

    @Column(nullable = false)
    private String courseName;

    @Column(nullable = false)
    private String college;

    // Getters and Setters
    public Long getCourseID() { return courseID; }
    public void setCourseID(Long courseID) { this.courseID = courseID; }

    public String getCourseName() { return courseName; }
    public void setCourseName(String courseName) { this.courseName = courseName; }

    public String getCollege() { return college; }
    public void setCollege(String college) { this.college = college; }
}
