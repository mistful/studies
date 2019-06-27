package com.company;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
class MainTest {
    @Test
    void convertCelsiusToFahrenheitEquality() {
        assertEquals(105.8, Main.convertCelsiusToFahrenheit(41));
    }
}