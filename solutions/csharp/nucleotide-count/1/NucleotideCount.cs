public static class NucleotideCount
{
    public static IDictionary<char, int> Count(string sequence)
    {
        int countA = 0;
        int countC = 0;
        int countG = 0;
        int countT = 0;
            
        for(int i=0;i<sequence.Length;i++)
        {
            if(sequence[i]=='A')
            {
                countA++;    
            }
            else if(sequence[i]=='C')
            {
                countC++;
            }
            else if(sequence[i] == 'G')
            {
                countG++;
            }
            else if(sequence[i] =='T')
            {
                countT++;
            }
            else 
            {
                throw new ArgumentException("error");
            }
          
        }
          var counts = new Dictionary<char, int>();

            counts.Add('A', countA);
            counts.Add('C', countC);
            counts.Add('G', countG);
            counts.Add('T', countT);

             return counts;
        
    }
}