public static class Darts
{
    public static int Score(double x, double y)
    {
        double d2 = x * x + y * y;

        if (d2 <= 1)
            return 10;
        else if (d2 <= 25)
            return 5;
        else if (d2 <= 100)
            return 1;
        else
            return 0;
    }
}