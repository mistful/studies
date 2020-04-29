public class FibList {
    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(getNthFibonacciNumber(n));
    }

    static long getNthFibonacciNumber(int n) {
        if (n <= 1) {
            return n;
        }

        long[] list = new long[n + 1];
        list[0] = 0;
        list[1] = 1;

        for (int i = 2; i < n + 1; i++) {
            list[i] = list[i - 1] + list[i - 2];
        }

        return list[n];
    }
}
