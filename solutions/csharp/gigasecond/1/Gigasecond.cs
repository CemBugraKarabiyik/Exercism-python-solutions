public static class Gigasecond
{
    public static DateTime Add(DateTime moment)
    {
        DateTime gigaSecsAfter=moment.AddSeconds(1000000000);
        
        return gigaSecsAfter;
    }
}