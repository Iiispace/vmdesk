<div style="background-color: #909190; padding: 40px;">

# **Functions**

The following functions work with **general expressions**

## Constants

```
i, j
    Imaginary unit
```
```
e
    Euler’s number, the base of natural logarithms
```
```
π, pi
    The ratio of the circumference of a circle to its diameter
```
```
tau
    2π
```
```
^
    power
```
```
!
    Factorial
```
```
%
    ÷100
```
```
x
    Current value
```
```
o
    Original value
```

## Length Units

All length units are ignore lowercase/uppercase
```
km
kilometer
kilometers
    Convert kilometers to attribute units
```
```
m
meter
meters
    Convert meters to attribute units
```
```
cm
centimeter
centimeters
    Convert centimeters to attribute units
```
```
mm
millimeter
millimeters
    Convert millimeters to attribute units
```
```
um
μ
mμ
micrometer
micrometers
    Convert micrometers to attribute units
```
```
mi
mile
miles
    Convert miles to attribute units
```
```
ft
feet
foot
    Convert feet to attribute units
```
```
in
inche
inches
    Convert inches to attribute units
```
```
mil
thou
    Convert thou to attribute units
```
```
Example:
    Scene Length unit: Inches
    Scene Unit Scale: 1.5

    Input:          2 + 4 mm + 6 ft
    Output:         74.15748
    Python value:   74.15748 * 0.0254 / 1.5 = 1.2557333
```

## Functions

```
seed()
    Same as Python version in random module.
    Initialize the random number generator.
```
```
getstate()
    Same as Python version in random module.
    Return an object capturing the current internal state of the generator.
    This object can be passed to setstate() to restore the state.
```
```
setstate(state)
    Same as Python version in random module.
    state should have been obtained from a previous call to getstate(), and setstate()
    restores the internal state of the generator to what it was at the time getstate() was called.
```
```
randbytes(n)
    Same as Python version in random module.
    Generate n random bytes.
    Parameters:
        n (integer > 0)

    Input:      int(randbytes(5).hex(), 16)
    Output:     621644248778
```
```
randrange(stop)
randrange(start, stop, step=1)
    Same as Python version in random module.
    Return a randomly selected element from range(start, stop, step).
    Parameters:
        start (integer)
        stop (integer)
        step (integer (optional))

    Input:      randrange(3, 6, 2)
    Output:     3
```
```
randint(a, b)
    Same as Python version in random module.
    Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
    Parameters:
        a (integer)
        b (integer)
```
```
getrandbits(k)
    Same as Python version in random module.
    Returns a non-negative Python integer with k random bits. This method is supplied with 
    the Mersenne Twister generator and some other generators may also provide it as 
    an optional part of the API. When available, getrandbits() enables randrange() 
    to handle arbitrarily large ranges.
    Parameters:
        k (nonnegaive integer)

    Input:      getrandbits(5)
    Output:     30
```
```
choice(seq)
    Same as Python version in random module.
    Return a random element from the non-empty sequence seq.
    Parameters:
        seq (sequence)

    Input:      choice((2, 3, 4))
    Output:     2
```
```
choices(population, k=1, weights=None, cum_weights=None)
    Return a k sized list of elements chosen from the population with replacement. 
    If a weights sequence is specified, selections are made according to the relative weights. 
    Alternatively, if a cum_weights sequence is given, the selections are made according 
    to the cumulative weights. For example, the relative weights [10, 5, 30, 5] 
    are equivalent to the cumulative weights [10, 15, 45, 50]. Internally, 
    the relative weights are converted to cumulative weights before making selections.
    Parameters:
        population (sequence)
        k (integer > 0 (optional))
        weights (sequence (optional))
        cum_weights (sequence (optional))

    Input:      sum(choices((1, 2, 3, 4), 1000)) / 1000
    Output:     2.506

    Input:      sum(choices((1, 2, 3, 4), 1000, None, (1, 1, 1, 1))) / 1000
    Output:     1
```
```
shuffle(seq)
    Same as Python version in random module.
    Shuffle the sequence x in place.
    Parameters:
        seq (sequence)

    Input:      shuffle((1, 2, 3, 4))[0]
    Output:     2
```
```
sample(population, k, counts=None)
    Same as Python version in random module.
    Return a k length list of unique elements chosen from the population sequence. 
    Used for random sampling without replacement.
    Returns a new list containing elements from the population while leaving 
    the original population unchanged. The resulting list is in selection order 
    so that all sub-slices will also be valid random samples. 
    This allows raffle winners (the sample) to be partitioned into grand prize 
    and second place winners (the subslices).
    Members of the population need not be hashable or unique. 
    If the population contains repeats, then each occurrence is a possible selection 
    in the sample. Repeated elements can be specified one at a time or with the 
    optional keyword-only counts parameter. 
    For example, sample([‘red’, ‘blue’], counts=[4, 2], k=5) 
    is equivalent to sample([‘red’, ‘red’, ‘red’, ‘red’, ‘blue’, ‘blue’], k=5).
    Parameters:
        population (sequence)
        k (integer > 0)
        counts (sequence (optional))

    Input:      sum(sample((1, 1, 2, 2, 3, 4), 4))
    Output:     9

    Input:      sum(sample((1, 2, 3, 4), 4, (2, 2, 1, 1)))
    Output:     8
```
```
random()
    Same as Python version in random module.
    Return the next random floating point number in the range [0.0, 1.0).
```
```
uniform(a, b)
    Same as Python version in random module.
    Return a random floating point number N such that 
    a <= N <= b for a <= b and b <= N <= a for b < a.
    The end-point value b may or may not be included in the range 
    depending on floating-point rounding in the equation a + (b-a) * random().
    Parameters:
        a (float)
        b (float)

    Input:      uniform(-2.3, 7.2)
    Output:     -0.7599512525748
```
```
triangular(low, high, mode)
    Same as Python version in random module.
    Return a random floating point number N such that low <= N <= high 
    and with the specified mode between those bounds. The low and high 
    bounds default to zero and one. The mode argument defaults to the 
    midpoint between the bounds, giving a symmetric distribution.
    Parameters:
        low (float)
        high (float)
        mode (float)

    Input:      triangular(-2.1, 5.6, 3.1)
    Output:     4.650596214649
```
```
betavariate(alpha, beta)
    Same as Python version in random module.
    Beta distribution. Conditions on the parameters are alpha > 0 
    and beta > 0. Returned values range between 0 and 1.
    Parameters:
        alpha (float)
        beta (float)

    Input:      betavariate(2.1, 2.2)
    Output:     0.5409938021106
```
```
expovariate(lambd)
    Same as Python version in random module.
    Exponential distribution. lambd is 1.0 divided by the desired mean. 
    It should be nonzero. (The parameter would be called “lambda”, 
    but that is a reserved word in Python.) 
    Returned values range from 0 to positive infinity if lambd is positive, 
    and from negative infinity to 0 if lambd is negative.
    Parameters:
        lambd (float)

    Input:      expovariate(2)
    Output:     0.029974233415711
```
```
gammavariate(alpha, beta)
    Same as Python version in random module.
    Gamma distribution. (Not the gamma function!) Conditions on the 
    parameters are alpha > 0 and beta > 0.
    Parameters:
        alpha (float)
        beta (float)

    Input:      gammavariate(2.1, 2.2)
    Output:     9.419232015484
```
```
gauss(mu, sigma)
    Same as Python version in random module.
    Normal distribution, also called the Gaussian distribution. mu is the mean, 
    and sigma is the standard deviation. This is slightly faster than 
    the normalvariate() function defined below.
    Multithreading note: When two threads call this function simultaneously, 
    it is possible that they will receive the same return value. 
    This can be avoided in three ways. 1) Have each thread use a 
    different instance of the random number generator. 2) Put locks around all calls. 3) 
    Use the slower, but thread-safe normalvariate() function instead.
    Parameters:
        mu (float)
        sigma (float)

    Input:      gauss(0, 1)
    Output:     2.3667486814625
```
```
lognormvariate(mu, sigma)
    Same as Python version in random module.
    Log normal distribution. If you take the natural logarithm of this distribution, 
    you’ll get a normal distribution with mean mu and standard deviation sigma. 
    mu can have any value, and sigma must be greater than zero.
    Parameters:
        mu (float)
        sigma (float)

    Input:      lognormvariate(0, 1)
    Output:     1.615633099343
```
```
normalvariate(mu, sigma)
    Same as Python version in random module.
    Normal distribution. mu is the mean, and sigma is the standard deviation.
    Parameters:
        mu (float)
        sigma (float)

    Input:      normalvariate(0, 1)
    Output:     1.87181748392
```
```
vonmisesvariate(mu, kappa)
    Same as Python version in random module.
    mu is the mean angle, expressed in radians between 0 and 2*pi, 
    and kappa is the concentration parameter, which must be greater than or equal to zero. 
    If kappa is equal to zero, this distribution reduces to a uniform random angle 
    over the range 0 to 2*pi.
    Parameters:
        mu (float)
        kappa (float)

    Input:      vonmisesvariate(0, 1)
    Output:     0.1528172805248
```
```
paretovariate(alpha)
    Same as Python version in random module.
    Pareto distribution. alpha is the shape parameter.
    Parameters:
        alpha (float)

    Input:      paretovariate(2.1)
    Output:     1.9917223270650
```
```
weibullvariate(alpha, beta)
    Same as Python version in random module.
    Weibull distribution. alpha is the scale parameter and beta is the shape parameter.
    Parameters:
        alpha (float)
        beta (float)

    Input:      weibullvariate(2.1, 2.2)
    Output:     4.055761225935
```
```
phase(x)
    Same as Python version in cmath module.
    Return the phase of x.
    Parameters:
        x (complex)

    Input:      phase(1 + i)
    Output:     0.785398163397
```
```
polar(x)
    Same as Python version in cmath module.
    Return the representation of x in polar coordinates. Returns a pair (r, phi) 
    where r is the modulus of x and phi is the phase of x. polar(x) is equivalent to 
    (abs(x), phase(x)).
    Parameters:
        x (complex)

    Input:      polar(1 + i)[1]
    Output:     0.785398163397
```
```
rect(r, θ)
    Same as Python version in cmath module.
    Return the complex number x with polar coordinates r and θ. Equivalent to r (cos θ + i sin θ).
    Parameters:
        r (float)
        θ (float)

    Input:      rect(2, 5)
    Output:     0.5673243709265 - 1.917848549326 i
```
```
exp(x)
    Same as Python version in cmath module.
    Return e raised to the power x, where e is the base of natural logarithms.
    Parameters:
        x (complex)

    Input:      exp(i*pi)
    Output:     -1
```
```
log(x, base=10)
log10(x, base=10)
    Logarithm in base 10. There is one branch cut, from 0 along the negative real axis to -∞, 
    continuous from above.
    Parameters:
        x (complex)
        base (complex (optional))

    Input:      log(10)
    Output:     1

    Input:      log(8, 2)
    Output:     3
```
```
log2(x, base=2)
    Logarithm in base 2.
    Parameters:
        x (complex)
        base (complex (optional))

    Input:      log2(2)
    Output:     1
```
```
ln(x, base=e)
    Natural logarithm.
    Parameters:
        x (complex)
        base (complex (optional))

    Input:      ln(e)
    Output:     1
```
```
sqrt(x, root=2)
rt(x, root=2)
    Square root.
    Parameters:
        x (complex)
        root (complex (optional))

    Input:      sqrt(4)
    Output:     2

    Input:      sqrt(8, 3)
    Output:     2
```
```
acos(x, unit=None)
    Return the arc cosine of x. 
    There are two branch cuts: One extends right from 1 along the real axis to ∞. 
    The other extends left from -1 along the real axis to -∞.
    Parameters:
        x (complex)
        unit (optional) : d

    Input:      acos(rt(2)/2)
    Output:     0.7853981633974

    Input:      acos(rt(2)/2, d)
    Output:     45
```
```
asin(x, unit=None)
    Return the arc sine of x. This has the same branch cuts as acos().
    Parameters:
        x (complex)
        unit (optional) : d

    Input:      asin(rt(2)/2)
    Output:     0.7853981633974

    Input:      asin(rt(2)/2, d)
    Output:     45
```
```
atan(x, unit=None)
    Return the arc tangent of x. 
    There are two branch cuts: One extends from i along the imaginary axis to ∞i. 
    The other extends from -i along the imaginary axis to -∞i.
    Parameters:
        x (complex)
        unit (optional) : d

    Input:      atan(1)
    Output:     0.7853981633974

    Input:      atan(1, d)
    Output:     45
```
```
asec(x, unit=None)
    Return the arc secant of x.
    Parameters:
        x (complex)
        unit (optional) : d

    Input:      asec(2)
    Output:     1.0471975511966

    Input:      asec(2, d)
    Output:     60
```
```
acsc(x, unit=None)
    Return the arc cosecant of x.
    Parameters:
        x (complex)
        unit (optional) : d

    Input:      acsc(2)
    Output:     0.5235987755983

    Input:      acsc(2, d)
    Output:     30
```
```
acot(x, unit=None)
    Return the arc cotangent of x.
    Parameters:
        x (complex)
        unit (optional) : d

    Input:      acot(2)
    Output:     0.4636476090008

    Input:      acot(2, d)
    Output:     26.565051177078
```
```
cos(x, unit=None)
    Return the cosine of x.
    Parameters:
        x (complex)
        unit (optional) : d

    Input:      cos(pi)
    Output:     -1

    Input:      cos(180, d)
    Output:     -1
```
```
sin(x, unit=None)
    Return the sine of x.
    Parameters:
        x (complex)
        unit (optional) : d

    Input:      sin(pi)
    Output:     0

    Input:      sin(180, d)
    Output:     0
```
```
tan(x, unit=None)
    Return the tangent of x.
    Parameters:
        x (complex)
        unit (optional) : d

    Input:      tan(pi/4)
    Output:     1

    Input:      tan(45, d)
    Output:     1
```
```
sec(x, unit=None)
    Return the secant of x.
    Parameters:
        x (complex)
        unit (optional) : d

    Input:      sec(pi/4)
    Output:     1.414213562373

    Input:      sec(45, d)
    Output:     1.414213562373
```
```
csc(x, unit=None)
    Return the cosecant of x.
    Parameters:
        x (complex)
        unit (optional) : d

    Input:      csc(pi/3)
    Output:     1.1547005383793

    Input:      csc(60, d)
    Output:     1.1547005383793
```
```
cot(x, unit=None)
    Return the cotangent of x.
    Parameters:
        x (complex)
        unit (optional) : d

    Input:      cot(pi/3)
    Output:     0.5773502691896

    Input:      cot(60, d)
    Output:     0.5773502691896
```
```
acosh(x)
    Return the inverse hyperbolic cosine of x. There is one branch cut, 
    extending left from 1 along the real axis to -∞.
    Parameters:
        x (complex)

    Input:      acosh(2)
    Output:     1.3169578969248
```
```
asinh(x)
    Return the inverse hyperbolic sine of x. There are two branch cuts: 
    One extends from i along the imaginary axis to ∞i. 
    The other extends from -i along the imaginary axis to -∞i.
    Parameters:
        x (complex)

    Input:      asinh(2)
    Output:     1.4436354751788
```
```
atanh(x)
    Return the inverse hyperbolic tangent of x. There are two branch cuts: 
    One extends from 1 along the real axis to ∞. 
    The other extends from -1 along the real axis to -∞.
    Parameters:
        x (complex)

    Input:      atanh(0.5)
    Output:     0.5493061443341
```
```
asech(x)
    Return the inverse hyperbolic secant of x.
    Parameters:
        x (complex)

    Input:      asech(0.5)
    Output:     1.3169578969248
```
```
acsch(x)
    Return the inverse hyperbolic cosecant of x.
    Parameters:
        x (complex)

    Input:      acsch(0.5)
    Output:     1.4436354751788
```
```
acoth(x)
    Return the inverse hyperbolic cotangent of x.
    Parameters:
        x (complex)

    Input:      acoth(2)
    Output:     0.54930614433405
```
```
cosh(x)
    Return the hyperbolic cosine of x.
    Parameters:
        x (complex)

    Input:      cosh(pi)
    Output:     11.5919532755215
```
```
sinh(x)
    Return the hyperbolic sine of x.
    Parameters:
        x (complex)

    Input:      sinh(pi)
    Output:     11.5487393572577
```
```
tanh(x)
    Return the hyperbolic tangent of x.
    Parameters:
        x (complex)

    Input:      tanh(pi)
    Output:     0.99627207622
```
```
sech(x)
    Return the hyperbolic secant of x.
    Parameters:
        x (complex)

    Input:      sech(pi)
    Output:     0.08626673833405
```
```
csch(x)
    Return the hyperbolic cosecant of x.
    Parameters:
        x (complex)

    Input:      csch(pi)
    Output:     0.08658953753005
```
```
coth(x)
    Return the hyperbolic cotangent of x.
    Parameters:
        x (complex)

    Input:      coth(pi)
    Output:     1.0037418731973
```
```
isfinite(x)
    Same as Python version in cmath module.
    Return True if both the real and imaginary parts of x are finite, and False otherwise.
    Parameters:
        x (complex)

    Input:      int(isfinite(inf))
    Output:     0
```
```
isinf(x)
    Same as Python version in cmath module.
    Return True if either the real or the imaginary part of x is an infinity, and False otherwise.
    Parameters:
        x (complex)

    Input:      int(isinf(inf))
    Output:     1
```
```
isnan(x)
    Same as Python version in cmath module.
    Return True if either the real or the imaginary part of x is a NaN, and False otherwise.
    Parameters:
        x (complex)

    Input:      int(isnan(nan))
    Output:     1
```
```
isclose(a, b, rel_tot=10**-9, abs_tol=0.0)
    Same as Python version in cmath module.
    Return True if the values a and b are close to each other and False otherwise.
    Whether or not two values are considered close is determined according to given absolute 
    and relative tolerances.
    rel_tol is the relative tolerance – it is the maximum allowed difference between a and b, 
    relative to the larger absolute value of a or b. For example, to set a tolerance of 5%, 
    pass rel_tol=0.05. The default tolerance is 1e-09, which assures that the two values 
    are the same within about 9 decimal digits. rel_tol must be greater than zero.
    abs_tol is the minimum absolute tolerance – useful for comparisons near zero. 
    abs_tol must be at least zero.
    If no errors occur, the result will be: abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol).
    The IEEE 754 special values of NaN, inf, and -inf will be handled according to IEEE rules. 
    Specifically, NaN is not considered close to any other value, including NaN. 
    inf and -inf are only considered close to themselves.
    Parameters:
        a (complex)
        b (complex)
        rel_tot (float (optional))
        abs_tot (float (optional))

    Input:      int(isclose(1, 1 + 10^-10))
    Output:     1
```
```
Re(x)
    Same as z.real
    Return the real part of a complex number.
    Parameters:
        x (complex)

    Input:      Re(1 + i)
    Output:     1
```
```
Im(x)
    Same as z.imag
    Return the imaginary part of a complex number.
    Parameters:
        x (complex)

    Input:      Im(1 + i)
    Output:     i
```
```
conj(x)
    Same as Python version.
    Return the complex conjugate.
    Parameters:
        x (complex)

    Input:      conj(1 + i)
    Output:     1 - i
```
```
ceil(x)
    Return the ceiling of x, the smallest integer greater than or equal to x.
    Parameters:
        x (float)

    Input:      ceil(8.1)
    Output:     9
```
```
C(n, r)
comb(n, r)
    Combination.
    Parameters:
        n (integer >= 0)
        r (integer >= 0)

    Input:      comb(5, 2)
    Output:     10
```
```
copysign(x, y)
    Same as Python version in math module.
    Return a float with the magnitude (absolute value) of x but the sign of y. 
    On platforms that support signed zeros, copysign(1.0, -0.0) returns -1.0.
    Parameters:
        x (float)
        y (float)

    Input:      copysign(2, -1)
    Output:     -2
```
```
fabs(x)
    Same as Python version in math module.
    Absolute value.
    Parameters:
        x (float)

    Input:      fabs(-1)
    Output:     1
```
```
abs(x)
    Same as Python version.
    Absolute value.
    Parameters:
        x (complex)

    Input:      abs(1 + i)
    Output:     1.414213562373
```
```
factorial(x)
    Return n factorial as an integer.
    Parameters:
        x (integer >= 0)

    Input:      factorial(5)
    Output:     120
```
```
floor(x)
    Return the floor of x, the largest integer less than or equal to x.
    Parameters:
        x (float)

    Input:      float(9.9)
    Output:     9
```
```
fmod(x, y)
    Same as Python version in math module.
    Return fmod(x, y), as defined by the platform C library. 
    Note that the Python expression x % y may not return the same result. 
    The intent of the C standard is that fmod(x, y) be exactly (mathematically; 
    to infinite precision) equal to x - n*y for some integer n such that 
    the result has the same sign as x and magnitude less than abs(y)
    Parameters:
        x (float)
        y (float)

    Input:      fmod(5, 3)
    Output:     2
```
```
frexp(x)
    Same as Python version in math module.
    Return the mantissa and exponent of x as the pair (m, e). 
    m is a float and e is an integer such that x == m * 2**e exactly. 
    If x is zero, returns (0.0, 0), otherwise 0.5 <= abs(m) < 1. 
    This is used to “pick apart” the internal representation of a float in a portable way.
    Parameters:
        x (float)

    Input:      frexp(0.0625)[0]
    Output:     0.5
```
```
fsum(seq)
    Return an accurate floating point sum of values in the iterable. 
    Avoids loss of precision by tracking multiple intermediate partial sums.
    Parameters:
        seq (sequence)

    Input:      fsum((1, 0.1, 0.01))
    Output:     1.11
```
```
sum(x0, x1, ...)
sum(seq)
    Same as Python version.
    Sum of value.
    Parameters:
        x0 (complex)
        seq (sequence)

    Input:      sum(1, 0.1, 0.01)
    Output:     1.11

    Input:      sum((1, 0.1, 0.01))
    Output:     1.11
```
```
gcd(x0, x1, ...)
    Greatest common divisor.
    Parameters:
        x0 (integer >= 0)

    Input:      gcd(6, 12, 18)
    Output:     6
```
```
isqrt(n)
    Same as Python version in math module.
    Return the integer square root of the nonnegative integer n. 
    This is the floor of the exact square root of n, or equivalently the 
    greatest integer a such that a² ≤ n.
    Parameters:
        x0 (integer >= 0)

    Input:      isqrt(65)
    Output:     8
```
```
lcm(x0, x1, ...)
    Least common multiple.
    Parameters:
        x0 (integer >= 0)

    Input:      lcm(6, 12, 18)
    Output:     36
```
```
ldexp(x, y)
    Same as Python version in math module.
    Return x * (2**y). This is essentially the inverse of function frexp().
    Parameters:
        x (float)
        y (integer)

    Input:      ldexp(0.5, -3)
    Output:     0.0625
```
```
modf(x)
    Same as Python version in math module.
    Return the fractional and integer parts of x. Both results carry the sign of x and are floats.
    Parameters:
        x (float)

    Input:      modf(5.2)[0]
    Output:     0.2
```
```
nextafter(x, y)
    Same as Python version in math module.
    Return the next floating-point value after x towards y.
    If x is equal to y, return y.
    Parameters:
        x (float)
        y (float)

    Input:      nextafter(5, 1)
    Output:     4.999999999999
```
```
P(n, r)
perm(n, r)
    Permutation
    Parameters:
        n (integer >= 0)
        r (integer >= 0)

    Input:      perm(5, 2)
    Output:     20
```
```
prod(x0, x1, ...)
prod(seq, start=1)
    Same as Python version in math module.
    Calculate the product of all the elements in the input iterable. 
    The default start value for the product is 1.
    When the iterable is empty, return the start value. 
    This function is intended specifically for use with numeric values and may 
    reject non-numeric types.
    Parameters:
        x0 (float)
        seq (sequence)
        start (float (optional))

    Input:      prod(4,5,6)
    Output:     120

    Input:      prod((4,5,6))
    Output:     120
```
```
remainder(x, y)
    Same as Python version in math module.
    Return the IEEE 754-style remainder of x with respect to y. 
    For finite x and finite nonzero y, this is the difference x - n*y, 
    where n is the closest integer to the exact value of the quotient x / y. 
    If x / y is exactly halfway between two consecutive integers, 
    the nearest even integer is used for n. The remainder r = remainder(x, y) 
    thus always satisfies abs(r) <= 0.5 * abs(y).
    Special cases follow IEEE 754: in particular, 
    remainder(x, math.inf) is x for any finite x, 
    and remainder(x, 0) and remainder(math.inf, x) raise ValueError for any non-NaN x. 
    If the result of the remainder operation is zero, that zero will have the same sign as x.
    Parameters:
        x (float)
        y (float)

    Input:      remainder(5, -3)
    Output:     -1
```
```
trunc(x)
    Same as Python version in math module.
    Return x with the fractional part removed, leaving the integer part. 
    This rounds toward 0: trunc() is equivalent to floor() for positive x, 
    and equivalent to ceil() for negative x. If x is not a float, delegates to x.__trunc__, 
    which should return an Integral value.
    Parameters:
        x (float)

    Input:      trunc(pi)
    Output:     3
```
```
ulp(x)
    Same as Python version in math module.
    Return the value of the least significant bit of the float x:
    If x is a NaN (not a number), return x.
    If x is negative, return ulp(-x).
    If x is a positive infinity, return x.
    If x is equal to zero, return the smallest positive denormalized representable 
    float (smaller than the minimum positive normalized float, sys.float_info.min).
    If x is equal to the largest positive representable float, 
    return the value of the least significant bit of x, 
    such that the first float smaller than x is x - ulp(x).
    Otherwise (x is a positive finite number), 
    return the value of the least significant bit of x, 
    such that the first float bigger than x is x + ulp(x).
    ULP stands for “Unit in the Last Place”.
    Parameters:
        x (float)

    Input:      ulp(10^12)
    Output:     0.0001220703
```
```
cbrt(x)
    Same as Python version in math module.
    Return the cube root of x.
    Parameters:
        x (float)

    Input:      cbrt(8)
    Output:     2
```
```
exp2(x)
    Same as Python version in math module.
    Return 2 raised to the power x.
    Parameters:
        x (float)

    Input:      exp2(5)
    Output:     32
```
```
expm1(x)
    Same as Python version in math module.
    Return e raised to the power x, minus 1. Here e is the base of natural logarithms. 
    For small floats x, the subtraction in exp(x) - 1 can result in a significant loss 
    of precision; the expm1() function provides a way to compute 
    this quantity to full precision.
    Parameters:
        x (float)

    Input:      expm1(3)
    Output:     19.085536923188
```
```
log1p(x)
    Same as Python version in math module.
    Return the natural logarithm of 1+x (base e). 
    The result is calculated in a way which is accurate for x near zero.
    Parameters:
        x (float)

    Input:      log1p(e-1)
    Output:     1
```
```
atan2(y, x)
    Same as Python version in math module.
    Return atan(y / x), in radians. The result is between -pi and pi. 
    The vector in the plane from the origin to point (x, y) 
    makes this angle with the positive X axis. The point of atan2() is that the signs of 
    both inputs are known to it, so it can compute the correct quadrant for the angle. 
    For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.
    Parameters:
        y (float)
        x (float)

    Input:      atan2(-1, -1)
    Output:     -2.356194490192
```
```
dist(p, q)
    Same as Python version in math module.
    Return the Euclidean distance between two points p and q, 
    each given as a sequence (or iterable) of coordinates. 
    The two points must have the same dimension.
    Parameters:
        p (coordinate)
        q (coordinate)

    Input:      dist((5,0,0), (8,0,0))
    Output:     3
```
```
hypot(x0, x1, ...)
    Same as Python version in math module.
    Return the Euclidean norm, sqrt(sum(x**2 for x in coordinates)). 
    This is the length of the vector from the origin to the point given by the coordinates.
    For a two dimensional point (x, y), 
    this is equivalent to computing the hypotenuse of a right triangle using 
    the Pythagorean theorem, sqrt(x*x + y*y).
    Parameters:
        x0 (coordinate)

    Input:      hypot(5, 6)
    Output:     7.810249675907
```
```
degrees(x)
    Same as Python version in math module.
    Convert angle x from radians to degrees.
    Parameters:
        x (float)

    Input:      degrees(pi)
    Output:     180
```
```
radians(x)
    Same as Python version in math module.
    Convert angle x from degrees to radians.
    Parameters:
        x (float)

    Input:      radians(180)
    Output:     3.1415926535898
```
```
erf(x)
    Same as Python version in math module.
    Return the error function at x.
    Parameters:
        x (float)

    Input:      erf(2)
    Output:     0.995322265019
```
```
erfc(x)
    Same as Python version in math module.
    Return the complementary error function at x. 
    The complementary error function is defined as 1.0 - erf(x). 
    It is used for large values of x where a subtraction from one would cause a loss of significance.
    Parameters:
        x (float)

    Input:      erfc(2)
    Output:     0.004677734981047
```
```
gamma(x)
    Same as Python version in math module.
    Return the Gamma function at x.
    Parameters:
        x (float)

    Input:      gamma(2.2)
    Output:     1.1018024908797
```
```
round(x, places=0)
    Returns a number that is a rounded version of the specified number, 
    with the specified number of decimals.
    Parameters:
        x (float)
        places (integer (optional))

    Input:      round(5.5)
    Output:     6

    Input:      round(14.5, -1)
    Output:     10
```
```
pow(base, power)
    Same as Python version.
    Power.
    Parameters:
        base (complex)
        power (complex)

    Input:      pow(2, 3)
    Output:     8
```
```
min(x0, x1, ...)
    Return the smallest item.
    Parameters:
        x0 (float)

    Input:      min(1, 2, 3)
    Output:     1
```
```
max(x0, x1, ...)
    Return the largest item.
    Parameters:
        x0 (float)

    Input:      max(1, 2, 3)
    Output:     3
```
