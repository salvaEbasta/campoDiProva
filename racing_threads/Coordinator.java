package racing_threads;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

public class Coordinator{
    private List<Callable<?>> tasks;
    private ExecutorService exe;
    private List<Future<?>> promises;

    public Coordinator(List<Callable<?>> calls){
        tasks = calls;
        exe = Executors.newFixedThreadPool(calls.size());
        promises = new ArrayList<>();
    }

    public void run(){
        tasks.forEach(call->{
            promises.add(exe.submit(call));
        });
        boolean exit = false;
        try{
            while(!exit){
                TimeUnit.MILLISECONDS.sleep(100);
                for(int i=0; i<promises.size(); i++){
                    if(promises.get(i).isDone()){
                        System.out.println(String.format("Promise %d: done", i));
                        exit = true;
                        break;
                    }
                }
            }
            exe.shutdownNow();
        }catch(InterruptedException e){
            exe.shutdownNow();
            e.printStackTrace();
        }
    }
    
    public static void main(String[] args){
        List<Callable<?>> calls = new ArrayList<>();
        for(int i=0; i<5; i++)
            calls.add(new Task(i));
        Coordinator c = new Coordinator(calls);
        c.run();
    }
}