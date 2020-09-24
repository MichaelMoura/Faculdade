public static void main(String[] args) {
       //foi utilizado o uso de expressões relugares 
       
       Scanner entrada = new Scanner(System.in);
       String letra; 
       
       System.out.print("Digite algum valor: ");
       letra = entrada.next();
       
       boolean palavra=letra.matches("[A-Za-z]*")==true;//expressão regular
       
       if(palavra==true){
		   System.out.println("O valor digitado é uma Letra");
       }else{
           System.out.println("O valor digitado é um número");       
       }
    }
