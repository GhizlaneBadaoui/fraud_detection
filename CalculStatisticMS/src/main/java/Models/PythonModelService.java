package Models;

import org.python.util.PythonInterpreter;

public class PythonModelService {

    public static void main(String[] args) {
        try {

            PythonInterpreter pi = new PythonInterpreter();
            System.setProperty("python.home", "C:\\Users\\hp\\.m2\\repository\\org\\python\\jython-standalone");
            pi.exec("import sys");
            pi.exec("sys.path.append('CalculStatisticMS/src/main/java/Models/main.py')");
            pi.exec("import pandas");
            //
//            pi.exec("from main import init");
//            pi.exec("result = init()");
//            pi.exec("print(result)");
        }
        catch (Exception e){
            e.printStackTrace();
        }


    }



}