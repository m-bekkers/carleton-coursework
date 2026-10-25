import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;

/**
 * A class modelling a tic-tac-toe (noughts and crosses, Xs and Os) game.
 *
 * @author Lynn Marshall
 * @version November 8, 2012
 *
 * @author Matthé Bekkers
 * @version March 31st, 2025
 */

public class TicTacToe {
    public static final String PLAYER_X = "X"; // player using "X"
    public static final String PLAYER_O = "O"; // player using "O"
    public static final String EMPTY = " ";  // empty cell
    public static final String TIE = "T"; // game ended in a tie

    private String player;   // current player (PLAYER_X or PLAYER_O)

    private String winner;   // winner: PLAYER_X, PLAYER_O, TIE, EMPTY = in progress

    private int numFreeSquares; // number of squares still free

    public Container board; // Container to hold the button frame

    public JPanel buttonPanel; // Panel to hold the buttons

    public JButton[][] buttons; // 2D array containing buttons

    public JLabel infoLabel; // Label containing information on the game state

    public JButton lastButton; // The button that was last clicked

    // row and col of the last selected tile
    public int row;
    public int col;

    /**
     * Constructs a new Tic-Tac-Toe board.
     */
    public TicTacToe() {
        // Create the menu bar
        JMenuBar menuBar = new JMenuBar();

        // Create a setup the frame to hold the game
        JFrame frame = new JFrame("TicTacToe");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);
        frame.setLayout(new BorderLayout());

        frame.setJMenuBar(menuBar);

        JMenu fileMenu = new JMenu("Game");
        menuBar.add(fileMenu);

        JMenuItem newItem = new JMenuItem("New");
        fileMenu.add(newItem);
        JMenuItem quitItem = new JMenuItem("Quit");
        fileMenu.add(quitItem);

        final int SHORTCUT_MASK = Toolkit.getDefaultToolkit().getMenuShortcutKeyMaskEx();
        newItem.setAccelerator((KeyStroke.getKeyStroke(KeyEvent.VK_N, SHORTCUT_MASK)));
        quitItem.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Q, SHORTCUT_MASK));

        newItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                clearBoard();
            }
        });

        quitItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });


        // Create the board that will hold the squares
        board = frame.getContentPane();

        // Create the button panel
        buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(3, 3));

        // Initialize the button array
        buttons = new JButton[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                JButton button = new JButton();
                int finalI = i;
                int finalJ = j;

                /**
                 * Action listener for each button. Most of the game's logic is contained within the listener
                 */
                button.addActionListener(new ActionListener() {
                    public void actionPerformed(ActionEvent e) {
                        buttons[finalI][finalJ].setFont(new Font("Arial", Font.PLAIN, 60));
                        button.setText(player);

                        // Swap players on click
                        if (player.equals(PLAYER_X)) {
                            player = PLAYER_O;
                        } else if (player.equals(PLAYER_O)) {
                            player = PLAYER_X;
                        }

                        // Add a reference to the lst button clicked to check for winner
                        lastButton = button;

                        // Need to do this (obviously)
                        numFreeSquares--;
                        button.setEnabled(false);
                        infoLabel.setText("Game is in progress... Player " + player + " to play");

                        row = finalI;
                        col = finalJ;

                        // Check and display what kind of ending we got
                        if (haveWinner(row, col)) {
                            if (winner.equals(TIE)) {
                                infoLabel.setText("Game over: It's a tie!");
                            } else {
                                infoLabel.setText("Game over: " + winner + " wins!");

                            }
                            disableButtons();
                        }

                    }
                });

                // Add the buttons to the panel
                buttons[i][j] = button;
                buttonPanel.add(buttons[i][j]);
            }
        }

        infoLabel = new JLabel("Game starting... Player X to play.");
        frame.add(buttonPanel);
        board.add(infoLabel, BorderLayout.SOUTH);

        numFreeSquares = 9;

        frame.setVisible(true);
    }

    /**
     * Sets everything up for a new game.  Marks all squares in the Tic Tac Toe board as empty,
     * and indicates no winner yet, 9 free squares and the current player is player X.
     */
    private void clearBoard() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                buttons[i][j].setText(EMPTY);
                buttons[i][j].setEnabled(true);
            }
        }
        winner = EMPTY;
        numFreeSquares = 9;
        player = PLAYER_X;     // Player X always has the first turn.
    }

    /**
     * Plays one game of Tic Tac Toe.
     */

    public void disableButtons() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                buttons[i][j].setEnabled(false);
            }
        }
    }

    /**
     * Plays the game.
     */
    public void playGame() {

        clearBoard();

        // loop until the game ends
        while (winner == EMPTY) { // game still in progress
            continue;
        }

    }

    /**
     * Returns true if filling the given square gives us a winner, and false
     * otherwise.
     *
     * @param row row of square just set
     * @param col col of square just set
     * @return true if we have a winner, false otherwise
     */
    private boolean haveWinner(int row, int col) {
        // We only check when at least 5 moves are made
        if (numFreeSquares > 4) return false;

        // Check row
        if (buttons[row][0].getText().equals(buttons[row][1].getText()) &&
                buttons[row][0].getText().equals(buttons[row][2].getText())) {
            winner = buttons[row][0].getText();
            return true;
        }

        // Check column
        if (buttons[0][col].getText().equals(buttons[1][col].getText()) &&
                buttons[0][col].getText().equals(buttons[2][col].getText())) {
            winner = buttons[0][col].getText();
            return true;
        }

        // Check main diagonal (top-left to bottom-right)
        if (row == col) {
            if (buttons[0][0].getText().equals(buttons[1][1].getText()) &&
                    buttons[0][0].getText().equals(buttons[2][2].getText())) {
                winner = buttons[0][0].getText(); // Use a fixed reference
                return true;
            }
        }

        // Check anti-diagonal (top-right to bottom-left)
        if (row + col == 2) {
            if (buttons[0][2].getText().equals(buttons[1][1].getText()) &&
                    buttons[0][2].getText().equals(buttons[2][0].getText())) {
                winner = buttons[0][2].getText(); // Use a fixed reference
                return true;
            }
        }

        // Check for a tie
        if (numFreeSquares == 0) {
            winner = TIE;
            return true;
        }

        return false; // No winner yet
    }
}