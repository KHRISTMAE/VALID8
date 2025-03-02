package com.example.demo.model;

import jakarta.persistence.*;
import com.fasterxml.jackson.annotation.JsonIgnore;
import java.util.List;

@Entity
@Table(name = "student")
public class Student {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long studentID;

    @Column(nullable = false)
    private String studentName;

    @Column(unique = true, nullable = false)
    private String email;

    private String password;

    @ManyToOne
    @JoinColumn(name = "programID", nullable = false) // Added Foreign Key for Program
    private Program program;

    @Column(nullable = false)
    private int yearLevel; // Added yearLevel

    @ManyToOne
    @JoinColumn(name = "userID", nullable = false) // Added Foreign Key for UserTable
    private UserTable user;

    @Lob // Large Object for storing images
    @Column(columnDefinition = "LONGBLOB") // Store image as binary data
    private byte[] photo; // Added Photo for Face Recognition

    @OneToMany(mappedBy = "student", fetch = FetchType.LAZY, cascade = CascadeType.ALL)
    @JsonIgnore // Prevent circular reference issue in JSON response
    private List<Attendance> attendances;

    // Getters and Setters
    public Long getStudentID() { return studentID; }
    public void setStudentID(Long studentID) { this.studentID = studentID; }

    public String getStudentName() { return studentName; }
    public void setStudentName(String studentName) { this.studentName = studentName; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }

    public Program getProgram() { return program; } // Getter for Program
    public void setProgram(Program program) { this.program = program; } // Setter for Program

    public int getYearLevel() { return yearLevel; } // Getter for Year Level
    public void setYearLevel(int yearLevel) { this.yearLevel = yearLevel; } // Setter for Year Level

    public UserTable getUser() { return user; } // Getter for User
    public void setUser(UserTable user) { this.user = user; } // Setter for User

    public byte[] getPhoto() { return photo; } // Getter for Photo
    public void setPhoto(byte[] photo) { this.photo = photo; } // Setter for Photo

    public List<Attendance> getAttendances() { return attendances; }
    public void setAttendances(List<Attendance> attendances) { this.attendances = attendances; }
}
