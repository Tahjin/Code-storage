import java.util.Scanner;

public class Truck{
    public static void main(String[]args){
        Scanner scnr = new Scanner(System.in);
        String Popsicle_Or_Icecream;
        String Ice_Or_Cream;
        String Flavor;
        System.out.println("Please enter one of the listed options. (Popsicle or Icecream): ");
        Popsicle_Or_Icecream = scnr.nextLine().toLowerCase();
        switch(Popsicle_Or_Icecream){
            case "popsicle":
               System.out.println("Chose what kind of popsicle (Ice or cream): ");
               Ice_Or_Cream = scnr.nextLine().toLowerCase();
               switch(Ice_Or_Cream){
                  case "ice":
                    System.out.println("The options for popsicles are: ");
                    System.out.println("    Watermelon\n    Grape\n    keylime");
                    System.out.println("Please enter a Flavor: ");
                    Flavor = scnr.nextLine().toLowerCase();                  
                    switch(Flavor){
                        case "watermelon":
                        case "grape":
                        case "keylime":
                           System.out.println("Here is your popsicle of "+Flavor);
                           break;
                        default:
                           System.out.println("That is not on the menue.");
                           break;
                     }
                     break;
              
                  case "cream":
                     System.out.println("The options for cream are: ");
                     System.out.println("    bombpop\n    bigbang\n    creamswirl");
                     System.out.println("Please enter a Flavor: ");
                     Flavor = scnr.nextLine().toLowerCase();                  
                     switch(Flavor){
                        case "bombpop":
                        case "bigbang":
                        case "creamswirl":
                           System.out.println("Here is your popsicle of "+Flavor);
                           break;
                        default:
                           System.out.println("That is not on the menue.");
                           break;//it's ignoreing this break for some reason
                     }
                     break;

                  default:
                     System.out.println("That is not on the menue.");
                     break;
               }
               break;
            case "icecream":
               System.out.println("The options for Ice-cream are: ");
               System.out.println("    Rockyroad\n    ChoclateMint\n    CookiesAndCream");
               System.out.println("Please enter a Flavor: ");
               Flavor = scnr.nextLine().toLowerCase();
               switch (Flavor){
                  case "rockyroad":
                  case "choclatemint":
                  case "cookiesandcream":
                     System.out.println("Here is your icecream cone of "+Flavor);
                     break;
                  default:
                     System.out.println("That is not on the menue.");
                     break;                
               }
               break;
            default:
               System.out.println("That is not on the menue.");
        }
  
     scnr.close();
     }
  }
  