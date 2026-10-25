/**
 * RollOverCounter models a counter which cannot exceed its given bounds.
 * If the counter is asked to count beyond its bounds, it will rollover.
 * This counter can only count up or down by one at a time.
 *
 * @author Matthé Bekkers, Carleton University
 * @version 1.0.0, March 5th 2025
 */
public class RollOverCounter extends Counter
{
    /**
     * Constructs a new RollOverCounter whose current count is
     * initialized to DEFAULT_MINIMUM, and which counts between
     * DEFAULT_MINIMUM and DEFAULT_MAXIMUM, inclusive.
     */
    public RollOverCounter()
    {
        super();
    }

    /**
     * Constructs a new RollOverCounter whose current count is
     * initialized to minCount, and which counts between
     * minCount and maxCount, inclusive.
     */
    public RollOverCounter(int minCount, int maxCount)
    {
        super(minCount, maxCount);
    }

    /**
     * Increment this counter by 1.
     */
    public void countUp()
    {
        // If we've reached the maximum count, invoking this
        // method rolls the counter over to its minimum value.
        if (super.count() == super.maximumCount()) {
            super.reset();
        } else {
            super.countUp();
        }
    }

    /**
     * Decrement this counter by 1. If we have reached the minimum count,
     * invoking this method rolls the counter over to its maximum value.
     */
    public void countDown() {
        if (isAtMinimum()) {
            setToMaximum();
        }
        else {
            super.decrementCount();
        }
    }
}
