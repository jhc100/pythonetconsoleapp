using Python.Runtime;
using System;

namespace ConsoleAppSF
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string pythonDll = @"C:\Python311\python311.dll";
            Environment.SetEnvironmentVariable("PYTHONNET_PYDLL", pythonDll);
            PythonEngine.Initialize();
            using (Py.GIL())
            {
                dynamic np = Py.Import("numpy");
                Console.WriteLine(np.cos(np.pi * 2.5));
            }
        }
    }
}
