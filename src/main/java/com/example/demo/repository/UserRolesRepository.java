package com.example.demo.repository;

import com.example.demo.model.UserRoles;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface UserRolesRepository extends JpaRepository<UserRoles, Long> {
    List<UserRoles> findByUserUserID(Long userID);
    List<UserRoles> findByRoleRoleID(Long roleID);
}
