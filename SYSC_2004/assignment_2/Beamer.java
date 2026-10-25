/**
 * This class models a beamer item, which can be picked up by the player and
 * used to set a restore point by using the charge() method. The player may then
 * at any point use fire() to warp back to the room they called charge() in.
 *
 * @author Matthé Bekkers
 * @version 1.19, Match 14th, 2025
 */
public class Beamer extends Item{

    /**
     * Room which is stored in the Beamer's charge.
     */
    public Room chargedRoom;

    /**
     * Initializes the description and weight fields for the beamer being created.
     *
     * @param description : description of the item.
     * @param weight      : weight of the item in inventory.
     * @param name        : name of the item - in this case beamer.
     */
    public Beamer(String description, double weight, String name) {
        super(description, weight, name);

        chargedRoom = null;
    }

    /**
     * Charges the beamer with the current room the player is in.
     *
     * @param room The room the player is currently in.
     */
    public void charge(Room room) {
        if (isBeamerCharged()) {
            System.out.println("Beamer is already charged");
        }
        else {
            chargedRoom = room;
        }
    }

    /**
     * Fires the beamer and returns the room to be teleported to.
     * Prints an error message if the beamer is empty.
     *
     * @return The room to be teleported to.
     */
    public Room fire() {
        if(isBeamerCharged()) {
            Room destRoom = chargedRoom;
            chargedRoom = null;
            return destRoom;
        }
        System.out.println("No room charged!");
        return null;
    }

    /**
     * Checks whether the beamer currently has a Room charged.
     *
     * @return true if there is a room charged.
     */
    public boolean isBeamerCharged() {
        return chargedRoom != null;
    }
}
