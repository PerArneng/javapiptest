package com.scalebit.javapiptest;

import org.springframework.boot.Banner;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.context.ConfigurableApplicationContext;


@SpringBootApplication
public class Application {

    public static void main(String[] args) {

        ConfigurableApplicationContext context = new SpringApplicationBuilder()
                .sources(Application.class)
                .bannerMode(Banner.Mode.CONSOLE)
                .run(args);

        Application app = context.getBean(Application.class);
        app.start();
    }

    private void start() {
        System.out.println("Hello World!");
    }
}
