import java.util.Stack;
/**
 *  This class is the main class of the "World of Zuul" application. 
 *  "World of Zuul" is a very simple, text based adventure game.  Users 
 *  can walk around some scenery. That's all. It should really be extended 
 *  to make it more interesting!
 * 
 *  To play this game, create an instance of this class and call the "play"
 *  method.
 * 
 *  This main class creates and initialises all the others: it creates all
 *  rooms, creates the parser and starts the game.  It also evaluates and
 *  executes the commands that the parser returns.
 * 
 * @author  Michael Kolling and David J. Barnes
 * @version 2006.03.30
 * 
 * @author Lynn Marshall
 * @version October 21, 2012
 *
 * @author Matthé Bekkers
 * @version 2.15, March 15, 2025
 */

public class Game 
{
    /**
     * A parser object
     */
    private Parser parser;

    /**
     * The room the player is currently in
     */
    public Room currentRoom;

    /**
     * The room just previously visited
     */
    private Room previousRoom;

    /**
     * A stack of rooms previously visited
     */
    private Stack<Room> roomStack;

    /**
     * The item being held by the player
     */
    public Item heldItem;

    /**
     * A counter that tracks the remaining items the player may pick up until they must eat.
     */
    private int hungerBar;
        
    /**
     * Create the game and initialise its internal map.
     */
    public Game() 
    {
        createRooms();
        parser = new Parser();
        previousRoom = null;
        roomStack = new Stack<Room>() {};
        heldItem = null;
        hungerBar = 0;
    }

    /**
     * Create all the rooms and link their exits together.
     */
    private void createRooms()
    {
        Room outside, theatre, pub, lab, office;
        TransporterRoom transporter;
      
        // create the rooms
        outside = new Room("outside the main entrance of the university");
        theatre = new Room("in a lecture theatre");
        pub = new Room("in the campus pub");
        lab = new Room("in a computing lab");
        office = new Room("in the computing admin office");
        transporter = new TransporterRoom();
        
        // initialise room exits
        outside.setExit("east", theatre);
        outside.setExit("south", lab);
        outside.setExit("west", pub);
        outside.setExit("north", transporter);

        theatre.setExit("west", outside);

        pub.setExit("east", outside);

        lab.setExit("north", outside);
        lab.setExit("east", office);

        office.setExit("west", lab);

        // add items to rooms
        Item cookies = new Item("A few cookies. Looks like they're raisin...", 1.0, "cookies");
        Item leaves = new Item("A pile of old leaves. They're too damp to crumple up.", 0.5, "leaves");
        Item costume = new Item("An old costume. There are a few mold holes.", 3, "costume");
        Item makeup = new Item("Stage makeup. Someone has left teeth marks in the blue.", 1, "makeup");
        Item glass = new Item("A drinking glass. There are finger marks on it.", 4, "glass");
        Item pen = new Item("A ball-point pen. Someone has left teeth marks on it.", 1.5, "pen");
        Item beamer1 = new Beamer("A beamer. It can teleport you to rooms.", 1, "beamer");
        Item beamer2 = new Beamer("A beamer. It can teleport you to rooms.", 1, "beamer");

        outside.addItemToRoom(cookies);
        outside.addItemToRoom(leaves);
        outside.addItemToRoom(beamer1);
        theatre.addItemToRoom(costume);
        theatre.addItemToRoom(makeup);
        pub.addItemToRoom(glass);
        pub.addItemToRoom(cookies);
        pub.addItemToRoom(beamer2);
        office.addItemToRoom(pen);

        currentRoom = outside;  // start game outside
    }

    /**
     *  Main play routine.  Loops until end of play.
     */
    public void play() 
    {            
        printWelcome();

        // Enter the main command loop.  Here we repeatedly read commands and
        // execute them until the game is over.
                
        boolean finished = false;
        while (! finished) {
            Command command = parser.getCommand();
            finished = processCommand(command);
        }
        System.out.println("Thank you for playing.  Good bye.");
    }

    /**
     * Print out the opening message for the player.
     */
    private void printWelcome()
    {
        System.out.println();
        System.out.println("Welcome to the World of Zuul!");
        System.out.println("World of Zuul is a new, incredibly boring adventure game.");
        System.out.println("Type 'help' if you need help.");
        System.out.println();
        System.out.println(currentRoom.getLongDescription());
    }

    /**
     * Given a command, process (that is: execute) the command.
     * 
     * @param command The command to be processed
     * @return true If the command ends the game, false otherwise
     */
    private boolean processCommand(Command command) 
    {
        boolean wantToQuit = false;

        if(command.isUnknown()) {
            System.out.println("I don't know what you mean...");
            return false;
        }

        String commandWord = command.getCommandWord();
        if (commandWord.equals("help")) {
            printHelp();
        }
        else if (commandWord.equals("go")) {
            goRoom(command);
        }
        else if (commandWord.equals("quit")) {
            wantToQuit = quit(command);
        }
        else if (commandWord.equals("look")) {
            look(command);
        }
        else if (commandWord.equals("eat")) {
            eat(command);
        }
        else if (commandWord.equals("back")) {
            back(command);
        }
        else if (commandWord.equals("stackBack")) {
            stackBack(command);
        }
        else if (commandWord.equals("take")) {
            take(command);
        }
        else if (commandWord.equals("drop")) {
            drop(command);
        }
        else if (commandWord.equals("charge")) {
            charge(heldItem);
        }
        else if (commandWord.equals("fire")) {
            fire(heldItem);
        }
        // else command not recognised.
        return wantToQuit;
    }

    // implementations of user commands:

    /**
     * Print out some help information.
     * Here we print a cryptic message and a list of the 
     * command words.
     */
    private void printHelp() 
    {
        System.out.println("You are lost. You are alone. You wander");
        System.out.println("around at the university.");
        System.out.println();
        System.out.println("Your command words are:");
        System.out.println(parser.getCommands());
    }

    /** 
     * Try to go to one direction. If there is an exit, enter the new
     * room, otherwise print an error message.
     * 
     * @param command The command to be processed
     */
    private void goRoom(Command command) 
    {
        if(!command.hasSecondWord()) {
            // if there is no second word, we don't know where to go...
            System.out.println("Go where?");
            return;
        }

        String direction = command.getSecondWord();

        // Try to leave current room.
        Room nextRoom = currentRoom.getExit(direction);

        if (nextRoom == null) {
            System.out.println("There is no door!");
        }
        else {
            previousRoom = currentRoom;
            roomStack.push(currentRoom);
            currentRoom = nextRoom;
            System.out.println(currentRoom.getLongDescription());
            if (heldItem != null) {
                System.out.println("You are currently holding: " + heldItem.getName() + ".");
            }
        }
    }

    /** 
     * "Quit" was entered. Check the rest of the command to see
     * whether we really quit the game.
     * 
     * @param command The command to be processed
     * @return true, if this command quits the game, false otherwise
     */
    private boolean quit(Command command) 
    {
        if(command.hasSecondWord()) {
            System.out.println("Quit what?");
            return false;
        }
        else {
            return true;  // signal that we want to quit
        }
    }

    /**
     * "Look" was entered. Display a detailed description of the room
     * the player is in.
     *
     * @param command The command to be processed.
     */
    private void look(Command command) {
        if(command.hasSecondWord()) {
            System.out.println("Look where?");
        }
        else {
            System.out.println(currentRoom.getLongDescription());
            if (heldItem != null) {
                System.out.println("You are currently holding: " + heldItem.getName() + ".");
            }
        }
    }

    /**
     * "Eat" was entered. Display a message informing the player that they have eaten
     * and are no longer full.
     *
     * @param command the command to be processed.
     */
    private void eat(Command command) {
        if(command.hasSecondWord()) {
            System.out.println("Eat what?");
        }
        else {
            if(heldItem == null) {
                System.out.println("You have nothing to eat!");
            }
            else if (heldItem.getName().equals("cookies")) {
                System.out.println("You have eaten the cookies and are no longer hungry. Crumbs litter the floor.");
                heldItem = null;
                hungerBar = 5;
            }
            else {
                System.out.println("You can't eat that!");
            }
        }
    }

    private void back(Command command) {
        if(command.hasSecondWord()) {
            System.out.println("Back what?");
        }
        else {
            if(previousRoom == null) {
                System.out.println("You have not yet been anywhere!");
            }
            else {
                Room nextRoom = previousRoom;
                roomStack.push(currentRoom);
                previousRoom = currentRoom;
                currentRoom = nextRoom;

                System.out.println(currentRoom.getLongDescription());
            }
        }
    }

    /**
     * Fetches the previous room from the roomStack Stack. If there are no
     * previous rooms in the Stack, a message is printed.
     *
     * @param command: the command to be ran.
     */
    private void stackBack(Command command) {
        if(command.hasSecondWord()) {
            System.out.println("stackBack what?");
        }
        else {
            if(roomStack.isEmpty()) {
                System.out.println("You are back at the entrance!");
            }
            else {
                Room nextRoom = roomStack.pop();
                previousRoom = currentRoom;
                currentRoom = nextRoom;
                System.out.println(currentRoom.getLongDescription());
            }
        }

    }

    /**
     * Takes the item in the room specified by command.
     * If the item is not in the room, print an error message.
     *
     * @param command a two-word command containing the word "take" and the name of the item to take.
     */
    private void take(Command command) {
        if(!command.hasSecondWord()) {
            System.out.println("Take what?");
        }
        else if (heldItem != null) {
            System.out.println("You are already holding " + heldItem.name + "!");
        }
        else if (hungerBar <= 0) {
            String itemToTake = command.getSecondWord();
            if (itemToTake.equals("cookies")) {
                for(Item item: currentRoom.items) {
                    if(item.name.equals(itemToTake)) {
                        heldItem = item;
                        System.out.println("You are now holding " + heldItem.name + ".");
                        currentRoom.removeItemFromRoom(heldItem);
                        hungerBar--;
                        return;
                    }
                }
            }
            else {
                System.out.println("You are hungry! Find and eat cookies to carry more items.");
            }

        }
        else {
            String itemToTake = command.getSecondWord();
            for(Item item: currentRoom.items) {
                if(item.name.equals(itemToTake)) {
                    heldItem = item;
                    System.out.println("You are now holding " + heldItem.name + ".");
                    currentRoom.removeItemFromRoom(heldItem);
                    hungerBar--;
                    return;
                }
            }
            System.out.println("There is no " + itemToTake + "!");
        }
    }

    /**
     * Drops the player's current held item and adds it to the room's item.
     * Outputs an error message if there is no item to drop.
     *
     * @param command a two-word command containing the word "drop" and the name of the item to drop.
     */
    private void drop(Command command) {
        if(!command.hasSecondWord()) {
            System.out.println("Drop what?");
        }
        else if (heldItem == null) {
            System.out.println("You are not holding an item!");
        }
        else {
            currentRoom.addItemToRoom(heldItem);
            System.out.println("You have dropped " + heldItem.name + ".");
            heldItem = null;

        }
    }

    /**
     * Charges the provided Beamer item.
     *
     * @param item the beamer to be charged.
     */
    public void charge(Item item) {
        if (item instanceof Beamer beamer) {
            if (!beamer.isBeamerCharged()) {
                System.out.println("Beamer charged!");
                beamer.charge(currentRoom);
            }
            else {
                System.out.println("You already have a room charged!");
            }
        }
        else {
            System.out.println("You are not holding a beamer!");
        }
    }

    /**
     * Fires the beamer and teleports the user to the charged room.
     *
     * @param item the beamer to be fired.
     */
    public void fire(Item item) {
        if (item instanceof Beamer beamer) {
            if (!beamer.isBeamerCharged()) {
                System.out.println("You have no room charged!");
            }
            else {
                System.out.println("Beamer fired!");
                currentRoom = beamer.fire();
                System.out.println(currentRoom.getLongDescription());
            }
        }
        else {
            System.out.println("You are not holding a beamer!");
        }

    }
}
