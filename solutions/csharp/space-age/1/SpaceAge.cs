public class SpaceAge
{

    private int seconds;
    
    public SpaceAge(int seconds)
    {
      this.seconds=seconds;  
    }

    public double OnEarth()
    {
        double ageinEarth = seconds/31557600.0;
        return ageinEarth;
    }

    public double OnMercury()
    {
        double ageinmercury = (seconds/31557600.0)/0.2408467;
        return ageinmercury;
    }

    public double OnVenus()
    {
       double ageinvenus= (seconds/31557600.0)/0.61519726;
       return ageinvenus;
    }

    public double OnMars()
    {
        double ageinmars=(seconds/31557600.0)/1.8808158;
        return ageinmars;
    }

    public double OnJupiter()
    {
        double ageinjupiter = (seconds/31557600.0)/11.862615;
        return ageinjupiter;
    }

    public double OnSaturn()
    {
        double ageinsaturn = (seconds/31557600.0)/29.447498;
        return ageinsaturn;
    }

    public double OnUranus()
    {
        double ageinuranus= (seconds/31557600.0)/84.016846;
        return ageinuranus;
    }

    public double OnNeptune()
    {
        double ageinneptune = (seconds/31557600.0)/164.79132;
        return ageinneptune;
    }
}    