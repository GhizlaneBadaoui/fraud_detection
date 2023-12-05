package insa.project.microservicesdecouvertems;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

@SpringBootApplication
@EnableEurekaServer
public class MicroServicesDecouverteMsApplication {

    public static void main(String[] args) {
        SpringApplication.run(MicroServicesDecouverteMsApplication.class, args);
    }

}
