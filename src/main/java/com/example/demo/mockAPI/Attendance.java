package com.example.demo.mockAPI;

import com.example.demo.model.Event;
import com.example.demo.model.Student;
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
    private Student studentID;

    private Event eventID;

    private LocalDateTime checkInTime;
    private LocalDateTime midEventCheckpoint;
    private LocalDateTime checkOutTime;

    @Column(nullable = false)
    private String status;

    public Attendance(Long attendanceID, Long eventID, Long studentID ,String dateTime, String status) {
        this.attendanceID = attendanceID;
        this.status = status;

    }

    // Getters and Setters
    public Long getAttendanceID() { return attendanceID; }
    public void setAttendanceID(Long attendanceID) { this.attendanceID = attendanceID; }

    public Event getEventID(){return eventID;}
    public void setEventID(Event eventID) {this.eventID = eventID;}

    public Student getStudent() { return studentID; }
    public void setStudent(Student studentID) { this.studentID = studentID; }

    public LocalDateTime getCheckInTime() { return checkInTime; }
    public void setCheckInTime(LocalDateTime checkInTime) { this.checkInTime = checkInTime; }

    public LocalDateTime getMidEventCheckpoint() { return midEventCheckpoint; }
    public void setMidEventCheckpoint(LocalDateTime midEventCheckpoint) { this.midEventCheckpoint = midEventCheckpoint; }

    public LocalDateTime getCheckOutTime() { return checkOutTime; }
    public void setCheckOutTime(LocalDateTime checkOutTime) { this.checkOutTime = checkOutTime; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}
