public class MaxPairwiseProduct {
    static long getMaxPairwiseProduct(long[] numbers) {
        long max = 0;
        int maxIndex = -1;

        for (int i = 0; i < numbers.length; i++) {
            if (Math.max(numbers[i], max) == numbers[i]) {
                max = numbers[i];
                maxIndex = i;
            }
        }

        max = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (Math.max(numbers[i], max) == numbers[i] && i != maxIndex) {
                max = numbers[i];
            }
        }

        return max * numbers[maxIndex];
    }

    public static void main(String[] args) {
        FastScanner scanner = new FastScanner(System.in);
        int n = scanner.nextInt();
        long[] numbers = new long[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = scanner.nextInt();
        }
        System.out.println(getMaxPairwiseProduct(numbers));
    }



}
