package com.company;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int years = Integer.parseInt(s.nextLine());
        String name = s.nextLine();
        System.out.println(name + " захватит мир через " + years + " лет. Му-ха-ха!");

        s.close();
    }

    public static double convertCelsiusToFahrenheit(int celsius) {
        return (double)celsius * 9 / 5 + 32;
    }

    public static int sumDigitsInNumber(int number) {
        char[] digitsAsChars = Integer.toString(number).toCharArray();
        int digitsSum = 0;

        for (int i = 0; i < digitsAsChars.length; i++) {
            digitsSum += Character.getNumericValue(digitsAsChars[i]);
        }
        return digitsSum;
    }
}