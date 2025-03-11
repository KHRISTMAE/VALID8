package com.example.demo.controller;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import com.example.demo.model.LoginRequest;

@CrossOrigin(origins = "http://localhost:5178") // Allow CORS for frontend
@RestController
@RequestMapping("/api/auth")
public class AuthController {

    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestBody LoginRequest request) {
        System.out.println("Received Email: " + request.getEmail());
        System.out.println("Received Password: " + request.getPassword());

        String validEmail = "user@example.com";
        String validPassword = "password123";

        if (validEmail.equals(request.getEmail()) && validPassword.equals(request.getPassword())) {
            return ResponseEntity.ok("Login Successful!");
        } else {
            return ResponseEntity.status(401).body("Invalid email or password");
        }
    }

}
