package com.example.demo.repository;

import com.example.demo.model.EventOrganizer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EventOrganizerRepository extends JpaRepository<EventOrganizer, Long> {
    EventOrganizer findByOrganizerName(String organizerName); // Find organizer by name
}
