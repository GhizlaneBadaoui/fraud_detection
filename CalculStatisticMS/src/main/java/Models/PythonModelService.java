package Models;

import jep.Jep;
import jep.JepConfig;
import jep.JepException;
import jep.SubInterpreter;

public class PythonModelService {
    private SubInterpreter jep;
    String pathToScript;


    public PythonModelService() {
    }

    public void ModelService() {
        // Créer une nouvelle instance de SubInterpreter
        this.jep = new SubInterpreter();
        // Utilisez le SubInterpreter pour interagir avec Python
        this.jep.runScript("from main import init");

        // Prepare input data (this would be your Java input converted to Python-compatible data)
        // For example, if input_data is a list:

        // Call the Python predict function with input data
        jep.eval("result = init()");

        // Get the result from Python
        Object result = jep.getValue("result");
        System.out.println("Prediction result from Python: " + result);

    }


    public void usePythonModel() {
        try {
            this.jep.runScript(this.pathToScript);
            // Continuez avec l'entraînement du modèle et la prédiction comme avant
        } catch (JepException e) {
            e.printStackTrace();
        }
    }
    
    public void close() {
        if (this.jep != null) {
            this.jep.close();
        }
    }

    public static void main(String[] args) {
        PythonModelService pythonModelService = new PythonModelService();
        pythonModelService.ModelService();
    }



}