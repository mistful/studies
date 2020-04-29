import org.junit.jupiter.api.BeforeAll;

import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

class MaxPairwiseProductTest {
    static long[] numbers;

    @BeforeAll
    static void beforeAll() {
        numbers = new long[100000];
        Random random = new Random();
        for (int i = 0; i < 100000; i++) {
            if (i == 10) {
                numbers[i] = 100000;
            } else if (i == 756) {
                numbers[i] = 90000;
            } else {
                numbers[i] = random.nextInt(10);
            }
        }
    }

    @org.junit.jupiter.api.Test
    void getMaxPairwiseProduct() {
        //numbers = new long[]{7, 5, 14, 2, 8, 8, 10, 1, 2, 3};
        assertEquals(9000000000L, MaxPairwiseProduct.getMaxPairwiseProduct(numbers));
    }
}