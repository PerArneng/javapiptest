package com.scalebit.javapiptest;

public class Application {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("need a message as the first argument");
            System.exit(1);
        }
        String message = args[0];
        System.out.println(message);
        System.out.println("currently executing in: " + System.getProperty("user.dir"));
    }

}
