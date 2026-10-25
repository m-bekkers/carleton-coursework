/**
 * The test class CounterTest.
 *
 * @author  Matthé Bekkers
 * @version 69.420
 */
public class CounterTest extends junit.framework.TestCase
{
    private Counter c1;
    private Counter c2;
	
    /**
     * Default constructor for test class CounterTest
     */
    public CounterTest()
    {
    }

    /**
     * Sets up the test fixture.
     *
     * Called before every test case method.
     */
    protected void setUp()
    {
        c1 = new RollOverCounter(1, 10);
        c2 = new LimitedCounter(1, 10);
    }

    /**
     * Tears down the test fixture.
     *
     * Called after every test case method.
     */
    protected void tearDown()
    {
    }
    
    /**
     * Tests the original (lab 8) RollOverCounter methods.
     */
    public void testAllRollOverCounterMethods()
    {    
        /* Verify that the counter is in the correct initial state. */
        assertEquals(1, c1.minimumCount());
        assertEquals(10, c1.maximumCount());
        assertEquals(1, c1.count());        
        
        assertTrue(c1.isAtMinimum());
        assertFalse(c1.isAtMaximum());
  
        /* Count 1 -> 2 */
        
        c1.countUp();
        assertEquals(2, c1.count());
        assertFalse(c1.isAtMinimum());
        
        /* Count 3, 4, ...9, 10 */
        for (int i = 1; i < 9; i++) {
            c1.countUp();
        }
        assertTrue(c1.isAtMaximum());
        
        /* Count 10 -> 1 */
        c1.countUp();
        assertEquals(1, c1.count());
        
        /* Verify that reset works. */
        c1.countUp();
        c1.countUp();
        c1.reset();
        assertEquals(1, c1.count());
    }

    /**
     * Tests LimitedCounter's methods
     */
    public void testAllLimitedCounterMethods() {
        /* Verify that the counter is in the correct initial state. */
        assertEquals(1, c2.minimumCount());
        assertEquals(10, c2.maximumCount());
        assertEquals(1, c2.count());

        assertTrue(c2.isAtMinimum());
        assertFalse(c2.isAtMaximum());

        /* Count 1 -> 2 */

        c2.countUp();
        assertEquals(2, c2.count());
        assertFalse(c2.isAtMinimum());

        /* Count 3, 4, ...9, 10 */
        for (int i = 1; i < 9; i++) {
            c2.countUp();
        }
        assertTrue(c2.isAtMaximum());

        /* Count 10 -> 1 */
        c2.countUp();
        assertTrue(c2.count() == 10);

        /* Verify that reset works. */
        c2.countUp();
        c2.countUp();
        c2.reset();
        assertEquals(1, c2.count());
    }

    /**
     * Tests the new methods in RollOverCounter
     */
    public void testNewRollOverCounterMethods() {
        c1.reset();
        assertTrue(c1.isAtMinimum());
        assertFalse(c1.isAtMaximum());

        for (int i = 1; i < 10; i++) {
            c1.countUp();
        }

        assertTrue(c1.isAtMaximum());
        assertFalse(c1.isAtMinimum());
    }

    /**
     * Tests the new methods in LimitedCounter
     */
    public void testNewLimitedCounterMethods() {
        c2.reset();
        assertTrue(c2.isAtMinimum());
        assertFalse(c2.isAtMaximum());

        for (int i = 1; i < 10; i++) {
            c2.countUp();
        }

        assertTrue(c2.isAtMaximum());
        assertFalse(c2.isAtMinimum());
    }
}
