package com.example.demo.all;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

@SpringBootApplication(scanBasePackages = "com.example.demo.config")
@EntityScan(basePackages = "com.example.demo.model;") // Scan sa imong models
@EnableJpaRepositories(basePackages = "com.example.demo.repository") // Scan sa repositories
@ComponentScan(basePackages = "com.example.demo") // Scan tanan beans
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}