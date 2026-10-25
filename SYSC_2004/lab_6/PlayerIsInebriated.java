import java.util.Random;

/**
 * PlayerIsInebriated models a player who has had one too many and is no longer
 * making logical decisions. Whether the player ends a turn is completely random.
 *
 * @author Matthé Bekkers
 * @version 1.0
 */
public class PlayerIsInebriated extends Player{

    /**
     * Constructor for objects of class PlayerIsInebriated.
     *
     * @param dice The dice used by all players.
     * @param name The name of the player.
     */
    public PlayerIsInebriated(Dice dice, String name) {
        super(dice, name);
    }

    /**
     * The decision on whether to roll or not.
     *
     * @return Whether to roll or not.
     */
    protected boolean stopRolling() {
        Random rand = new Random();
        int decide = rand.nextInt(2);
        return decide != 0 && numRolls > 1;
    }
}
