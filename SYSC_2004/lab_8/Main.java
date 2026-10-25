public class Main {
    public static void main(String[] args) {
        RollOverCounter rollOverCounter = new RollOverCounter(1, 5);
        LimitedCounter limitedCounter = new LimitedCounter(1, 5);


        for (int i = 0; i < 5; i++) {
            rollOverCounter.countUp();
            System.out.println(rollOverCounter.count());
        }

        for (int i = 0; i < 5; i++) {
            limitedCounter.countUp();
            System.out.println(limitedCounter.count());
        }

        limitedCounter.countDown();

        System.out.println(limitedCounter.count());

    }
}
