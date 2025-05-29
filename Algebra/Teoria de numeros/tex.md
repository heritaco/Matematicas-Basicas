A continuación tienes una recopilación de los principales teoremas y resultados de **Teoría de Números** en las áreas de congruencias, aritmética modular, teoremas clásicos, números primos, factorización única y funciones aritméticas.

---

## 1. Congruencias y aritmética modular

1. **Relaciones de congruencia**
   Para enteros $a,b,m$ con $m>0$,

   $$
     a \equiv b \pmod m
     \quad\Longleftrightarrow\quad
     m\mid (a-b).
   $$

   Se preserva bajo suma, resta y multiplicación:

   $$
     a\equiv b,\;c\equiv d\pmod m
     \;\Longrightarrow\;
     a\pm c\equiv b\pm d,\;
     a\,c\equiv b\,d\pmod m.
   $$

2. **Solución de la congruencia lineal**
   La congruencia
   $\displaystyle a\,x \equiv b\pmod m$
   tiene solución si y sólo si $\gcd(a,m)\mid b$.
   En ese caso, hay exactamente $\gcd(a,m)$ clases solución módulo $m$.

3. **Teorema Chino del Resto (CRT)**
   Si $m_1,\dots,m_k$ son coprimos dos a dos, entonces el sistema

   $$
     x \equiv a_i\pmod{m_i},\quad i=1,\dots,k
   $$

   tiene una única solución módulo $M=m_1\cdots m_k$.
   Además, esta solución se puede construir explícitamente mediante combinaciones lineales.

---

## 2. Teoremas clásicos de aritmética modular

1. **Pequeño Teorema de Fermat**
   Si $p$ es primo y $p\nmid a$, entonces

   $$
     a^{p-1}\equiv1\pmod p.
   $$

2. **Teorema de Euler**
   Para $a$ y $n$ coprimos,

   $$
     a^{\varphi(n)}\equiv1\pmod n,
   $$

   donde $\varphi(n)$ es la función totiente de Euler.

3. **Teorema de Wilson**
   Un entero $p>1$ es primo si y solo si

   $$
     (p-1)!\equiv -1\pmod p.
   $$

4. **Criterio de Euler (para residuos cuadráticos)**
   Si $p$ es primo impar y $a$ entero no divisible por $p$, entonces

   $$
     a^{\frac{p-1}2}
     \equiv
     \begin{cases}
       1\pmod p,&\text{si }a\text{ es un residuo cuadrático},\\
      -1\pmod p,&\text{si }a\text{ es no residuo cuadrático}.
     \end{cases}
   $$

5. **Reciprocidad cuadrática de Gauss**
   Para primos impares $p\neq q$,

   $$
     \Bigl(\tfrac pq\Bigr)\,\Bigl(\tfrac qp\Bigr)
     = (-1)^{\frac{p-1}2\,\frac{q-1}2},
   $$

   donde $\bigl(\tfrac ap\bigr)$ es el símbolo de Legendre.

---

## 3. Números primos y factorización única

1. **Infinitud de los primos (Euclides)**
   No existe un último número primo; hay infinitamente muchos.

2. **Lema de Euclides**
   Si un primo $p$ divide el producto $a\,b$, entonces $p$ divide a $a$ o a $b$.

3. **Teorema Fundamental de la Aritmética**
   Todo entero $n>1$ se descompone de manera única —salvo el orden de los factores— como

   $$
     n = p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k},
   $$

   con $p_i$ primos y $e_i\ge1$.

4. **Estimación de la distribución de primos (aproximada)**
   La cantidad $\pi(x)$ de primos $\le x$ satisface

   $$
     \pi(x)\sim \frac{x}{\ln x}
     \quad(x\to\infty),
   $$

   según el Teorema de los Números Primos.

---

## 4. Funciones aritméticas y sus propiedades

1. **Función totiente de Euler**
   $\displaystyle \varphi(n)=\#\{\,1\le k\le n:\gcd(k,n)=1\}.$
   Es función multiplicativa y para la descomposición $n=\prod p_i^{e_i}$ vale

   $$
     \varphi(n)
     = n\prod_{i}\Bigl(1-\tfrac1{p_i}\Bigr).
   $$

2. **Función de Möbius**

   $$
     \mu(n)=
     \begin{cases}
       1,&n=1,\\
       (-1)^k,&n\text{ producto de }k\text{ primos distintos},\\
       0,&\text{si }p^2\mid n\text{ para algún primo }p.
     \end{cases}
   $$

   Es multiplicativa y satisface la inversión de Möbius:

   $$
     f(n)
     = \sum_{d\mid n}g(d)
     \quad\Longleftrightarrow\quad
     g(n)
     = \sum_{d\mid n}\mu(d)\,f\bigl(\tfrac n d\bigr).
   $$

3. **Suma de divisores y multiplicatividad**
   La suma de divisores $\sigma(n)=\sum_{d\mid n}d$ es multiplicativa.
   Para $n=\prod p_i^{e_i}$:

   $$
     \sigma(n)
     = \prod_i\frac{p_i^{e_i+1}-1}{p_i-1}.
   $$

4. **Relación totiente–suma de divisores**

   $$
     \sum_{d\mid n}\varphi(d)=n,
     \quad
     \sum_{d\mid n}\mu(d)=
     \begin{cases}
       1,&n=1,\\
       0,&n>1.
     \end{cases}
   $$

5. **Función Liouville**
   $\displaystyle \lambda(n)=(-1)^{\Omega(n)},$ donde $\Omega(n)$ cuenta primos con multiplicidad. Es completamente multiplicativa.

---

## 5. Resultados auxiliares

1. **Fórmula de Legendre (exponente de $p$ en $n!$)**
   Para primo $p$,

   $$
     v_p(n!)
     = \sum_{k=1}^{\infty}\Big\lfloor\frac{n}{p^k}\Big\rfloor.
   $$

2. **Lema de Lifting The Exponent (LTE)**
   Para $p$ primo impar con $p\mid a-b$ pero $p\nmid ab$:

   $$
     v_p(a^n - b^n)
     = v_p(a-b) + v_p(n).
   $$

---

Estos teoremas forman la base de la teoría de números elemental y son imprescindibles para resolver problemas de concurso (Putnam, olimpiadas, etc.). Si deseas que profundice en la demostración de alguno o en aplicaciones concretas, ¡avísame!
