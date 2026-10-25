import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.Border;

/**
 * A class modelling a tic-tac-toe (noughts and crosses, Xs and Os) game in a very
 * simple GUI window.
 * 
 * @author Lynn Marshall
 * @version November 8, 2012
 */

public class TicTacToeFrame extends TicTacToe 
{ 
    private JTextArea status; // text area to print game status
    private JFrame frame;
    private JScrollPane scroll;
    private JTextArea text;
   
   /** 
    * Constructs a new Tic-Tac-Toe board and sets up the basic
    * JFrame containing a JTextArea in a JScrollPane GUI.
    */
    public TicTacToeFrame()
    {
        frame = new JFrame("Tic Tac Toe");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);
        text = new JTextArea();
        scroll = new JScrollPane(text);
        frame.setLayout(new BorderLayout());
        frame.add(scroll, BorderLayout.CENTER);
        frame.setVisible(true);

    }
   
    /**
     * Prints the board to the GUI using toString().
     */
     public void print()
     {
         text.append(toString());

     }

}