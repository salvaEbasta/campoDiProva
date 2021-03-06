package racing_threads;

import java.util.concurrent.Callable;
import java.util.concurrent.TimeUnit;

public class Task implements Callable<Object>{
    private int i;
    public Task(int i){
        this.i = i+1;
    }

    public Object call(){
        try{
            TimeUnit.MILLISECONDS.sleep(i*100);
        }catch(InterruptedException e){
            System.out.println(String.format("Interrupted: %d", i));
        }
        return null;
    }
}
