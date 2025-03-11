package com.example.demo.repository;

import com.example.demo.model.UserTable;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface UserTableRepository extends JpaRepository<UserTable, Long> {
    Optional<UserTable> findByUsername(String username);
}
