public class main {
    public static void main(String[] args) {
        Seat mySeat = new Seat(5, 25.00);
        System.out.println(mySeat.number());
        System.out.println(mySeat.price());
        System.out.println(mySeat.isBooked());
        mySeat.book();
        System.out.println(mySeat.isBooked());
        mySeat.cancelBooking();
        System.out.println(mySeat.isBooked());
        Car myCar = new Car(123, true);
        boolean booked = myCar.bookNextSeat();

        Car aCar = new Car(1385, true);
        Seat[] seats = aCar.seats();
        for(int i=0; i<seats.length; i++) {

        }
    }
}
