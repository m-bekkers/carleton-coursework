/**
 * Class Item - an item in an adventure game.
 *
 * This class is part of the "World of Zuul" application.
 * "World of Zuul" is a very simple, text based adventure game.
 *
 * An "Item" represents an item present in a particular room in the game.
 *
 * @author  Michael Kolling and David J. Barnes
 * @version 2006.03.30
 *
 * @author Matthé Bekkers
 * @version 1.41, January 29th, 2025
 *
 * @author Matthé Bekkers
 * @version 2.69, March 14th, 2025
 */
public class Item {

    /**
     * Description of the item at hand.
     */
    private String description;

    /**
     * Weight of the item at hand.
     */
    private double weight;

    /**
     * Name of the item at hand.
     */
    public String name;

    /**
     * Initializes the description and weight fields for the item being created.
     *
     * @param description: description of the item.
     * @param weight: weight of the item in inventory.
     */
    public Item(String description, double weight, String name) {
        this.description = description;
        this.weight = weight;
        this.name = name;
    }

    /**
     * Fetches a String representation of the description of an item.
     *
     * @return the String representation of the item, including the description, the weight, and the name.
     */
    public String getDescription() {
        return "Description: " + description + "\nWeight: " + weight + "\nName: " + name;
    }

    /**
     * Fetches a String representation of the name of the item.
     *
     * @return the name of the item as a String.
     */
    public String getName() { return name; }
}
