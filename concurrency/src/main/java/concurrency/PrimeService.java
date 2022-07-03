package concurrency;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Service
@RequestMapping("primes")
public class PrimeService {

    @GetMapping
    public ResponseEntity<Integer> getPrimes(@RequestParam int start, @RequestParam int end){
        int count=0;
        for(int i=start; i<=end; i++)
            if(isPrime(i)) count++;
        return ResponseEntity.ok(count);
    }

    private boolean isPrime(int n){
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++)
            if (n % i == 0) return false;
        return true;
    }
}
