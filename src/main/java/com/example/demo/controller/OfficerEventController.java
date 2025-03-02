package com.example.demo.controller;

import com.example.demo.model.Officer_Event;
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
    public List<Officer_Event> getAllOfficerEvents() {
        return officerEventService.getAllOfficerEvents();
    }

    @GetMapping("/{officerId}/{eventId}")
    public Optional<Officer_Event> getOfficerEventById(@PathVariable Long officerId, @PathVariable Long eventId) {
        OfficerEventKey id = new OfficerEventKey(officerId, eventId);
        return officerEventService.getOfficerEventById(id);
    }

    @PostMapping
    public Officer_Event createOfficerEvent(@RequestBody Officer_Event officerEvent) {
        return officerEventService.saveOfficerEvent(officerEvent);
    }

    @DeleteMapping("/{officerId}/{eventId}")
    public void deleteOfficerEvent(@PathVariable Long officerId, @PathVariable Long eventId) {
        OfficerEventKey id = new OfficerEventKey(officerId, eventId);
        officerEventService.deleteOfficerEvent(id);
    }
}