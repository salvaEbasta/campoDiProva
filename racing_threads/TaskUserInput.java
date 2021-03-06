package racing_threads;

import java.io.IOException;
import java.util.concurrent.Callable;
import java.util.concurrent.TimeUnit;

public class TaskUserInput implements Callable<String>{
    public String call(){
        //try{}catch(){}
        String usr_in = "";
        try{
            while(true){
                TimeUnit.MILLISECONDS.sleep(100);
                System.out.println("Polling");
                if(System.in.available() != 0){
                    int c = System.in.read();
                    System.out.println("Read: "+c);
                    if(c == 0x1B){
                        break;
                    }
                }
            }
        }catch(InterruptedException e){
            e.printStackTrace();
            System.out.println("Reading usr input Interrupted");
        }catch(IOException e){
            e.printStackTrace();
            System.out.println("Reading usr input IOException");
        }
        return usr_in;
    }

    public static void main(String[] args){
        new TaskUserInput().call();
    }
}
