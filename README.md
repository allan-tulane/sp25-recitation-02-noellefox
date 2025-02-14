# CMPS 2200  Recitation 02

**Name (Team Member 1):**___Noelle Fox______  
**Name (Team Member 2):**____Mohini Yaduv_______

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**TODO: your answer goes here**

**To derive the asymptotic behavior of W(n) when f(n) = 1, f(n) = logn, and f(n) = n I used the values a = 2 and b = 2 to create formulas in terms of big O. Because logb(a) utilizing my chosen values is equal to one I will be comparing f(n) to n^1 to derive the asymptotic behavior.**

- _When f(n) = 1_ The reccurence is leaf-dominated because the root level only does one unit of work while each deeper level does more work as the number of subproblems doubles. Thus, most of the work happens in the leaves and the asymptotic behavior can be represented with O(n).
- _When f(n) = logn_ The recurence is also a leaf-dominated function because logn is very small. The root will only be equal to logn and while moving deeper into the tree it breaks up into more subproblems thus producing more work than logn. Because the deeper you move into the tree the more work is done, the asymptotic behavior will be represented with O(n).
- _When f(n) = n_ The recurence would be considered balance because the work at the root is equivalent to the work at each deeper level. The work at the root in this case is equal to n, when you move to level 1 the work becomes equal to (n/2) + (n/2) which is also equal to n. Thus, the recursion is balanced and the asymptotic behavior can be represented with O(n logn) because n is the maximum cost per level and logn is the number of levels.
  
- Utilizing the test_work function I was able to test the growth of each of the three functions. These are the results I obtained:
  
        assert work_calc(8, 2, 2, lambda n: 1) == 15
        assert work_calc(16, 2, 2, lambda n: 1) == 31
        
        assert work_calc(8, 2, 2, lambda n: math.log(n, 2)) == 19
        assert work_calc(16, 2, 2, lambda n: math.log(n, 2)) == 42
        
        assert work_calc(8, 2, 2, lambda n: n) == 32
        assert work_calc(16, 2, 2, lambda n: n) == 80
  
  ^These actual values proved the derived aymptotic behavior trend that     work will increase from f(n) = 1 -> f(n) = logn -> f(n) = n. With the change from f(n) = 1 to f(n) = logn being minimal but prevalent and the change from f(n) = logn to f(n) = n being much more drastic. 
   


- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

**TODO: your answer goes here**
**For the reuccrence: W(n_ = aW(n/b)+f(n) where f(n) = n^c. We use the master theroem, where the behavior of W(nn) depends on the relationship between c and log b a. The first case is c < log b a where recursion dominates- an example is W1 (1000)= 697,496 which is much smaller than W2 (1000). This confirms that recursion dominates when c<log b a. The second case is c> log b a in which W2(1000) = 1,987,993,280, which confirms that n^c dominates for c> logba. The third case is the balanced case where c= logba and we can see that the growth is intermediate. An example of this is W3(1000) = 8,544,512 which is larger than case 1 but smaller than case 2. In conclusion, the results confirm the master theroem predictions, that recursion dominates when c is small, the work function dominates when c is large, and they balance when c=logba.  **
- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**TODO: your answer goes here**
- _For f(n) = 1_ when the asymptotic behavior is O(n) the span will be equivalent to O(logn). This is attained by following the single longest path, but because each level does constant additional work and to get to the base case we use 2^i = n or i = log2(n). Because each level only adds O(1) work and the total number of levels is O(log n) we get the span O(logn).
- _For f(n) = logn_ when the asymptotic behavior is O(n) the span will be equivalent to O(log^2(n)). Because the total number of levels is again O(logn) and each level adds O(logn) work we get the span O(log^2(n))
- _For f(n) = n_ when the asymptotic behavior is O(n logn) the span will be equivalent to O(n). Because again there are a total of O(logn) levels and the most work is done at the root, which does O(n) work, that is the single largest piece of work in the chain and the Span is equal to O(n). 
