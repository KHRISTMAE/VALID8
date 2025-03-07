package com.example.demo.controller;

import com.example.demo.model.OfficerEvent;
import com.example.demo.model.OfficerEventKey;
import com.example.demo.service.OfficerEventService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/officer-events")
public class OfficerEventController {
    @Autowired
    private OfficerEventService officerEventService;

    @GetMapping
    public List<OfficerEvent> getAllOfficerEvents() {
        return officerEventService.getAllOfficerEvents();
    }

    @GetMapping("/{officerId}/{eventId}")
    public Optional<OfficerEvent> getOfficerEventById(@PathVariable Long officerId, @PathVariable Long eventId) {
        OfficerEventKey id = new OfficerEventKey(officerId, eventId);
        return officerEventService.getOfficerEventById(id);
    }

    @PostMapping
    public OfficerEvent createOfficerEvent(@RequestBody OfficerEvent officerEvent) {
        return officerEventService.saveOfficerEvent(officerEvent);
    }

    @DeleteMapping("/{officerId}/{eventId}")
    public void deleteOfficerEvent(@PathVariable Long officerId, @PathVariable Long eventId) {
        OfficerEventKey id = new OfficerEventKey(officerId, eventId);
        officerEventService.deleteOfficerEvent(id);
    }
}