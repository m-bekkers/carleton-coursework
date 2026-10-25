import java.util.ArrayList;

/**
 * The test class TrainTest.
 *
 * @author  Lynn Marshall
 * @version May 2015
 */
public class TrainTest extends junit.framework.TestCase
{
    Train aTrain = new Train();
    Car car1;
    Car car2;
    Car car3;
    Car car4;
    /**
     * Default constructor for test class TrainTest
     */
    public TrainTest()
    {
        Car car1 = new Car(1250, true);
        aTrain.addCar(car1);
        Car car2 = new Car(1300, false);
        aTrain.addCar(car2);
        Car car3 = new Car(1740, false);
        aTrain.addCar(car3);
        Car car4 = new Car(1800, true);
        aTrain.addCar(car4);

        /* Book 1 1/2 of available business seats */
        for (int i = 0; i < Car.BUSINESS_SEATS * 1.5; i++) assertTrue(aTrain.issueTicket(true));

        /* Book 1/2 of available economy seats */
        for (int i = 0; i <Car.ECONOMY_SEATS; i++) assertTrue(aTrain.issueTicket(false));
    }

    /**
     * Sets up the test fixture.
     *
     * Called before every test case method.
     */
    protected void setUp()
    {
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
     * Checks that a new train has no pre=existing cars
     */
    public void testCreateEmptyTrain()
    {
        Train aTrain = new Train();
        
        /* Verify that a new train has no cars. */
        assertEquals(0, aTrain.cars().size());
    }

    /**
     * Tests adding a car to a train
     */
    public void testAddCar()
    {
        Train aTrain = new Train();
        
        Car car1 = new Car(1250, true);
        aTrain.addCar(car1);
        
        Car car2 = new Car(1300, false);
        aTrain.addCar(car2);
        
        Car car3 = new Car(1740, false);
        aTrain.addCar(car3);

        Car car4 = new Car(1800, true);
        aTrain.addCar(car4);
        
        ArrayList<Car> cars = aTrain.cars();
        assertEquals(4, cars.size());
    }

    /**
     * Tests issuing tickets to business and economy.
     */
    public void testIssueTicket()
    {
        Train aTrain = new Train();

        Car car1 = new Car(1250, true);
        aTrain.addCar(car1);

        Car car2 = new Car(1300, false);
        aTrain.addCar(car2);

        Car car3 = new Car(1740, false);
        aTrain.addCar(car3);

        Car car4 = new Car(1800, true);
        aTrain.addCar(car4);

        /* Book all the seats in the business-class cars. */
        for (int i = 0; i <Car.BUSINESS_SEATS * 2; i++) {
            assertTrue(aTrain.issueTicket(true));
        }
        
        /* Attempt to book one more business-class seat, even
         * though they are all booked.
         */
        assertFalse(aTrain.issueTicket(true));
 
        ArrayList<Car> cars = aTrain.cars();
        
        for (int i = 0; i < Car.BUSINESS_SEATS; i++) {
            assertTrue(cars.get(0).seats()[i].isBooked());
        }
        
        for (int i = 0; i < Car.ECONOMY_SEATS; i++) {
            assertFalse(cars.get(1).seats()[i].isBooked());
        }
        
        for (int i = 0; i < Car.ECONOMY_SEATS; i++) {
            assertFalse(cars.get(2).seats()[i].isBooked());
        }
        
        /* Book all the seats in the first economy-class car. */
        for (int i = 0; i <Car.ECONOMY_SEATS; i++) {
           assertTrue(aTrain.issueTicket(false));
        }
        
        cars = aTrain.cars();
        
        for (int i = 0; i < Car.BUSINESS_SEATS; i++) {
            assertTrue(cars.get(0).seats()[i].isBooked());
        }
        
        for (int i = 0; i < Car.ECONOMY_SEATS; i++) {
            assertTrue(cars.get(1).seats()[i].isBooked());
        }
        
        for (int i = 0; i < Car.ECONOMY_SEATS; i++) {
            assertFalse(cars.get(2).seats()[i].isBooked());
        }  
        
        /* Book all the seats in the second economy-class car. */
        for (int i = 0; i <Car.ECONOMY_SEATS; i++) {
            assertTrue(aTrain.issueTicket(false));
        }
        
        /* check that all seats are now booked */
        for (int i = 0; i < Car.BUSINESS_SEATS; i++) {
            assertTrue(cars.get(0).seats()[i].isBooked());
        }
        
        for (int i = 0; i < Car.ECONOMY_SEATS; i++) {
            assertTrue(cars.get(1).seats()[i].isBooked());
        }
        
        for (int i = 0; i < Car.ECONOMY_SEATS; i++) {
            assertTrue(cars.get(2).seats()[i].isBooked());
        }  
        
        /* Try to book another business class seat (fails)*/
        assertFalse(aTrain.issueTicket(true));
        /* Try to book another economy class seat (fails)*/
        assertFalse(aTrain.issueTicket(false));
    }

    /**
     * Tests to see if cancelling a ticket works properly
     */
    public void testCancelTicket()
    {
        
        ArrayList<Car> cars = aTrain.cars();

        assertTrue(aTrain.cancelTicket(1300, 4));
        assertFalse(cars.get(1).seats()[3].isBooked());        
        
        /* Cancel ticket in a non-existent car. */
        assertFalse(aTrain.cancelTicket(1500, 7));
        
        /* Cancel ticket in a non-existent seat. */
        assertFalse(aTrain.cancelTicket(1300, 54));
        
        /* Cancel ticket for a seat that hasn't been booked. */
        assertFalse(aTrain.cancelTicket(1740, 21));
        assertFalse(cars.get(2).seats()[20].isBooked());        
        
        /* Attempt to cancel the same ticket twice. */
        assertTrue(aTrain.cancelTicket(1250, 11));
        assertFalse(cars.get(0).seats()[10].isBooked());

        assertFalse(aTrain.cancelTicket(1250, 11));
        assertFalse(cars.get(0).seats()[10].isBooked());

        /* Try to cancel a booked ticked in the front half of the second business class car*/
        assertTrue(aTrain.cancelTicket(1800, 12));

        /* Try to cancel a booked ticked in the unbooked half of the second business class car */
        assertFalse(aTrain.cancelTicket(1800, 28));
    }

    /**
     * Tests to see if cancelling a ticket makes it elligible to be booked again.
     */
    public void testBookCancelTicket() {

        /* Create a new train with 2 business class cars and 2 economy class cars */

        /* Cancel the first 3 tix in the economy car */
        assertTrue(aTrain.cancelTicket(1250, 1));
        assertTrue(aTrain.cancelTicket(1250, 2));
        assertTrue(aTrain.cancelTicket(1250, 3));

        /* Book the first 4 available seats in economy. Make sure the previously cancelled seats are re-booked. */
        for (int i = 0; i < 4; i++) assertTrue(aTrain.issueTicket(false));
        for (int i = 0; i < 3; i++) {
            ArrayList<Car> cars = aTrain.cars();
            assertTrue(cars.getLast().seats()[i].isBooked());
        }
        assertTrue(aTrain.cancelTicket(1250, 16));

        /* Cancel 3 business class tickets */
        assertTrue(aTrain.cancelTicket(1740, 1));
        assertTrue(aTrain.cancelTicket(1800, 2));
        assertTrue(aTrain.cancelTicket(1800, 3));

        /* Try to re-book the cancelled tickets and one extra */
        for (int i = 0; i < 4; i++) assertTrue(aTrain.issueTicket(true));
        ArrayList<Car> cars = aTrain.cars();
        assertTrue(cars.get(1).seats()[1].isBooked());
        assertTrue(cars.get(0).seats()[2].isBooked());
        assertTrue(cars.get(0).seats()[3].isBooked());
        assertTrue(cars.get(1).seats()[16].isBooked());
    }
}
