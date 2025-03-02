package com.example.demo.repository;

import com.example.demo.model.Officer_Event;
import com.example.demo.model.OfficerEventKey;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface OfficerEventRepository extends JpaRepository<Officer_Event, OfficerEventKey> {
    // Pwede ka mag-add ug custom queries kung kinahanglan
}