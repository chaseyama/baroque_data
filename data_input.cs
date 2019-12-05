using System;
					
public class Program
{
	public static void Main()
	{
		string[] categories = new string[]
            {"Arts", "Business", "Computers", "Games", "Health", "Home", "Recreation",
            "Science", "Society", "Sports"};

        string[][] twitter_interests =
            {
                new string[] {"Animation", "Music news and general info"}, // arts
                new string[] {}, // business
                new string[] {"Tech news", "Computer reviews"}, // computers
                new string[] {"Gaming news and general info", "Computer gaming", "Online gaming"}, // games
                new string[] {}, // health
                new string[] {}, // home
                new string[] {}, // recreation
                new string[] {"Space and astronomy", "Science news"}, // science
                new string[] {}, // society
                new string[] {"Sports news"}, // sports
            };

        string[][] facebook_interests =
            {
                new string[] {"Anime movies", "Castle (TV series)", "Comedy movies", "Empire (film magazine)", "Shopping and fashion"}, // arts
                new string[] {"Online shopping"}, // business
                new string[] {"Bluetooth", "Internet meme", "IPhone", "Meme"}, // computers
                new string[] {}, // games
                new string[] {}, // health
                new string[] {"Shopping"}, // home
                new string[] {"Northern California"}, // recreation
                new string[] {"California", "Cosmos", "Evolutionary psychology", "Memetics", "University of Southern California"}, // science
                new string[] {"Hippie", "Nancy Pelosi", "San Francisco"}, // society
                new string[] {"Rhett and Link", "San Francisco Bay Area", "Table tennis"}, // sports
            };

        double totalPrice = 0.6722;
        double[] prices = new double[] {0.1207, 0.0836, 0.0936, 0.0759, 0.0288, 0.0363, 0.084, 0.0315, 0.0442, 0.0736};

        Console.WriteLine(totalPrice);
        Console.WriteLine(prices[2]);
        Console.WriteLine(facebook_interests[0][0]);
        Console.WriteLine(categories[3]);

	}
}