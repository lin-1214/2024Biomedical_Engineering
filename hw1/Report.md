# Homework 1 Due: 1002

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" }); </script>

## 1.
![q1_solution](./img/q1.jpg)

---
## 2.
### (a)
The three molecules are viral RNA, viral antigen and antibody

### (b)
`Inactive whole virus`：When injected, the immune system recognizes the viral antigens and produces antibodies to fight the virus. These antibodies will be ready to respond to future exposures to the live virus.

`Antigen proteins`：The immune system identifies these proteins as foreign antigens and generates an immune response, including producing antibodies that recognize and neutralize the virus if encountered later.

`mRNA(genetic instructions)`：The mRNA vaccines contain a small piece of the virus’s genetic material that provides instructions for cells to make the spike protein found on the surface of SARS-CoV-2. Once cells produce this spike protein, the immune system detects it and generates a response, including the production of antibodies and memory cells to recognize the virus in the future.

`DNA (genetic instructions)`: After being delivered into the body, cells take up the DNA, produce the spike protein, and display it on their surface. The immune system responds by producing antibodies and T cells, which prepare the body to fight the actual virus if it is encountered later.

---
<div style="page-break-after: always;"></div>

## 3.
### (a)
Solution implemented in with Python in `plot.py`

![q3_code](./img/solve_sir.png)
<div style="page-break-after: always;"></div>
Result when $\nu = 0.05$ 

![q3_a](./img/sir_model_0.05.png)


### (b)
Compare result of different $\nu$

$\nu = 0.0$

![q3_b_0](./img/sir_model_0.0.png)
<div style="page-break-after: always;"></div>
$\nu = 0.10$

![q3_b_1](./img/sir_model_0.1.png)

$\nu = 0.30$

![q3_b_2](./img/sir_model_0.3.png)

By comparing the results of different $\nu$, we can find that when $\nu$ increases, the number of susceptible individuals decreases faster, and the number of recovered individuals increases faster. This is because the vaccination rate $\nu$ reduces the number of susceptible individuals by vaccinating them, and also reduces the number of infected individuals by reducing the contact rate.

---
## 4. Souce Code
[github](https://github.com/lin-1214/2024Biomedical_Engineering/blob/main/hw1/plot.py)