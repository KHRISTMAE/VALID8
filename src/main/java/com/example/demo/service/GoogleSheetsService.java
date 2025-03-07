package com.example.demo.service;

import com.google.api.client.auth.oauth2.Credential;
import com.google.api.client.googleapis.auth.oauth2.GoogleCredential;
import com.google.api.client.http.HttpTransport;
import com.google.api.client.http.javanet.NetHttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.client.json.jackson2.JacksonFactory;
import com.google.api.services.sheets.v4.Sheets;
import com.google.api.services.sheets.v4.model.ValueRange;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.io.InputStream;
import java.sql.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Service
public class GoogleSheetsService {

    @Value("${google.sheets.credentials.path}")
    private String credentialsPath;

    @Value("${google.sheets.spreadsheet.id}")
    private String spreadsheetId;

    private static final String RANGE = "AttendanceData!A2:G";
    private final ResourceLoader resourceLoader;

    public GoogleSheetsService(ResourceLoader resourceLoader) {
        this.resourceLoader = resourceLoader;
    }

    private Sheets getSheetsService() throws IOException {
        HttpTransport httpTransport = new NetHttpTransport();
        JsonFactory jsonFactory = JacksonFactory.getDefaultInstance();

        Resource resource = resourceLoader.getResource(credentialsPath);
        InputStream credentialsStream = resource.getInputStream();

        Credential credential = GoogleCredential.fromStream(credentialsStream)
                .createScoped(Arrays.asList("https://www.googleapis.com/auth/spreadsheets"));

        return new Sheets.Builder(httpTransport, jsonFactory, credential)
                .setApplicationName("AttendanceSync")
                .build();
    }

    public void syncPostgreSQLToGoogleSheets() {
        String dbUrl = "jdbc:postgresql://localhost:5432/Valid8";
        String dbUser = "postgres";
        String dbPassword = "Anthony2001";

        try (Connection conn = DriverManager.getConnection(dbUrl, dbUser, dbPassword)) {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT studentID, studentName, programName, timeIn, timeOut, photoURL, status FROM Attendance");

            List<List<Object>> data = new ArrayList<>();
            while (rs.next()) {
                data.add(Arrays.asList(
                        rs.getString("studentID"),
                        rs.getString("studentName"),
                        rs.getString("programName"), // Updated from Course to programName
                        rs.getString("timeIn"),
                        rs.getString("timeOut"),
                        rs.getString("photoURL"),
                        rs.getString("status")
                ));
            }

            Sheets sheetsService = getSheetsService();
            ValueRange body = new ValueRange().setValues(data);
            sheetsService.spreadsheets().values().update(spreadsheetId, RANGE, body)
                    .setValueInputOption("RAW").execute();

            System.out.println("✅ Attendance Data Updated Successfully!");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}