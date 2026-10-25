/**
 * A Heater models a simple space-heater. The operations provided by a Heater
 * object are:
 * 1. Increase and decrease the temperature setting by a set amount.
 * 2. Return the current temperature setting.
 * 3. Change the set amount by which the temperature is increased and lowered.
 * 
 * @author L.S. Marshall, SCE, Carleton University
 * (incomplete implementation for SYSC 2004 Lab 2)
 * @author Matthé Bekkers
 * @version 1.03 January 14th, 2025
 */
public class Heater
{
    /** The temperature setting that the heater should maintain. */
    private int temperature;
    
    /** The temperature setting for a newly created heater. */
    private static final int INITIAL_TEMPERATURE = 15;
    
    /** 
     * The amount by which the temperature setting is raised/lowered when
     * warmer() and cooler() are invoked.
     */
     private int increment;
    
    /** 
     * The default amount by which the temperature setting is 
     * increased when warmer() is invoked and decreased when cooler()
     * is invoked.
     */
    private static final int DEFAULT_INCREMENT = 5;

    /** The highest setting the temperature of the heater may be set to. */
    private int max = 100;

    /** The lowest setting the temperature of the heater may be set to */
    private int min = 0;
    
    /**
     * Constructs a new Heater with an initial temperature setting of 15
     * degrees, and which increments and decrements the temperature
     * setting in increments of 5 degrees.
     */
    public Heater()
    {
        this.temperature = INITIAL_TEMPERATURE;
        this.increment = DEFAULT_INCREMENT;
    }
 
    /**
     * Write an appropriate comment here.
     */    
    public Heater(int minTemp, int maxTemp)
    {
        this.max = maxTemp;
        this.min = minTemp;
        this.temperature = INITIAL_TEMPERATURE;
        this.increment = DEFAULT_INCREMENT;
    }

    /**
     * Returns the current temperature of the heater.
     */    
    public int temperature()
    {
        return temperature;
    }
    
    /**
     * Increases the heater's temperature by the amount stored in increment.
     * If raising the temperature would yield a temperature greater than the
     * max temperature, nothing happens.
     */
    public void warmer()
    {
        if(temperature + increment <= max) {
            temperature += increment;
        }
    }

    /**
     * Decreases the heater's temperature by the amount stored in increment.
     */    
    public void cooler()
    {
        if (temperature - increment >= min) {
            temperature -= increment;
        }
    }
    
    
    /**
     * Write an appropriate comment here.
     */    
    public void setIncrement(int newIncrement)
    {
        if(newIncrement > 0) {
            increment = newIncrement;
        }
    }


}
