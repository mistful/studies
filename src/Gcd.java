import java.util.Scanner;

public class Gcd {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long a = scanner.nextLong();
        long b = scanner.nextLong();
        System.out.println(gcd(a, b));
    }

    static long gcd(long a, long b) {
        long remainder = a % b;
        if (remainder == 0L) {
            return b;
        }
        return gcd(b, remainder);
    }
}
