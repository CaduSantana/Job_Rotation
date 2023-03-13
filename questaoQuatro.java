// 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
// Descreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

public class questaoQuatro {
    public static void main(String[] args) {
        double sp = 67836.43;
        double rj = 36678.66;  
        double mg = 29229.88;
        double es = 27165.48;
        double outros = 19849.53;

        double total = sp + rj + mg + es + outros;

        System.out.println("Faturamento por estado");
        
        // Percentual de cada estado
        System.out.println("São Paulo: " + (sp / total) * 100 + "%");
        System.out.println("Rio de Janeiro: " + (rj / total) * 100 + "%");
        System.out.println("Minas Gerais: " + (mg / total) * 100 + "%");
        System.out.println("Espírito Santo: " + (es / total) * 100 + "%");
        System.out.println("Outros: " + (outros / total) * 100 + "%");

    }
}
