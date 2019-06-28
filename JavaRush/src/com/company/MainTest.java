package com.company;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
class MainTest {
    @Test
    void convertCelsiusToFahrenheitEquality() {
        assertEquals(105.8, Main.convertCelsiusToFahrenheit(41));
    }

    @Test
    void sumDigitsInNumberOneDigit() {
        assertEquals(3, Main.sumDigitsInNumber(3));
    }

    @Test
    void sumDigitsInNumberTwoDigits() {
        assertEquals(5, Main.sumDigitsInNumber(32));
    }

    @Test
    void sumDigitsInNumberThreeDigits() {
        assertEquals(15, Main.sumDigitsInNumber(546));
    }
}