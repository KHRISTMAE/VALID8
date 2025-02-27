package com.example.demo.repository;

import com.example.demo.model.Officer_Event;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface OfficerEventRepository extends JpaRepository<Officer_Event, Long> {
    List<Officer_Event> findByOfficerOfficerID(Long officerID);
    List<Officer_Event> findByEventEventID(Long eventID);
}
