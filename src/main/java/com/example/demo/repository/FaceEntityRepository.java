package com.example.demo.repository;

import com.example.demo.model.FaceEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FaceEntityRepository extends JpaRepository<FaceEntity, Long> {
}
