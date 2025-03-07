package com.example.demo.model;

import jakarta.persistence.*;
import com.fasterxml.jackson.annotation.JsonIgnore;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

import java.util.List;

@Entity
@Table(name = "student")
public class Student {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long studentID;

    @Column(nullable = false, length = 100) // ✅ Added length constraint
    private String studentName;

    @Column(unique = true, nullable = false, length = 100) // ✅ Limited email length
    private String email;

    @Column(nullable = false) // ✅ Ensure password is required
    private String password; // ✅ Will store hashed password

    @ManyToOne
    @JoinColumn(name = "programID", nullable = false) // ✅ Foreign Key for Program
    private Program program;

    @Column(nullable = false)
    private int yearLevel; // ✅ Ensure yearLevel is required

    @ManyToOne
    @JoinColumn(name = "userID", nullable = false) // ✅ Foreign Key for UserTable
    private UserTable user;

    @Lob
    @Column(columnDefinition = "BYTEA") // ✅ PostgreSQL format for binary data
    private byte[] photo; // ✅ Store photo for Face Recognition

    @OneToMany(mappedBy = "student", fetch = FetchType.LAZY, cascade = CascadeType.ALL)
    @JsonIgnore // ✅ Prevent circular reference issue
    private List<Attendance> attendances;

    // ✅ Default Constructor (Required for JPA)
    public Student() {}

    // ✅ Correct Parameterized Constructor
    public Student(String studentName, String email, String password, Program program, int yearLevel, UserTable user) {
        this.studentName = studentName;
        this.email = email;
        this.password = hashPassword(password); // ✅ Hash password
        this.program = program;
        this.yearLevel = yearLevel;
        this.user = user;
    }

    // ✅ Hash the password using BCrypt
    private String hashPassword(String password) {
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
        return passwordEncoder.encode(password);
    }

    // ✅ Getters and Setters
    public Long getStudentID() { return studentID; }
    public void setStudentID(Long studentID) { this.studentID = studentID; }

    public String getStudentName() { return studentName; }
    public void setStudentName(String studentName) { this.studentName = studentName; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = hashPassword(password); } // ✅ Always hash password

    public Program getProgram() { return program; }
    public void setProgram(Program program) { this.program = program; }

    public int getYearLevel() { return yearLevel; }
    public void setYearLevel(int yearLevel) { this.yearLevel = yearLevel; }

    public UserTable getUser() { return user; }
    public void setUser(UserTable user) { this.user = user; }

    public byte[] getPhoto() { return photo; }
    public void setPhoto(byte[] photo) { this.photo = photo; }

    public List<Attendance> getAttendances() { return attendances; }
    public void setAttendances(List<Attendance> attendances) { this.attendances = attendances; }
}