package com.example.demo.controller;

import com.example.demo.model.UserTable;
import com.example.demo.repository.UserTableRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/admin")
public class AdminController {
    private final UserTableRepository userRepository;

    public AdminController(UserTableRepository userRepository) {
        this.userRepository = userRepository;
    }

    // GET all users
    @GetMapping("/users")
    public ResponseEntity<List<UserTable>> getAllUsers() {
        return ResponseEntity.ok(userRepository.findAll());
    }

    // CREATE a new user
    @PostMapping("/users")
    public ResponseEntity<UserTable> createUser(@RequestBody UserTable user) {
        UserTable newUser = userRepository.save(user);
        return ResponseEntity.ok(newUser);
    }

    // UPDATE an existing user
    @PutMapping("/users/{id}")
    public ResponseEntity<UserTable> updateUser(@PathVariable Long id, @RequestBody UserTable updatedUser) {
        return userRepository.findById(id)
                .map(user -> {
                    user.setUsername(updatedUser.getUsername());
                    user.setPassword(updatedUser.getPassword()); // Encrypt ito sa actual na setup
                    user.setRole(updatedUser.getRole());
                    userRepository.save(user);
                    return ResponseEntity.ok(user);
                })
                .orElse(ResponseEntity.notFound().build());
    }

    // DELETE a user
    @DeleteMapping("/users/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        if (userRepository.existsById(id)) {
            userRepository.deleteById(id);
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}

