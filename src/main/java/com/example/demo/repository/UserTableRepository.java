package com.example.demo.repository;

import com.example.demo.model.UserTable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserTableRepository extends JpaRepository<UserTable, Long> {
    UserTable findByEmail(String email);
    UserTable findByUsername(String username);
}
