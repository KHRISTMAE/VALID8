package com.example.demo.service;

import com.example.demo.model.Officer_Event;
import com.example.demo.model.OfficerEventKey;
import com.example.demo.repository.OfficerEventRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class OfficerEventService {
    @Autowired
    private OfficerEventRepository officerEventRepository;

    public List<Officer_Event> getAllOfficerEvents() {
        return officerEventRepository.findAll();
    }

    public Optional<Officer_Event> getOfficerEventById(OfficerEventKey id) {
        return officerEventRepository.findById(id);
    }

    public Officer_Event saveOfficerEvent(Officer_Event officerEvent) {
        return officerEventRepository.save(officerEvent);
    }

    public void deleteOfficerEvent(OfficerEventKey id) {
        officerEventRepository.deleteById(id);
    }
}