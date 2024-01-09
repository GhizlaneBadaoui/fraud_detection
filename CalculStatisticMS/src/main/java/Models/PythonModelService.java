package Models;

import jep.Jep;
import jep.JepConfig;
import jep.JepException;
import jep.SubInterpreter;

public class PythonModelService {
    private SubInterpreter jep;
    String pathToScript;

    public PythonModelService(String path) {
        // Créer une nouvelle instance de SubInterpreter
        this.pathToScript = path;
        this.jep = new SubInterpreter();
        // Utilisez le SubInterpreter pour interagir avec Python

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



}