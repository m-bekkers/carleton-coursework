public class Main {
    public static void main(String[] args) {
        Heater heater = new Heater();
        int temperature;
        temperature = heater.temperature();
        System.out.println("Temperature: " + temperature);
        heater.warmer();
        System.out.println("Temperature: " + heater.temperature());
        heater.cooler();
        System.out.println("Temperature: " + heater.temperature());

    }
}
