# VALID8

## Table of Contents
- [1. Project Overview](#1-project-overview)
- [2. Functional Requirements](#2-functional-requirements)
- [3. Non-Functional Requirements](#3-non-functional-requirements)
- [4. Stakeholders](#stakeholders)
- [5. Signature and Approval](#signature-and-approval)

## 1. Project Overview

### Project Description:
- A high-end attendance checker that will automatically displays students who attended the events in JRMSU College of Engineering.

### Target Audience:
- Students

### Project Objectives
- Design an intuitive user interface that allows students to easily access their attendance records, receive real-time notifications, and view upcoming events, ensuring a seamless experience.

## 2. Functional Requirements

### Core Features
- Sends instant notifications to students confirming their attendance status, along with reminders for upcoming events.
- Allows students to view their attendance history, including past events attended, dates, and statuses (e.g., present, absent).
- Features an intuitive and responsive user interface for students, SSG officer, event organizer,  and administrators, making it easy to navigate and access attendance information.

### User Stories/ Use Cases
 **As a Student:**
- I want to log in to the app using my student credentials so that I can accurately track my attendance and view the events I have participated in.
- I want to have an email notificcation reminding for an upcoming event.
- I would like to receive an email confirmation after checking in to ensure that my attendance is valid.
- I want to be able to view my past attendance records for events, allowing me to track my participation over time.

**As an SSG Officer:**
- I want to verify student check-ins to ensure that only valid attendees are recorded.
- Additionally, I want to flag any incorrect check-ins so that event organizers or administrators can review them.

**As an Event Organizer:**
- I want to create a new event by entering essential details such as the event name, date, time, location, and description.
- I want to easily edit or update event details whenever necessary.
- I want to define registration limits and deadlines for my events.
- I want to send email notifications or reminders to registered students about the event.

**As an Administrator:**
- I want to manage user accounts for students, SSG officer, and event organizers.
- I want to oversee all events created within the system and review flagged attendance issues so that attendance accuracy is maintained.
- I want to set permissions and access levels for different users.
- I want to generate comprehensive reports on attendance data across all events. 

### Integration Requirements
- The system should integrate with an email service provider to facilitate automated email notifications for event reminders, confirmations, and updates.
- The system should allow integration with calendar applications.
- It should integrate with the Valid8 system to allow students to check in and view their attendance records on their smartphones.

### Data Requirements 
### 1. User Data:
### Student Information:
- Student ID, name, email address, contact number, enrollment status, and program/major.
### Event Organizer Information:
- Organizer ID, name, email address, contact number.

### 2. Event Data:
### Event Details:
- Event ID, name, date, time, location, description, registration deadline, and maximum capacity.
### Event Status:
- Status (upcoming, ongoing, completed, canceled).

### 3. Attendance Data:
### Check-In Records:
- Check-in ID, event ID, student ID, check-in time, and check-out time (if applicable).
### Attendance Status:
- Status (present, absent, late).

### 4. Notification Data:
### Email Notifications:
- Notification ID, recipient email, subject, message content, and timestamp.

### 5. Feedback Data:
### Survey Responses:
- Feedback ID, event ID, student ID, rating (e.g., 1-5 stars), comments, and submission timestamp.

### 6. System Logs:
### User Activity Logs:
- Log ID, user ID, user role (e.g., student, admin, SSG officer, event organizer), action performed (e.g., login, check-in, event creation)

## 3. Non-Functional Requirements: 
 ### Performance: 
 - The system should respond quickly to user actions, with minimal latency during event creation, registration, and check-in processes.
 - It should be able to handle thousands of students concurrently without degradation in performance, ensuring a smooth user experience even during peak usage times.

### Security: 
- The system must implement robust security measures to protect user data and prevent unauthorized access. This includes data encryption, secure authentication methods, and regular security audits.

### Usability: 
- The user interface should be intuitive and user-friendly, allowing users of varying technical expertise to navigate the system easily. 

### Compliance & Standards:
- The system must comply with relevant data protection regulations (e.g., GDPR, FERPA) and industry standards to ensure the privacy and security of user information.

### Reliability: 
- The system should be reliable, with minimal downtime. It should include backup and recovery mechanisms to ensure data integrity and availability in case of failures.

### Deployment and Maintenance: 
- The system should be easy to deploy and maintain, with clear procedures for updates, bug fixes, and user support. Regular maintenance schedules should be established to ensure optimal performance and security.

## Stakeholders
### Project Sponsor
- Engr Richie Lacaya
- Eng. Troy Lasco

### Primary Point of Contact
- Valid8 group

## Signature and Approval
#### By signing below, the sponsor confirms that all information provided is accurate and complete, and authorizes the development team to proceed with the requirements based on this document.

#### Sponsor Name: 
 - Engr Richie Lacaya

###    

#### Signature:

#### Date: 
  
  
