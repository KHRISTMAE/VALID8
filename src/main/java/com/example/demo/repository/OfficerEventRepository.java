package com.example.demo.repository;

import com.example.demo.model.OfficerEvent;
import com.example.demo.model.OfficerEventKey;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface OfficerEventRepository extends JpaRepository<OfficerEvent, OfficerEventKey> {
    //
}