/**
 * PlayerRollOnce models a very wimpy and loser player of Chance-It who only ever rolls once
 * because they are scared that they will roll the same as their initial roll.
 *
 * @author Matthé Bekkers
 * @version 1.0
 */
public class PlayerRollOnce extends Player {

    /**
     * Constructor for objects of class PlayerRollOnce.
     *
     * @param dice The pair of dice shared by all players
     * @param name The name of the player rolling.
     */
    public PlayerRollOnce(Dice dice, String name) {
        super(dice, name);
    }

    /**
     * Encapsulates the strategy for this player to determine when to stop rolling this turn.
     *
     * @return When the player decides to end their turn, otherwise false.
     */
    protected boolean stopRolling() {
        return currentRoll > 1;
    }
}
