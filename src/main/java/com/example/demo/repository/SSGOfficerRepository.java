package com.example.demo.repository;

import com.example.demo.model.SSGOfficer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SSGOfficerRepository extends JpaRepository<SSGOfficer, Long> {
    SSGOfficer findByEmail(String email);
}
