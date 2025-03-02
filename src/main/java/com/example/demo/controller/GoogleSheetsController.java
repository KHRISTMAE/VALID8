package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.example.demo.service.GoogleSheetsService;


@RestController
@RequestMapping("/sheets")
public class GoogleSheetsController {

    private final GoogleSheetsService googleSheetsService;

    public GoogleSheetsController(GoogleSheetsService googleSheetsService) {
        this.googleSheetsService = googleSheetsService;
    }

    @GetMapping("/sync")
    public String syncData() {
        googleSheetsService.syncPostgreSQLToGoogleSheets();
        return "✅ Data Synced Successfully!";
    }
}


