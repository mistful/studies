package com.company;

public class Main {
    public static void main(String[] args) {
        System.out.println(convertCelsiusToFahrenheit(41));
    }

    public static double convertCelsiusToFahrenheit(int celsius) {
        return (double)celsius * 9 / 5 + 32;
    }
}