package com.example.demo.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "attendance")
public class Attendance {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long attendanceID;

    @ManyToOne
    @JoinColumn(name = "studentID", nullable = false)
    private Student student;

    @ManyToOne
    @JoinColumn(name = "eventID", nullable = false) // Added missing FK
    private Event event;

    private LocalDateTime checkInTime;
    private LocalDateTime midEventCheckpoint;
    private LocalDateTime checkOutTime;

    @Column(nullable = false)
    private String status;

    // Getters and Setters
    public Long getAttendanceID() { return attendanceID; }
    public void setAttendanceID(Long attendanceID) { this.attendanceID = attendanceID; }

    public Student getStudent() { return student; }
    public void setStudent(Student student) { this.student = student; }

    public Event getEvent() { return event; } // Getter for Event FK
    public void setEvent(Event event) { this.event = event; } // Setter for Event FK

    public LocalDateTime getCheckInTime() { return checkInTime; }
    public void setCheckInTime(LocalDateTime checkInTime) { this.checkInTime = checkInTime; }

    public LocalDateTime getMidEventCheckpoint() { return midEventCheckpoint; }
    public void setMidEventCheckpoint(LocalDateTime midEventCheckpoint) { this.midEventCheckpoint = midEventCheckpoint; }

    public LocalDateTime getCheckOutTime() { return checkOutTime; }
    public void setCheckOutTime(LocalDateTime checkOutTime) { this.checkOutTime = checkOutTime; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}