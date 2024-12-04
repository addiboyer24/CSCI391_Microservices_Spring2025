package App.Application.Controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController()
@RequestMapping("/HealthCheck")
public class HealthCheckController {
    @GetMapping("/")
    public String Get(){
        return "I'm Healthy...";
    }
}
