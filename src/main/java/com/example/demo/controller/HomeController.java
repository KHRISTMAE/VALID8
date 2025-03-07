package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/")
public class HomeController {

    @GetMapping
    public String home() {
        return "Hello, Spring Boot!";
    }

    @GetMapping("/login")
    public String login() {
        return "Login Page"; // You can return a proper login HTML page later
    }
}
