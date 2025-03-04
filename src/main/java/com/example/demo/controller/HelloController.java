package com.example.demo.controller;  // <-- SIGURADUHING SAKTO ANG PACKAGE

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")  // <-- Base path para sa tanan endpoints diri
public class HelloController {

    @GetMapping("/hello")  // <-- Ang endpoint nga mo-respond sa '/api/hello'
    public String sayHello() {
        return "Hello, Spring Boot!My Name is Lady Zoy Borja \n" +
                "I'm 19 years old \n" +
                "I'm from Oroquieta City,Misamis Occidental\n" +
                "You can call me zoy ";
    }
}
