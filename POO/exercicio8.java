public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        String valor;
        
        System.out.println("Vamos verificar se o caracter é maiúsculo ou minúsculo");
        System.out.print("Digite alguma coisa: ");
        valor = entrada.next();
        
        boolean verificar=valor.matches("[a-zA-z&&[aeiouAEIOU]]")==true;
        boolean numero=valor.matches("[0-9]")==true;
                
        if(verificar==true && numero==false ){
            System.out.println("A letra digitada é uma vogal");
        }else if(verificar==false && numero==false){
            System.out.println("A letra digitada é uma consoante");
        }else{
            System.out.println("Desculpe, mas não é permitido a entrada de números");
        }
    }    
