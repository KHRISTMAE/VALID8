package com.example.demo.service;

import com.example.demo.model.SSGOfficer;
import com.example.demo.repository.SSGOfficerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class SSGOfficerService {

    @Autowired
    private SSGOfficerRepository officerRepository;

    public SSGOfficer createOfficer(String name, String position, String email, String password) {
        SSGOfficer officer = new SSGOfficer();
        officer.setName(name);
        officer.setPosition(position);
        officer.setEmail(email);
        officer.setPassword(password); // Pwede nimo i-encrypt dinhi kung gusto
        return officerRepository.save(officer);
    }
}