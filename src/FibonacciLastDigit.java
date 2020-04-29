import java.util.*;

public class FibonacciLastDigit {
    static int getFibonacciLastDigit(int n) {
        if (n <= 1)
            return n;

        int[] list = new int[n + 1];
        list[0] = 0;
        list[1] = 1;

        for (int i = 2; i < n + 1; i++) {
            list[i] = (list[i - 1] + list[i - 2]) % 10;
        }

        return list[n];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int c = getFibonacciLastDigit(n);

        System.out.println(c);
    }
}

