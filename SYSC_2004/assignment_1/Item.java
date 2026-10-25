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
 * @version January 29th, 2025
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
     * Initializes the description and weight fields for the item being created.
     *
     * @param description: description of the item.
     * @param weight: weight of the item in inventory.
     */
    public Item(String description, double weight) {
        this.description = description;
        this.weight = weight;
    }

    /**
     * Fetches a String representation of the description of an item.
     *
     * @return the String representation of the item.
     */
    public String getDescription() {
        return "Description: " + description + "\nWeight: " + weight;
    }
}
