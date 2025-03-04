package com.example.demo;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class LoginUITest {

    @Test
    public void testLogin() {
        // Use WebDriverManager to handle ChromeDriver automatically
        WebDriverManager.chromedriver().setup();

        // Launch browser
        WebDriver driver = new ChromeDriver();
        driver.get("http://localhost:8080"); // Change to your actual frontend URL

        // Find elements
        WebElement username = driver.findElement(By.name("username"));
        WebElement password = driver.findElement(By.name("password"));
        WebElement loginButton = driver.findElement(By.id("login-button"));

        // Input test credentials
        username.sendKeys("testuser");
        password.sendKeys("password123");
        loginButton.click();

        // Verify login success
        assertTrue(driver.getCurrentUrl().contains("dashboard"));

        // Close browser
        driver.quit();
    }
}