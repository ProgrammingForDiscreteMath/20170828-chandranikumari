from math import sqrt,atan,log
class ComplexNumber:
    """
    The class of complex numbers.
    """
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary part.
        """
        self.real = real_part
        self.imaginary = imaginary_part
    def __repr__(self):
        """
        Return the string representation of self.
        """
        return "%s + %s i"%(self.real, self.imaginary)
    def __eq__(self, other):
        """
        Test if ``self`` equals ``other``.
        
        Two complex numbers are equal if their real parts are equal and
        their imaginary parts are equal.
        """
        return self.real == other.real and self.imaginary == other.imaginary
    def complex_conjugate(self):
        """
        This function will not return anything but when it called replaces
        the instance by its complex conjugate
        """
        self.imaginary=-self.imaginary
        
    def modulus(self):
        """
        Return the modulus of self.
        
        The modulus (or absolute value) of a complex number is the square
        root of the sum of squares of its real and imaginary parts.
        """
        return sqrt(self.real**2 + self.imaginary**2)
    def sum(self, other):
        """
        Return the sum of ``self`` and ``other``.
        """
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def product(self, other):
        """
        Return the product of two complex number ``self`` and ``other``.

        (a+ib)(c+id)=(ac-bd)+(ad+bc)i

        The real part (ac-bd) of the product, is the product of the real parts minus the product of the imaginary parts,
        but , the imaginary part (ad+bc) of the product, is the sum of the two products of one real part and the other imaginary part

        """
        return ComplexNumber((self.real*other.real)-(self.imaginary*other.imaginary) ,(self.real*other.imaginary) + (self.imaginary*other.real))



class NonZeroComplexNumber(ComplexNumber):
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary parts after checking validity.
        """
        if real_part == 0 and imaginary_part == 0:
            raise ValueError("Real or imaginary part should be nonzero.")
        return ComplexNumber.__init__(self, real_part, imaginary_part)
    def inverse(self):
        """
        Return the multiplicative inverse of ``self``.
        """
        den = self.real**2 + self.imaginary**2
        return NonZeroComplexNumber(self.real/den, -self.imaginary/den)
    
    def polar_coordinates(self):
        """
        Return the polar coordinates of ``self``.
        """
        r=sqrt(self.real**2+self.imaginary**2)
        theta=atan(float(self.imaginary)/float(self.real))
        return (r,theta)
    
    def logarithm(self):
        """
        Return the Principal branch of log
        
        if z=a+ib is the complex number and |z| is the modulus and arg(z) is the argument then
        Principal is Log(a+ib)
        
        Log(a+ib)= ln(|z|) + i arg(z)
        
        """
        [r,t]=self.polar_coordinates()
        return "%s + %s i"%(log(r),t)
