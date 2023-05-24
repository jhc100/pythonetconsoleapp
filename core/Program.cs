using Python.Runtime;

internal class Program
{
    static void Main(string[] args)
    {
        string pythonDll = @"C:\Users\Luis Estebarra\AppData\Local\Programs\Python\Python39\python39.dll";
        Environment.SetEnvironmentVariable("PYTHONNET_PYDLL", pythonDll);
        PythonEngine.Initialize();
        using (Py.GIL())
        {
            dynamic os = Py.Import("os");
            dynamic sys = Py.Import("sys");
            sys.path.append(os.path.dirname(os.path.expanduser("sentence_sim.py")));
            dynamic sentence_sim = Py.Import(Path.GetFileNameWithoutExtension("sentence_sim.py"));
            Console.WriteLine(sentence_sim.semantic_sim("Hola","Adios"));
        }
    }
}