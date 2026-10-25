/**
 * LimitedCounter models a counter which cannot exceed its given bounds.
 * This counter can only count up or down by one at a time.
 *
 * @author Matthé Bekkers, Carleton University
 * @version 1.0.0, March 5th 2025
 */
public class LimitedCounter extends Counter
{

    /**
     * Constructs a new LimitedCounter whose current count is
     * initialized to DEFAULT_MINIMUM, and which counts between
     * DEFAULT_MINIMUM and DEFAULT_MAXIMUM, inclusive.
     */
    public LimitedCounter()
    {
        super();
    }

    /**
     * Constructs a new LimitedCounter whose current count is
     * initialized to minCount, and which counts between
     * minCount and maxCount, inclusive.
     */
    public LimitedCounter(int minCount, int maxCount)
    {
        super(minCount, maxCount);
    }

    public void countUp()
    {
        // If we've reached the maximum count, invoking this
        // method doesn't change the state of the counter.
        if (super.count() != super.maximumCount()) {
            super.countUp();
        }
    }

    public void countDown() {
        if (super.count() == super.minimumCount()) {
            return;
        }
        else {
            decrementCount();
        }
    }
}
