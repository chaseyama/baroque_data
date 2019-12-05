using System;
using System.IO;
using System.Collections.Generic;

namespace cs_test
{
    class Program
    {
        static void Main(string[] args)
        {
            using(var reader = new StreamReader("data_results.csv"))
            {
                List<string []> facebook_data = new List<string []>();
                while (!reader.EndOfStream)
                {
                    var line = reader.ReadLine();
                    var values = line.Split(',');
                    facebook_data.Add(values);

                    for (int i = 0; i < values.Length; i++) {
                        Console.Write(values[i] + ", ");
                    }
                    Console.WriteLine();
                }
            }
        }
    }
}
