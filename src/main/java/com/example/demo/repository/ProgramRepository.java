package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.example.demo.model.Program; // Update import to use Program entity

@Repository
public interface ProgramRepository extends JpaRepository<Program, Long> {
    Program findByProgramName(String programName); // Update method to match new entity
}