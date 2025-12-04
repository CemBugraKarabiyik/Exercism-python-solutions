static class LogLine
{
    public static string Message(string logLine)
    {
        int index = logLine.IndexOf(":");
        string rawMessage = logLine.Substring(index+1);
        string message = rawMessage.Trim();
        return message;
    }

    public static string LogLevel(string logLine)
    {
        int index1 = logLine.IndexOf("[");
        int index2 = logLine.IndexOf("]");
        string message = logLine[(index1+1)..index2].ToLower();
        return message;
    }

    public static string Reformat(string logLine)
    {
        string rawMessage = Message(logLine);
        string logMessage = LogLevel(logLine);
        string message = $"{rawMessage} ({logMessage})";
        return message;
        
    }
}
