package com.example.demo.service;

import com.example.demo.model.OfficerEvent;
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

    public List<OfficerEvent> getAllOfficerEvents() {
        return officerEventRepository.findAll();
    }

    public Optional<OfficerEvent> getOfficerEventById(OfficerEventKey id) {
        return officerEventRepository.findById(id);
    }

    public OfficerEvent saveOfficerEvent(OfficerEvent officerEvent) {
        return officerEventRepository.save(officerEvent);
    }

    public void deleteOfficerEvent(OfficerEventKey id) {
        officerEventRepository.deleteById(id);
    }
}