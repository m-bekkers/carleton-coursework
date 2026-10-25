import java.util.Random;

/**
 * This class implements a special room type named TransporterRoom, which
 * once entered, warps the player to a random room if the player exits.
 *
 * @author Matthé Bekkers
 * @version 1.15
 */
public class TransporterRoom extends Room{

    /**
     * Random object
     */
    private Random rand = new Random();

    /**
     * Creates a TransporterRoom with the hardcoded description
     */
    public TransporterRoom(){
        super("a Transporter Room");
    }
    /**
     * Returns a random room, independent of the direction parameter.
     *
     * @param direction The exit's direction. Ignored.
     * @return A randomly selected room.
     */
    public Room getExit(String direction) {
        return findRandomRoom();
    }

    /**
     * Gets a room at random from the ArrayList of rooms.
     *
     * @return a randomly selected room
     */
    private Room findRandomRoom() {
        int length = rooms.size();
        int randomRoom = rand.nextInt(length);
        System.out.println(randomRoom);
        return rooms.get(randomRoom);
    }
}
