import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class FibListTest {

//    @Test
//    void getZeroFibonacciNumber() {
//        assertEquals(0L, FibList.getNthFibonacciNumber(0));
//    }
//
//    @Test
//    void getFirstFibonacciNumber() {
//        assertEquals(1L, FibList.getNthFibonacciNumber(1));
//    }
//
//    @Test
//    void getSecondFibonacciNumber() {
//        assertEquals(1L, FibList.getNthFibonacciNumber(2));
//    }
//
//    @Test
//    void getThirdFibonacciNumber() {
//        assertEquals(2L, FibList.getNthFibonacciNumber(3));
//    }

    @Test
    void getNthFibonacciNumber() {
        assertEquals(6765, FibList.getNthFibonacciNumber(20));
    }
}