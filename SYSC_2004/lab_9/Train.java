import java.util.ArrayList;

public class Train
{
    /** The cars in this train. */
    private ArrayList<Car> cars;
   
    /** 
     * Constructs an empty train; i.e., one that has no cars.
     */
    public Train()
    {
        cars = new ArrayList<Car>();
    }
   
    /**
     * Adds the specified car to this train.
     *
     * @param car: The car to be added to the train.
     */
    public void addCar(Car car)
    {
        cars.add(car);
    }
    
    /**
     * Returns this trains's list of cars. This method is intended for 
     * testing purposes only, and should not be called by other objects,
     * as it may be removed from the final version of this class.
     * 
     * @return A list of the cars in the train
     */
    public ArrayList<Car> cars()
    {
        return cars;
    }    
      
    /**
     * Attempts to issue a ticket for a business class seat or an
     * economy class seat, as specified by the method's argument.
     * It will attempt to book a seat in the first car of the appropriate
     * type, but if a seat is not available it will attempt to book a seat
     * in the second car of the appropriate type, and so on. 
     * A request to issue a ticket in a business-class car will never result
     * in a seat being reserved in an economy-class car, and vice-versa. 
     * Returns true if successful, false otherwise.
     *
     * @param businessClassSeat: Whether the seat to be booked is business or economy class.
     * @return Whether a seat was successfully booked.
     */
    public boolean issueTicket(boolean businessClassSeat)
    {
        for(Car car : cars) {
            if(businessClassSeat) {
                if(car.isBusinessClass() && car.bookNextSeat()){
                    return true;
                }
            }
            else {
                if(!car.isBusinessClass()) {
                    if(car.bookNextSeat()) {
                        return true;
                    }
                }
            }

        }

        return false;
    }
   
    /**
     * Cancels the ticket for the specified seat in the specified car.
     * Returns true if successful, false otherwise.
     */
    public boolean cancelTicket(int carId, int seatNo)
    {
        for(Car car: cars) {
            if(car.id() == carId) {
                return car.cancelSeat(seatNo);
            }
        }

        return false;
    }
}
