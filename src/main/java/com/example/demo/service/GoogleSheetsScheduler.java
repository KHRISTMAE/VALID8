package com.example.demo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import javax.sql.DataSource;
import java.sql.Connection;

@Component
public class GoogleSheetsScheduler {

    private final GoogleSheetsService googleSheetsService;
    private final DataSource dataSource;

    @Autowired
    public GoogleSheetsScheduler(GoogleSheetsService googleSheetsService, DataSource dataSource) {
        this.googleSheetsService = googleSheetsService;
        this.dataSource = dataSource;
    }

    @Scheduled(fixedRate = 60000) // Runs every 1 minute
    public void syncData() {
        if (isDatabaseConnected()) {
            System.out.println("🔄 Syncing PostgreSQL to Google Sheets...");
            googleSheetsService.syncPostgreSQLToGoogleSheets();
        } else {
            System.err.println("⚠️ Database connection failed. Skipping sync.");
        }
    }

    private boolean isDatabaseConnected() {
        try (Connection conn = dataSource.getConnection()) {
            return conn != null && !conn.isClosed();
        } catch (Exception e) {
            System.err.println("⚠️ Error checking database connection: " + e.getMessage());
            return false;
        }
    }
}
