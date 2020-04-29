import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class GcdTest {

    @Test
    void gcd() {
        assertEquals(61232L, Gcd.gcd(3918848L, 1653264L));
    }
}